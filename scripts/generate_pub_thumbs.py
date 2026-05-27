"""
Extract key figure thumbnails from publication PDFs using PyMuPDF.

Strategy:
  - Scan every page of the PDF for embedded raster images.
  - Keep images that are ≥ 280 px wide AND ≥ 180 px tall (original res).
  - Discard images with extreme aspect ratios (< 0.25 or > 4.5) — headers/banners.
  - Among qualifying images, pick the one with the largest area found on the
    earliest page (page 1 first, then page 2 …).
  - Fall back to rendering page 1 at 150 dpi if no embedded image qualifies.
  - Output: 120 px-wide JPEG, height proportional.
"""

import os, json
import fitz                          # PyMuPDF
from PIL import Image
import io

BASE      = os.path.dirname(os.path.abspath(__file__))
PDF_DIR   = os.path.join(BASE, "user_data", "pdf")
OUT_DIR   = os.path.join(BASE, "user_data", "images", "pub_thumbs")
DATA_JSON = os.path.join(BASE, "_data", "publications.json")

os.makedirs(OUT_DIR, exist_ok=True)

THUMB_W   = 240      # output at 2× for retina; CSS displays at 120px
MIN_W     = 280      # min original image width to consider
MIN_H     = 180      # min original image height to consider
MIN_AR    = 0.25     # min aspect ratio (h/w)
MAX_AR    = 4.5      # max aspect ratio (h/w)
FORCE     = True     # set True to regenerate existing thumbs


def best_image_from_pdf(pdf_path):
    """Return a PIL Image of the best figure found in the PDF."""
    doc = fitz.open(pdf_path)
    best_pil  = None
    best_area = 0
    best_page = 9999

    for page_num, page in enumerate(doc):
        imgs = page.get_images(full=True)
        for img_info in imgs:
            xref = img_info[0]
            try:
                base = doc.extract_image(xref)
            except Exception:
                continue
            w, h = base["width"], base["height"]
            if w < MIN_W or h < MIN_H:
                continue
            ar = h / w
            if ar < MIN_AR or ar > MAX_AR:
                continue
            area = w * h
            if page_num < best_page or (page_num == best_page and area > best_area):
                try:
                    pil = Image.open(io.BytesIO(base["image"]))
                    if pil.mode in ("RGBA", "P", "CMYK"):
                        pil = pil.convert("RGB")
                    best_pil  = pil
                    best_area = area
                    best_page = page_num
                except Exception:
                    continue

    # Fall back: render first page
    if best_pil is None:
        page = doc[0]
        mat  = fitz.Matrix(300 / 72, 300 / 72)
        pix  = page.get_pixmap(matrix=mat)
        best_pil = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    doc.close()
    return best_pil


def trim_and_resize(img, thumb_w):
    """Trim white/transparent margins then resize to thumb_w wide."""
    import numpy as np
    if img.mode == "RGBA":
        alpha = img.split()[-1]
        bbox  = alpha.getbbox()
        if bbox:
            img = img.crop(bbox)
    # Trim white margins via numpy
    try:
        rgb = img.convert("RGB")
        arr = np.array(rgb)
        mask = ~((arr[:,:,0]>240) & (arr[:,:,1]>240) & (arr[:,:,2]>240))
        rows = np.any(mask, axis=1)
        cols = np.any(mask, axis=0)
        if rows.any() and cols.any():
            rmin, rmax = np.where(rows)[0][[0,-1]]
            cmin, cmax = np.where(cols)[0][[0,-1]]
            img = img.crop((cmin, rmin, cmax+1, rmax+1))
    except Exception:
        pass
    ratio = thumb_w / img.width
    thumb = img.resize((thumb_w, int(img.height * ratio)), Image.LANCZOS)
    if thumb.mode != "RGB":
        thumb = thumb.convert("RGB")
    return thumb


def make_thumb(key, pdf_rel):
    if not pdf_rel:
        return
    pdf_abs = os.path.join(BASE, pdf_rel.lstrip("/"))
    out = os.path.join(OUT_DIR, f"{key}.jpg")
    if os.path.exists(out) and not FORCE:
        print(f"  EXISTS: {key}.jpg")
        return

    # ── Priority 1: companion image in same dir as PDF (same stem, any ext) ──
    pdf_stem = os.path.splitext(pdf_abs)[0]
    companion = None
    for ext in (".png", ".jpg", ".jpeg", ".tif", ".tiff"):
        candidate = pdf_stem + ext
        if os.path.exists(candidate):
            companion = candidate
            break

    try:
        if companion:
            img = Image.open(companion)
            # Trim white/transparent margins only — keep original resolution
            img = trim_and_resize(img, img.width)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(out, "JPEG", quality=95)
            print(f"  OK  {key}.jpg  [companion: {os.path.basename(companion)}]  "
                  f"→ {img.width}×{img.height}  (original res)")
            return

        # ── Priority 2: extract best figure from PDF ──
        if not os.path.exists(pdf_abs):
            print(f"  SKIP (no PDF): {key}")
            return
        img   = best_image_from_pdf(pdf_abs)
        ratio = THUMB_W / img.width
        thumb = img.resize((THUMB_W, int(img.height * ratio)), Image.LANCZOS)
        if thumb.mode != "RGB":
            thumb = thumb.convert("RGB")
        thumb.save(out, "JPEG", quality=95)
        print(f"  OK  {key}.jpg  [PDF extract]  orig={img.width}×{img.height}  "
              f"→ {THUMB_W}×{int(img.height*ratio)}")
    except Exception as e:
        print(f"  ERR {key}: {e}")


with open(DATA_JSON) as f:
    data = json.load(f)

print("=== Journal Articles ===")
for p in data.get("articles", []):
    make_thumb(p["key"], p.get("file", ""))

print("\n=== Conference Papers ===")
for p in data.get("conferences", []):
    make_thumb(p["key"], p.get("file", ""))
