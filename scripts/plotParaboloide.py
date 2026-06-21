import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from formatadorTicks import formatter_oculta_tick_central

x = np.linspace(-22, 22, 300)
y = np.linspace(-22, 22, 300)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

fig = plt.figure(figsize=(8, 6))

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
ax.set_box_aspect((1, 1, 1))

ax.view_init(elev=15, azim=60)

ax.tick_params(axis="x", labelsize=8, pad=-5)
ax.tick_params(axis="y", labelsize=8, pad=-5)
ax.tick_params(axis="z", labelsize=8, pad=0)
ax.set_xlabel(r"$x$", fontsize=11, labelpad=-16)
ax.set_ylabel(r"$y$", fontsize=11, labelpad=-16)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_major_formatter(formatter_oculta_tick_central(ax.xaxis))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_formatter(formatter_oculta_tick_central(ax.yaxis))
ax.zaxis.set_major_locator(MultipleLocator(200))

from pathlib import Path

# Pasta onde está este script .py
script_dir = Path(__file__).resolve().parent

# Caminho relativo à pasta do script
saida = script_dir / "../mainmatter/introducao/funcoesRn/paraboloide.jpg"
saida = saida.resolve()

# Cria a pasta, se ela não existir
saida.parent.mkdir(parents=True, exist_ok=True)

fig.savefig(
    saida,
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.05,
    pil_kwargs={"optimize": True, "quality": 95}
)