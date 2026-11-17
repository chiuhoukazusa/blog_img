import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(5, 5.65, "Marching Tetrahedra Isosurface Extraction", ha="center", va="center",
        fontsize=23, fontweight="bold", color="#1a1a2e")
ax.text(5, 5.08,
        r"cube $\to$ 6 tetrahedra  $\quad$  sign mask $=\{0,1\}^4$  $\quad$  $t=\dfrac{-v_a}{v_b-v_a}$",
        ha="center", va="center", fontsize=12, color="#444444")

# --- left: a cube subdivided into 6 tetrahedra (main diagonal 0->7) ---
# draw cube front face + diagonal hints
cx, cy = 2.6, 2.9
s = 2.6
# front square
front = Polygon([(cx, cy), (cx+s, cy), (cx+s, cy+s), (cx, cy+s)],
                closed=True, facecolor="#e8eefc", edgecolor="#2d2d44", linewidth=2.2)
ax.add_patch(front)
# back square offset
ox, oy = 0.9, 0.85
back = Polygon([(cx+ox, cy+oy), (cx+s+ox, cy+oy), (cx+s+ox, cy+s+oy), (cx+ox, cy+s+oy)],
               closed=True, facecolor="#d6e0f5", edgecolor="#2d2d44", linewidth=1.8, linestyle="--")
ax.add_patch(back)
# connect corners
for i in range(4):
    fx = [cx, cx+s, cx+s, cx][i]; fy = [cy, cy, cy+s, cy+s][i]
    bx = fx+ox; by = fy+oy
    ax.plot([fx, bx], [fy, by], color="#2d2d44", linewidth=1.4)

# corner labels
ax.text(cx-0.18, cy-0.22, r"$0$", fontsize=13, fontweight="bold", color="#1a1a2e")
ax.text(cx+s+0.08, cy-0.22, r"$1$", fontsize=13, fontweight="bold", color="#1a1a2e")
ax.text(cx-0.18, cy+s+0.08, r"$2$", fontsize=13, fontweight="bold", color="#1a1a2e")
ax.text(cx+s+0.08, cy+s+0.08, r"$3$", fontsize=13, fontweight="bold", color="#1a1a2e")
ax.text(cx+ox-0.18, cy+oy-0.22, r"$4$", fontsize=13, fontweight="bold", color="#888")
ax.text(cx+ox+s+0.08, cy+oy-0.22, r"$5$", fontsize=13, fontweight="bold", color="#888")
ax.text(cx+ox-0.18, cy+oy+s+0.08, r"$6$", fontsize=13, fontweight="bold", color="#888")
ax.text(cx+ox+s+0.08, cy+oy+s+0.08, r"$7$", fontsize=13, fontweight="bold", color="#888")

# main diagonal 0 -> 7 (back top-right = 7  corner is cx+ox+s, cy+oy+s)
ax.add_patch(FancyArrowPatch((cx, cy), (cx+ox+s, cy+oy+s), arrowstyle="-|>",
             mutation_scale=14, color="#e67e22", linewidth=2.2, zorder=5))
ax.text(4.15, 3.75, r"main diagonal $0\!\to\!7$", fontsize=10, color="#d35400")

# --- right: a single tetrahedron with its isosurface triangle ---
# tetrahedron in 2D projection (triangle)
tv = [(7.0, 4.4), (9.2, 3.2), (7.6, 1.2)]
tet = Polygon(tv, closed=True, facecolor="#fdebd0", edgecolor="#2d2d44", linewidth=2.2)
ax.add_patch(tet)
ax.text(tv[0][0]-0.15, tv[0][1]+0.15, r"$p_0$", fontsize=13, fontweight="bold", color="#1a1a2e")
ax.text(tv[1][0]+0.1, tv[1][1], r"$p_1$", fontsize=13, fontweight="bold", color="#1a1a2e")
ax.text(tv[2][0]+0.1, tv[2][1]-0.2, r"$p_2$", fontsize=13, fontweight="bold", color="#1a1a2e")

# a triangle (isosurface cross-section) inside tetrahedron
it = [(7.9, 3.9), (8.6, 2.5), (7.5, 2.4)]
iso = Polygon(it, closed=True, facecolor="#e74c3c", alpha=0.55,
              edgecolor="#7a1f1a", linewidth=2.0, zorder=4)
ax.add_patch(iso)
ax.text(7.55, 3.35, r"isosurface", fontsize=11, fontweight="bold", color="#c0392b", zorder=6)

# edge intersection markers
for pt in it:
    ax.add_patch(Circle(pt, 0.055, facecolor="#1a1a2e", edgecolor="white", linewidth=1.2, zorder=6))
ax.text(8.0, 2.10, r"edge crossings $t=\dfrac{-v_a}{v_b-v_a}$",
        fontsize=9.5, color="#555")

# --- formula box ---
box = FancyBboxPatch((6.6, 0.55), 3.0, 1.35, boxstyle="round,pad=0.12",
                     linewidth=1.8, edgecolor="#2d2d44", facecolor="#fdf6e3")
ax.add_patch(box)
ax.text(8.1, 1.62, "3 intersections → 1 tri", ha="center", va="center",
        fontsize=11, color="#555", fontweight="bold")
ax.text(8.1, 1.18, "4 intersections → 2 tris", ha="center", va="center",
        fontsize=11, color="#555", fontweight="bold")
ax.text(8.1, 0.76, "0 or 4-fold sign → skip", ha="center", va="center",
        fontsize=10, color="#888")

# bottom note
ax.text(5, 0.28, "No ambiguous cases  ·  guaranteed closed manifold  ·  area/volume error < 5%",
        ha="center", va="center", fontsize=11, color="#555555")

plt.tight_layout()
plt.savefig("marching_tetrahedra_diagram.png", bbox_inches="tight", facecolor="white")
print("saved marching_tetrahedra_diagram.png")
