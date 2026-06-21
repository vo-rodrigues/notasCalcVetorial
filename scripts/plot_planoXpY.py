import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


x = np.linspace(-20, 20, 300)
y = np.linspace(-20, 20, 300)
X, Y = np.meshgrid(x, y)

Z = X + Y

fig = plt.figure(figsize=(8, 4))

ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(
    X, Y, Z,
    cmap="viridis",
    edgecolor="none",
    alpha=0.9,
    linewidth=0,
    rcount=300,
    ccount=300
)
# Ajusta a proporção visual dos eixos
ax.set_box_aspect((1, 1, .9))

fig.colorbar(surf, ax=ax, shrink=0.6, pad=0.1)

ax.view_init(elev=25, azim=-45)

ax.set_xlabel(r"$x$", fontsize=12, labelpad=0)
ax.set_ylabel(r"$y$", fontsize=12, labelpad=0)
ax.set_zlabel(r"$z$", fontsize=12, labelpad=0)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.zaxis.set_major_locator(MultipleLocator(10))

from pathlib import Path

# Pasta onde está este script .py
script_dir = Path(__file__).resolve().parent

# Caminho relativo à pasta do script
saida = script_dir / "../mainmatter/introducao/funcoesRn/planoXpY.png"
saida = saida.resolve()

# Cria a pasta, se ela não existir
saida.parent.mkdir(parents=True, exist_ok=True)

fig.savefig(
    saida,
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.05,
    pil_kwargs={"optimize": True, "compress_level": 9}
)