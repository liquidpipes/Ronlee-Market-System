from __future__ import annotations

"""dynamic_signal_gradient.py

Implements the Dynamic Signal Gradient (DSG) component.

Formula:
    DSG = d(Sharpe_z)/dt × sign(MACD)

We approximate d(Sharpe_z)/dt with a finite difference:
    gradient ≈ Sharpe_z[t] - Sharpe_z[t-1]
"""

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass
class DSGInputs:
    sharpe_z_history: Sequence[float]  # at least 2 values, oldest → newest
    macd_value: float                  # MACD at the latest time step


def compute_dsg(inputs: DSGInputs) -> float:
    """Compute Dynamic Signal Gradient (DSG) for the latest time step."""
    if len(inputs.sharpe_z_history) < 2:
        raise ValueError("Need at least 2 Sharpe_z history points to compute DSG.")

    sharpe_prev = inputs.sharpe_z_history[-2]
    sharpe_curr = inputs.sharpe_z_history[-1]
    gradient = sharpe_curr - sharpe_prev

    if inputs.macd_value > 0:
        macd_sign = 1.0
    elif inputs.macd_value < 0:
        macd_sign = -1.0
    else:
        macd_sign = 0.0

    return gradient * macd_sign


def batch_dsg(histories: Iterable[Sequence[float]], macd_values: Iterable[float]) -> list[float]:
    """Convenience function to compute DSG across multiple series."""
    return [
        compute_dsg(DSGInputs(sharpe_z_history=h, macd_value=m))
        for h, m in zip(histories, macd_values)
    ]
