import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(5, 5.65, "Egg Dropping Problem", ha="center", va="center",
        fontsize=27, fontweight="bold", color="#1a1a2e")
ax.text(5, 5.08, r"$\mathrm{dp}[e][f] = 1 + \min_x \max\left(\mathrm{dp}[e{-}1][x{-}1],\ \mathrm{dp}[e][f{-}x]\right)$",
        ha="center", va="center", fontsize=14, color="#444444")

def box(x, y, w, h, text, fc, tc="white", fs=12.5):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                       linewidth=2, edgecolor="#2d2d44", facecolor=fc)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fs, color=tc, fontweight="bold")

# k eggs, n floors input
box(1.0, 3.95, 3.3, 0.8, "k eggs\nn floors", "#6c63ff")

# drop decision node
box(4.35, 3.95, 2.2, 0.8, "drop at\nfloor x", "#f39c12")

# two branches: break / not break
box(0.4, 2.35, 2.9, 0.85, "egg breaks\n(k-1 eggs, x-1 fl)", "#e74c3c")
box(6.7, 2.35, 3.0, 0.85, "egg survives\n(k eggs, f-x fl)", "#00b894")

# result
box(2.2, 0.7, 5.6, 0.85, "worst case = 1 + max(both branches)", "#2d2d44", fs=14)

# arrows input -> decision
ax.add_patch(FancyArrowPatch((2.65, 3.93), (4.35, 4.35),
             arrowstyle="-|>", mutation_scale=18, color="#999999", linewidth=1.6))
ax.add_patch(FancyArrowPatch((5.45, 3.93), (6.2, 3.2),
             arrowstyle="-|>", mutation_scale=18, color="#999999", linewidth=1.6))
# arrows decision -> branches
ax.add_patch(FancyArrowPatch((5.0, 3.93), (1.8, 3.2),
             arrowstyle="-|>", mutation_scale=18, color="#999999", linewidth=1.6))
ax.add_patch(FancyArrowPatch((5.7, 3.93), (8.2, 3.2),
             arrowstyle="-|>", mutation_scale=18, color="#999999", linewidth=1.6))
# arrows branches -> result
ax.add_patch(FancyArrowPatch((1.8, 2.33), (3.6, 1.57),
             arrowstyle="-|>", mutation_scale=18, color="#999999", linewidth=1.6))
ax.add_patch(FancyArrowPatch((8.2, 2.33), (6.4, 1.57),
             arrowstyle="-|>", mutation_scale=18, color="#999999", linewidth=1.6))

ax.text(5, 1.35, "Monotonic DP: O(nk)  |  Binary-search DP: O(k log n)",
        ha="center", va="center", fontsize=11, color="#555555")

plt.tight_layout()
plt.savefig("egg_dropping_diagram.png", bbox_inches="tight", facecolor="white")
print("saved egg_dropping_diagram.png")
