import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Circle

fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(5, 5.65, "Möller-Trumbore Ray-Triangle Intersection", ha="center", va="center",
        fontsize=24, fontweight="bold", color="#1a1a2e")
ax.text(5, 5.08,
        r"$t = \frac{\mathbf{e_2}\cdot\mathbf{q}}{\mathbf{e_1}\cdot\mathbf{p}}$"
        r"$\quad$"
        r"$u = \frac{\mathbf{t}\cdot\mathbf{p}}{\mathbf{e_1}\cdot\mathbf{p}}$"
        r"$\quad$"
        r"$v = \frac{\mathbf{d}\cdot\mathbf{q}}{\mathbf{e_1}\cdot\mathbf{p}}$",
        ha="center", va="center", fontsize=12.5, color="#444444")

# --- draw a triangle with vertices ---
# triangle window (in data coords)
v0 = (2.2, 4.1)
v1 = (7.8, 3.4)
v2 = (4.6, 1.1)

tri = Polygon([v0, v1, v2], closed=True, facecolor="#d6e4ff",
              edgecolor="#2d2d44", linewidth=2.5)
ax.add_patch(tri)

# vertex labels
ax.text(v0[0]-0.28, v0[1]+0.2, r"$V_0$", fontsize=16, fontweight="bold", color="#1a1a2e")
ax.text(v1[0]+0.12, v1[1]+0.1, r"$V_1$", fontsize=16, fontweight="bold", color="#1a1a2e")
ax.text(v2[0]+0.1, v2[1]-0.32, r"$V_2$", fontsize=16, fontweight="bold", color="#1a1a2e")

# hit point P inside triangle (barycentric)
P = (4.5, 2.85)
ax.add_patch(Circle(P, 0.06, facecolor="#e74c3c", edgecolor="#7a1f1a", linewidth=1.5, zorder=5))
ax.text(P[0]+0.15, P[1]+0.15, r"$P$", fontsize=15, fontweight="bold", color="#c0392b")

# ray origin O and direction -> P
O = (1.4, 0.7)
ax.add_patch(Circle(O, 0.06, facecolor="#2c3e50", edgecolor="#1a252f", linewidth=1.5, zorder=5))
ax.text(O[0]-0.18, O[1]+0.2, r"$O$", fontsize=15, fontweight="bold", color="#2c3e50")

# ray line O -> P with arrowhead
ax.add_patch(FancyArrowPatch(O, P, arrowstyle="-|>", mutation_scale=22,
             color="#e67e22", linewidth=2.4, zorder=4))
ax.text(2.7, 1.35, r"ray: $O + t\,\mathbf{d}$", fontsize=13, color="#d35400")

# --- formula box ---
from matplotlib.patches import FancyBboxPatch
box = FancyBboxPatch((6.0, 0.55), 3.7, 1.5, boxstyle="round,pad=0.12",
                     linewidth=1.8, edgecolor="#2d2d44", facecolor="#fdf6e3")
ax.add_patch(box)
ax.text(7.85, 1.78, "Hit iff", ha="center", va="center", fontsize=12, color="#555", fontweight="bold")
ax.text(7.85, 1.32, r"$u \geq 0,\ v \geq 0,\ u+v \leq 1$",
        ha="center", va="center", fontsize=12.5, color="#1a1a2e")
ax.text(7.85, 0.82, r"$P = V_0 + u\,\mathbf{e_1} + v\,\mathbf{e_2}$",
        ha="center", va="center", fontsize=10, color="#1a1a2e")

# bottom note
ax.text(5, 0.28, "No plane precompute  ·  single-pass barycentric solve  ·  optional backface culling",
        ha="center", va="center", fontsize=11, color="#555555")

plt.tight_layout()
plt.savefig("moller_trumbore_diagram.png", bbox_inches="tight", facecolor="white")
print("saved moller_trumbore_diagram.png")
