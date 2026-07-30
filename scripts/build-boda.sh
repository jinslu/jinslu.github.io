#!/bin/bash
# 构建博达平台版本（lu.whu.edu.cn）
# 用法：bash scripts/build-boda.sh
# 构建完成后直接从 _boda/ 目录上传文件到博达，无需打包。

set -e
SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "→ 构建博达版本（url: https://lu.whu.edu.cn）..."
cd "$SITE_DIR"
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll build \
  --config _config.yml,_config.boda.yml

# ── 生成博达静态 HTML 文件（修正内部链接）──────────────────────────
echo "→ 生成博达静态 HTML 文件..."
python3 << 'PYEOF'
import os

SITE = os.path.join(os.environ.get("SITE_DIR", "."), "_boda")
PAGES = ["research", "publications", "members", "news", "contact", "join"]

def fix_links(html):
    for page in PAGES:
        html = html.replace(f'href="/{page}/"', f'href="/{page}.html"')
        html = html.replace(f'href="/{page}/#', f'href="/{page}.html#')
    return html

# 修正 index.html 中的内部链接
index_path = os.path.join(SITE, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()
with open(index_path, "w", encoding="utf-8") as f:
    f.write(fix_links(content))
print("  ✓ index.html (链接已修正)")

# 生成各栏目的 flat HTML 文件
for page in PAGES:
    src = os.path.join(SITE, page, "index.html")
    dst = os.path.join(SITE, f"{page}.html")
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    with open(dst, "w", encoding="utf-8") as f:
        f.write(fix_links(content))
    print(f"  + {page}.html")
PYEOF

# ── 清理博达不需要的文件 ─────────────────────────────────────────
echo "→ 清理多余文件..."
rm -f  _boda/CNAME _boda/README.md _boda/feed.xml _boda/boda-upload.zip
rm -rf _boda/scripts _boda/wiki
for page in research publications members news contact join; do
  rm -rf "_boda/$page"
done
echo "  ✓ 完成"

echo ""
echo "✓ 完成！_boda/ 目录已就绪，可直接上传到博达。"
echo ""
echo "  ┌─ 博达上传指南 ──────────────────────────────────────────────────┐"
echo "  │ 【首页模板（每次更新内容时）】                                   │"
echo "  │   文件|模板 → 新建/更新模板 → 选用本地HTML源文件：               │"
echo "  │     首页 : _boda/index.html → 模板名 index                      │"
echo "  │                                                                  │"
echo "  │ 【其他页面（静态文件，每次更新内容时）】                          │"
echo "  │   文件|模板 → 上传文件（直接上传到根目录）：                      │"
echo "  │     _boda/research.html                                          │"
echo "  │     _boda/publications.html                                      │"
echo "  │     _boda/members.html                                           │"
echo "  │     _boda/news.html                                              │"
echo "  │     _boda/contact.html                                           │"
echo "  │     _boda/join.html                                              │"
echo "  │                                                                  │"
echo "  │ 【静态资源（首次或资源有变动时）】                                │"
echo "  │   文件|模板 → 批量上传：                                         │"
echo "  │     CSS/JS : _boda/assets/          → 上传到 assets/            │"
echo "  │     图片   : _boda/user_data/images/ → 上传到 user_data/images/ │"
echo "  │     PDF    : _boda/user_data/pdf/    → 上传到 user_data/pdf/    │"
echo "  └──────────────────────────────────────────────────────────────────┘"
