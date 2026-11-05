import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# Title
ax.text(5, 5.6, "Karatsuba Multiplication", ha="center", va="center",
        fontsize=26, fontweight="bold", color="#1a1a2e")
ax.text(5, 5.05, r"$A\times B = Z_2\,10^{2m} + (Z_1 - Z_0 - Z_2)\,10^{m} + Z_0$",
        ha="center", va="center", fontsize=15, color="#444444")

def box(x, y, w, h, text, fc, tc="white", fs=13):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                       linewidth=2, edgecolor="#2d2d44", facecolor=fc)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fs, color=tc, fontweight="bold")

# Top: A and B split
box(1.0, 3.9, 3.4, 0.75, "A = A1 * 10^m + A0", "#6c63ff")
box(5.6, 3.9, 3.4, 0.75, "B = B1 * 10^m + B0", "#6c63ff")

# Three multiplications
box(0.4, 2.3, 2.6, 0.75, "Z0 = A0 * B0", "#00b894")
box(3.7, 2.3, 2.6, 0.75, "Z1 = (A0+A1)(B0+B1)", "#00b894")
box(7.0, 2.3, 2.6, 0.75, "Z2 = A1 * B1", "#00b894")

# Result
box(2.2, 0.7, 5.6, 0.85, "3 multiplications -> O(n^1.585)", "#e17055", fs=14)

# Labels
ax.text(5, 3.45, "2 additions let us drop from 4 to 3 multiplications",
        ha="center", va="center", fontsize=12, color="#555555")

# Arrows top -> multiplications
for xm in (1.7, 5.0, 8.3):
    ax.add_patch(FancyArrowPatch((5, 3.88), (xm, 3.08),
                 arrowstyle="-|>", mutation_scale=18,
                 color="#999999", linewidth=1.6))
# Arrows multiplications -> result
for xm in (1.7, 5.0, 8.3):
    ax.add_patch(FancyArrowPatch((xm, 2.28), (5, 1.57),
                 arrowstyle="-|>", mutation_scale=18,
                 color="#999999", linewidth=1.6))

plt.tight_layout()
plt.savefig("karatsuba_diagram.png", bbox_inches="tight", facecolor="white")
print("saved karatsuba_diagram.png")
