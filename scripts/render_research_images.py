"""
Render 4 scientific diagrams for lab website research area cards.
Output: user_data/images/research/research-[1-4].jpg, 900×500 px
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, Arc, FancyBboxPatch, Wedge
from matplotlib.collections import LineCollection
from scipy.ndimage import gaussian_filter
import os

# ── colour palette ──────────────────────────────────────────────────────────
BG      = '#071628'
GOLD    = '#C8973A'
LGOLD   = '#EDBE6A'
CYAN    = '#3ADEE8'
LCYAN   = '#9AEEF5'
WHITE   = '#F0F4FF'
GREY    = '#7A8BA0'
GREEN   = '#4AE89A'
PURPLE  = '#A07AE8'
RED     = '#E85A4A'
BLUE    = '#3A8BE8'

W_IN, H_IN = 9, 5   # inches
DPI = 100            # → 900 × 500 px

OUT_DIR = os.path.join(os.path.dirname(__file__),
                       'user_data', 'images', 'research')
os.makedirs(OUT_DIR, exist_ok=True)


def new_fig():
    fig, ax = plt.subplots(figsize=(W_IN, H_IN), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('auto')
    ax.axis('off')
    return fig, ax


def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=DPI, bbox_inches='tight',
                pad_inches=0, facecolor=BG, format='jpeg',
                pil_kwargs={'quality': 92})
    plt.close(fig)
    print(f'  saved → {path}')


# ════════════════════════════════════════════════════════════════════════════
#  1  光致推拉  Light-Induced Pulling & Pushing
# ════════════════════════════════════════════════════════════════════════════
def draw_research1():
    fig, ax = new_fig()

    # ── background grid (subtle) ──────────────────────────────────────────
    for x in np.linspace(0, 1, 20):
        ax.axvline(x, color='#0D2040', lw=0.4, zorder=0)
    for y in np.linspace(0, 1, 12):
        ax.axhline(y, color='#0D2040', lw=0.4, zorder=0)

    # ── Gaussian beam from the left ───────────────────────────────────────
    xs = np.linspace(0.0, 0.48, 300)
    w0 = 0.06
    for n, alpha in [(4, 0.06), (3, 0.11), (2, 0.18), (1, 0.30), (0, 0.55)]:
        offset = w0 * (n + 1)
        ax.fill_between(xs,
                        0.50 - offset - 0.003,
                        0.50 - offset + 0.003,
                        color=CYAN, alpha=alpha, lw=0, zorder=2)
        ax.fill_between(xs,
                        0.50 + offset - 0.003,
                        0.50 + offset + 0.003,
                        color=CYAN, alpha=alpha, lw=0, zorder=2)
    # bright central ray
    ax.fill_between(xs, 0.497, 0.503, color=CYAN, alpha=0.9, lw=0, zorder=3)

    # faint beam glow
    for y_off, a in [(0, 0.22), (0.05, 0.12), (-0.05, 0.12), (0.10, 0.05), (-0.10, 0.05)]:
        ax.fill_between(xs, 0.497 + y_off, 0.503 + y_off,
                        color=CYAN, alpha=a, lw=0, zorder=1)

    # ── gold microplate ───────────────────────────────────────────────────
    plate = FancyBboxPatch((0.44, 0.42), 0.12, 0.16,
                           boxstyle='round,pad=0.008',
                           fc=GOLD, ec=LGOLD, lw=2, zorder=6)
    ax.add_patch(plate)
    # sheen
    ax.fill_between([0.45, 0.50], [0.555, 0.555], [0.565, 0.565],
                    color=LGOLD, alpha=0.5, zorder=7)
    ax.text(0.50, 0.50, 'Au', color=BG, fontsize=14, fontweight='bold',
            ha='center', va='center', zorder=8)

    # ── scattering rays from plate ────────────────────────────────────────
    center = (0.50, 0.50)
    for angle_deg in range(30, 360, 40):
        angle = np.radians(angle_deg)
        x2 = center[0] + 0.28 * np.cos(angle)
        y2 = center[1] + 0.28 * np.sin(angle)
        ax.annotate('', xy=(x2, y2), xytext=center,
                    arrowprops=dict(arrowstyle='->', color=LCYAN,
                                   lw=0.8, alpha=0.4), zorder=5)

    # ── force arrows ──────────────────────────────────────────────────────
    # pulling arrow (←, to the left)
    ax.annotate('', xy=(0.26, 0.50), xytext=(0.43, 0.50),
                arrowprops=dict(arrowstyle='->', color=LGOLD,
                                lw=3.5, mutation_scale=22), zorder=9)
    ax.text(0.18, 0.50, 'Pull', color=LGOLD, fontsize=11, fontweight='bold',
            ha='center', va='center', zorder=9)

    # pushing arrow (→, to the right)
    ax.annotate('', xy=(0.76, 0.50), xytext=(0.57, 0.50),
                arrowprops=dict(arrowstyle='->', color=RED,
                                lw=3.5, mutation_scale=22), zorder=9)
    ax.text(0.84, 0.50, 'Push', color=RED, fontsize=11, fontweight='bold',
            ha='center', va='center', zorder=9)

    # ── photophoretic force label (upward) ───────────────────────────────
    ax.annotate('', xy=(0.50, 0.75), xytext=(0.50, 0.60),
                arrowprops=dict(arrowstyle='->', color=GREEN,
                                lw=2.5, mutation_scale=18), zorder=9)
    ax.text(0.50, 0.80, 'Photophoresis', color=GREEN, fontsize=9,
            ha='center', va='bottom', zorder=9)

    # ── beam label ───────────────────────────────────────────────────────
    ax.text(0.10, 0.62, 'Laser beam', color=LCYAN, fontsize=9,
            ha='center', va='bottom', style='italic', zorder=9)

    # ── title ─────────────────────────────────────────────────────────────
    ax.text(0.50, 0.96, 'Light-Induced Pulling & Pushing',
            color=WHITE, fontsize=13, fontweight='bold',
            ha='center', va='top', zorder=10)
    ax.text(0.50, 0.04, 'Optical force + Photophoretic force  |  Phys. Rev. Lett. 2017',
            color=GREY, fontsize=8, ha='center', va='bottom', zorder=10)

    save(fig, 'research-1.jpg')


# ════════════════════════════════════════════════════════════════════════════
#  2  光驱马达  Light-Driven Nanomotors (Lamb-wave)
# ════════════════════════════════════════════════════════════════════════════
def draw_research2():
    fig, ax = new_fig()

    # ── substrate surface ────────────────────────────────────────────────
    ax.fill_between([0, 1], [0.26, 0.26], [0.31, 0.31],
                    color='#1A3050', zorder=1)
    ax.plot([0, 1], [0.31, 0.31], color='#2A5080', lw=1.5, zorder=2)

    # Lamb wave ripples on surface
    xs = np.linspace(0, 1, 500)
    for k, (phase, alpha, lw) in enumerate([
            (0.0, 0.7, 1.5), (0.3, 0.45, 1.0), (0.6, 0.25, 0.7)]):
        wave = 0.31 + 0.018 * np.sin(2 * np.pi * 8 * xs + phase * np.pi)
        ax.plot(xs, wave, color=CYAN, alpha=alpha, lw=lw, zorder=3)

    # ── nano-plate (rotor) ────────────────────────────────────────────────
    cx, cy = 0.50, 0.455
    theta = np.radians(20)
    hw, hh = 0.10, 0.025
    corners = np.array([
        [-hw, -hh], [hw, -hh], [hw, hh], [-hw, hh]
    ])
    rot = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])
    corners = (rot @ corners.T).T + np.array([cx, cy])
    plate = plt.Polygon(corners, closed=True,
                        fc=GOLD, ec=LGOLD, lw=2, zorder=7)
    ax.add_patch(plate)

    # ── rotation arrows ───────────────────────────────────────────────────
    for start_ang, end_ang, color in [
            (200, 310, LGOLD), (20, 130, LGOLD)]:
        arc = Arc((cx, cy), 0.28, 0.28,
                  angle=0, theta1=start_ang, theta2=end_ang,
                  color=color, lw=2.5, zorder=8)
        ax.add_patch(arc)
    # arrowhead for rotation direction
    arr_angle = np.radians(310)
    ax.annotate('', xy=(cx + 0.14*np.cos(arr_angle + 0.4),
                        cy + 0.14*np.sin(arr_angle + 0.4)),
                xytext=(cx + 0.14*np.cos(arr_angle),
                        cy + 0.14*np.sin(arr_angle)),
                arrowprops=dict(arrowstyle='->', color=LGOLD,
                                lw=2, mutation_scale=16), zorder=9)
    arr_angle2 = np.radians(130)
    ax.annotate('', xy=(cx + 0.14*np.cos(arr_angle2 + 0.4),
                        cy + 0.14*np.sin(arr_angle2 + 0.4)),
                xytext=(cx + 0.14*np.cos(arr_angle2),
                        cy + 0.14*np.sin(arr_angle2)),
                arrowprops=dict(arrowstyle='->', color=LGOLD,
                                lw=2, mutation_scale=16), zorder=9)

    # ── pulsed laser beam ─────────────────────────────────────────────────
    # vertical beam from above
    for x_off, alpha in [(0, 0.8), (0.015, 0.3), (-0.015, 0.3),
                          (0.030, 0.10), (-0.030, 0.10)]:
        ax.fill_between([cx + x_off - 0.003, cx + x_off + 0.003],
                        [cy + 0.02, cy + 0.02],
                        [0.95, 0.95],
                        color=CYAN, alpha=alpha, zorder=4)

    # pulse markers on beam
    for y_pulse in [0.78, 0.68, 0.58]:
        ax.fill_between([cx - 0.012, cx + 0.012],
                        [y_pulse - 0.008, y_pulse - 0.008],
                        [y_pulse + 0.008, y_pulse + 0.008],
                        color=LCYAN, alpha=0.8, zorder=5)

    ax.text(cx + 0.06, 0.75, 'Pulsed\nlaser', color=LCYAN, fontsize=9,
            ha='left', va='center', zorder=9)

    # ── Lamb wave propagation arrows ──────────────────────────────────────
    ax.annotate('', xy=(0.15, 0.32), xytext=(0.42, 0.32),
                arrowprops=dict(arrowstyle='<-', color=CYAN,
                                lw=1.5, mutation_scale=12), zorder=6)
    ax.annotate('', xy=(0.85, 0.32), xytext=(0.58, 0.32),
                arrowprops=dict(arrowstyle='<-', color=CYAN,
                                lw=1.5, mutation_scale=12), zorder=6)
    ax.text(0.50, 0.23, 'Lamb waves', color=CYAN, fontsize=9,
            ha='center', va='top', zorder=6)

    # ── omega symbol ──────────────────────────────────────────────────────
    ax.text(cx, cy + 0.22, 'ω', color=LGOLD, fontsize=18,
            ha='center', va='bottom', style='italic', zorder=9)

    # ── title ─────────────────────────────────────────────────────────────
    ax.text(0.50, 0.96, 'Light-Driven Nanomotors',
            color=WHITE, fontsize=13, fontweight='bold',
            ha='center', va='top', zorder=10)
    ax.text(0.50, 0.04, 'Lamb-wave actuation  |  Science Advances 2019',
            color=GREY, fontsize=8, ha='center', va='bottom', zorder=10)

    save(fig, 'research-2.jpg')


# ════════════════════════════════════════════════════════════════════════════
#  3  片上光镊  On-chip Optical Tweezers
# ════════════════════════════════════════════════════════════════════════════
def draw_research3():
    fig, ax = new_fig()

    # ── chip substrate ────────────────────────────────────────────────────
    chip = FancyBboxPatch((0.05, 0.12), 0.90, 0.60,
                          boxstyle='round,pad=0.01',
                          fc='#0F2030', ec='#1A3A55', lw=2, zorder=1)
    ax.add_patch(chip)

    # ── waveguide ridges ──────────────────────────────────────────────────
    wg_y_bottom = 0.43
    wg_y_top    = 0.57

    # bottom waveguide (light blue ridge)
    ax.fill_between([0.07, 0.93], [wg_y_bottom - 0.030, wg_y_bottom - 0.030],
                    [wg_y_bottom + 0.030, wg_y_bottom + 0.030],
                    color='#1A4060', zorder=2)
    ax.fill_between([0.07, 0.93], [wg_y_bottom - 0.012, wg_y_bottom - 0.012],
                    [wg_y_bottom + 0.012, wg_y_bottom + 0.012],
                    color='#2A6090', zorder=3)

    # top waveguide
    ax.fill_between([0.07, 0.93], [wg_y_top - 0.030, wg_y_top - 0.030],
                    [wg_y_top + 0.030, wg_y_top + 0.030],
                    color='#1A4060', zorder=2)
    ax.fill_between([0.07, 0.93], [wg_y_top - 0.012, wg_y_top - 0.012],
                    [wg_y_top + 0.012, wg_y_top + 0.012],
                    color='#2A6090', zorder=3)

    # ── propagating light in waveguides ───────────────────────────────────
    for wg_y, alpha in [(wg_y_bottom, 0.7), (wg_y_top, 0.7)]:
        xs = np.linspace(0.10, 0.88, 200)
        intensity = 0.5 + 0.5 * np.sin(2 * np.pi * 12 * xs)
        for i in range(len(xs) - 1):
            c = intensity[i]
            ax.fill_between([xs[i], xs[i+1]],
                            [wg_y - 0.008, wg_y - 0.008],
                            [wg_y + 0.008, wg_y + 0.008],
                            color=(c * 0.2, c * 0.8, 1.0),
                            alpha=alpha * c, lw=0, zorder=4)

    # ── freeform lens / focus element ─────────────────────────────────────
    lens_x = 0.50
    lens_y = (wg_y_bottom + wg_y_top) / 2

    # lens structure (metalens pattern – rings)
    for r, lw, alpha in [(0.065, 4, 0.9), (0.050, 3, 0.7),
                          (0.036, 2, 0.55), (0.022, 2, 0.4)]:
        circ = plt.Circle((lens_x, lens_y), r,
                           fc='none', ec=GOLD, lw=lw, alpha=alpha, zorder=8)
        ax.add_patch(circ)

    # ── converging rays ───────────────────────────────────────────────────
    focus_y = lens_y + 0.18
    rays_y0_bottom = wg_y_bottom + 0.012
    rays_y0_top    = wg_y_top    - 0.012
    for x_src in [0.38, 0.44, 0.50, 0.56, 0.62]:
        # from bottom wg upward
        ax.plot([x_src, lens_x], [rays_y0_bottom, lens_y - 0.066],
                color=CYAN, lw=0.8, alpha=0.5, zorder=5)
        ax.plot([x_src, lens_x], [rays_y0_top, lens_y + 0.066],
                color=CYAN, lw=0.8, alpha=0.5, zorder=5)
        # from lens to focus
        ax.plot([lens_x, lens_x], [lens_y + 0.066, focus_y],
                color=LCYAN, lw=0.9, alpha=0.5, zorder=5)

    # converging cone
    for x_off, alpha in [(0.07, 0.3), (0.05, 0.5), (0.02, 0.7)]:
        ax.fill([lens_x - x_off, lens_x, lens_x + x_off, lens_x],
                [lens_y + 0.065, focus_y - 0.01,
                 lens_y + 0.065, lens_y + 0.065],
                color=CYAN, alpha=alpha, zorder=5)

    # ── trapped particle ──────────────────────────────────────────────────
    particle = plt.Circle((lens_x, focus_y), 0.038,
                           fc='#D0A050', ec=LGOLD, lw=2.5, zorder=10)
    ax.add_patch(particle)
    # glow
    for r_glow, a_glow in [(0.055, 0.15), (0.070, 0.08), (0.090, 0.04)]:
        glow = plt.Circle((lens_x, focus_y), r_glow,
                          fc=LGOLD, ec='none', alpha=a_glow, zorder=9)
        ax.add_patch(glow)

    # trap force arrows (↕ on particle)
    ax.annotate('', xy=(lens_x, focus_y + 0.052),
                xytext=(lens_x, focus_y + 0.10),
                arrowprops=dict(arrowstyle='->', color=LGOLD,
                                lw=1.8, mutation_scale=14), zorder=11)
    ax.annotate('', xy=(lens_x, focus_y - 0.052),
                xytext=(lens_x, focus_y - 0.10),
                arrowprops=dict(arrowstyle='->', color=LGOLD,
                                lw=1.8, mutation_scale=14), zorder=11)

    ax.text(lens_x + 0.11, focus_y, 'Trapped\nparticle',
            color=LGOLD, fontsize=8.5, ha='left', va='center', zorder=11)
    ax.text(lens_x - 0.04, lens_y - 0.01, 'Metalens',
            color=GOLD, fontsize=8, ha='right', va='center', zorder=11)

    # ── title ─────────────────────────────────────────────────────────────
    ax.text(0.50, 0.96, 'On-chip Optical Tweezers',
            color=WHITE, fontsize=13, fontweight='bold',
            ha='center', va='top', zorder=12)
    ax.text(0.50, 0.04, 'Freeform meta-optic elements  |  Optica 2021',
            color=GREY, fontsize=8, ha='center', va='bottom', zorder=12)

    save(fig, 'research-3.jpg')


# ════════════════════════════════════════════════════════════════════════════
#  4  集成光子  Cascaded-Mode Interferometers
# ════════════════════════════════════════════════════════════════════════════
def draw_research4():
    fig, ax = new_fig()

    # ── input spectrum (Gaussian-ish broadband) ───────────────────────────
    lam = np.linspace(0.0, 1.0, 400)
    spec_in  = np.exp(-((lam - 0.5) / 0.18)**2)

    def lorentzian(l, l0, gamma):
        return 1 / (1 + ((l - l0) / gamma)**2)

    # engineered output: narrow + flat-top via mode interference
    spec_out = (0.65 * lorentzian(lam, 0.50, 0.025)
              + 0.20 * lorentzian(lam, 0.50, 0.006)
              + 0.15 * np.exp(-((lam - 0.50) / 0.055)**4))
    spec_out = spec_out / spec_out.max()

    # spectrum panel boundaries
    sp_y0, sp_y1 = 0.54, 0.90
    sp_h = sp_y1 - sp_y0

    # ── input spectrum panel (left) ───────────────────────────────────────
    in_x0, in_x1 = 0.04, 0.22
    ax.fill_between([in_x0, in_x1], [sp_y0, sp_y0], [sp_y1, sp_y1],
                    color='#0A1E30', zorder=1)
    ax.plot([in_x0, in_x1, in_x1, in_x0, in_x0],
            [sp_y0, sp_y0, sp_y1, sp_y1, sp_y0],
            color='#1A3A55', lw=1, zorder=2)
    ax.text((in_x0 + in_x1) / 2, sp_y1 + 0.03, 'Input',
            color=GREY, fontsize=8.5, ha='center', va='bottom', zorder=3)

    # normalise spectrum into panel
    xs_in = in_x0 + (lam) * (in_x1 - in_x0)
    ys_in = sp_y0 + spec_in * sp_h * 0.88
    ax.plot(xs_in, ys_in, color=CYAN, lw=1.8, zorder=3)
    ax.fill_between(xs_in, sp_y0, ys_in, color=CYAN, alpha=0.25, zorder=2)

    # ── output spectrum panel (right) ────────────────────────────────────
    out_x0, out_x1 = 0.78, 0.96
    ax.fill_between([out_x0, out_x1], [sp_y0, sp_y0], [sp_y1, sp_y1],
                    color='#0A1E30', zorder=1)
    ax.plot([out_x0, out_x1, out_x1, out_x0, out_x0],
            [sp_y0, sp_y0, sp_y1, sp_y1, sp_y0],
            color='#1A3A55', lw=1, zorder=2)
    ax.text((out_x0 + out_x1) / 2, sp_y1 + 0.03, 'Output',
            color=GREY, fontsize=8.5, ha='center', va='bottom', zorder=3)

    xs_out = out_x0 + (lam) * (out_x1 - out_x0)
    ys_out = sp_y0 + spec_out * sp_h * 0.88
    ax.plot(xs_out, ys_out, color=LGOLD, lw=2, zorder=3)
    ax.fill_between(xs_out, sp_y0, ys_out, color=GOLD, alpha=0.30, zorder=2)

    # ── cascaded waveguide chain ──────────────────────────────────────────
    wg_y   = 0.36
    n_segs = 4
    seg_x0s = np.linspace(0.22, 0.58, n_segs + 1)
    seg_colors = [CYAN, BLUE, PURPLE, LGOLD]

    wg_h = 0.036
    for i in range(n_segs):
        x0 = seg_x0s[i]
        x1 = seg_x0s[i + 1]
        c  = seg_colors[i]

        # waveguide body
        rect = FancyBboxPatch((x0, wg_y - wg_h / 2), x1 - x0, wg_h,
                              boxstyle='round,pad=0.004',
                              fc=c, ec=WHITE, lw=0.7, alpha=0.85, zorder=5)
        ax.add_patch(rect)

        # mode label inside
        modes = ['TE₀', 'TE₁', 'TE₀', 'TE₁']
        ax.text((x0 + x1) / 2, wg_y, modes[i],
                color=BG, fontsize=7.5, fontweight='bold',
                ha='center', va='center', zorder=6)

        # connector / coupler at segment boundary
        if i < n_segs - 1:
            cx_c = seg_x0s[i + 1]
            coupler = FancyBboxPatch((cx_c - 0.008, wg_y - wg_h),
                                     0.016, 2 * wg_h,
                                     boxstyle='round,pad=0.003',
                                     fc=WHITE, ec=WHITE, lw=0, alpha=0.9,
                                     zorder=7)
            ax.add_patch(coupler)
            ax.text(cx_c, wg_y - wg_h - 0.04, 'MC',
                    color=WHITE, fontsize=6.5, ha='center', va='top', zorder=7)

    # ── input/output waveguide stubs ──────────────────────────────────────
    # input stub
    ax.fill_between([in_x1, seg_x0s[0]],
                    [wg_y - wg_h / 2 - 0.005] * 2,
                    [wg_y + wg_h / 2 + 0.005] * 2,
                    color='#1A3A55', zorder=4)
    ax.annotate('', xy=(seg_x0s[0], wg_y), xytext=(in_x1 + 0.01, wg_y),
                arrowprops=dict(arrowstyle='->', color=CYAN,
                                lw=1.5, mutation_scale=12), zorder=8)

    # output stub
    ax.fill_between([seg_x0s[-1], out_x0],
                    [wg_y - wg_h / 2 - 0.005] * 2,
                    [wg_y + wg_h / 2 + 0.005] * 2,
                    color='#1A3A55', zorder=4)
    ax.annotate('', xy=(out_x0 - 0.01, wg_y), xytext=(seg_x0s[-1], wg_y),
                arrowprops=dict(arrowstyle='->', color=LGOLD,
                                lw=1.5, mutation_scale=12), zorder=8)

    # vertical arrows connecting spectra to waveguide
    ax.annotate('', xy=((in_x0 + in_x1) / 2, sp_y0),
                xytext=((in_x0 + in_x1) / 2, wg_y + wg_h / 2 + 0.01),
                arrowprops=dict(arrowstyle='->', color=GREY,
                                lw=1, mutation_scale=10), zorder=3)
    ax.annotate('', xy=((out_x0 + out_x1) / 2, sp_y0),
                xytext=((out_x0 + out_x1) / 2, wg_y + wg_h / 2 + 0.01),
                arrowprops=dict(arrowstyle='<-', color=GREY,
                                lw=1, mutation_scale=10), zorder=3)

    # ── legend for MC ────────────────────────────────────────────────────
    ax.text(0.50, 0.12, 'MC = Mode Converter',
            color=GREY, fontsize=8, ha='center', va='bottom', zorder=6)

    # ── resonance ring (optional micro-ring resonator) ────────────────────
    ring_cx, ring_cy = 0.50, 0.22
    ring_r = 0.07
    ring = plt.Circle((ring_cx, ring_cy), ring_r,
                      fc='none', ec=BLUE, lw=2.5, alpha=0.85, zorder=5)
    ax.add_patch(ring)
    # coupling waveguide through ring
    ax.fill_between([ring_cx - ring_r - 0.04, ring_cx + ring_r + 0.04],
                    [ring_cy - ring_r - 0.018, ring_cy - ring_r - 0.018],
                    [ring_cy - ring_r - 0.004, ring_cy - ring_r - 0.004],
                    color=BLUE, alpha=0.7, zorder=4)
    ax.text(ring_cx, ring_cy, 'Ring', color=BLUE, fontsize=8,
            ha='center', va='center', zorder=6)

    # resonance comb on spectrum
    comb_x_center = (out_x0 + out_x1) / 2
    for lam_res in [0.42, 0.50, 0.58]:
        x_comb = out_x0 + lam_res * (out_x1 - out_x0)
        y_h = sp_y0 + lorentzian(lam_res, 0.50, 0.025) * sp_h * 0.88
        ax.plot([x_comb, x_comb], [sp_y0, y_h],
                color=WHITE, lw=0.8, alpha=0.4, zorder=4)

    # ── title ─────────────────────────────────────────────────────────────
    ax.text(0.50, 0.97, 'Integrated Photonics',
            color=WHITE, fontsize=13, fontweight='bold',
            ha='center', va='top', zorder=10)
    ax.text(0.50, 0.04, 'Cascaded transverse-mode interferometers  |  Science Advances 2025',
            color=GREY, fontsize=8, ha='center', va='bottom', zorder=10)

    save(fig, 'research-4.jpg')


# ── run all ──────────────────────────────────────────────────────────────────
print('Rendering research diagrams...')
draw_research1()
draw_research2()
draw_research3()
draw_research4()
print('Done.')
