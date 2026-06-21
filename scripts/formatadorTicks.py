import numpy as np
from matplotlib.ticker import FuncFormatter

def formatter_oculta_tick_central(eixo):
    def formatar_tick(valor, pos):
        # Ticks gerados para este eixo
        ticks = np.array(eixo.get_majorticklocs())

        # Se a quantidade de ticks visíveis for par, não há tick central
        if len(ticks) % 2 == 0:
            return f"{valor:g}"

        # Tick central
        tick_central = ticks[len(ticks) // 2]

        # Oculta apenas o tick central
        if np.isclose(valor, tick_central):
            return ""

        return f"{valor:g}"

    return FuncFormatter(formatar_tick)