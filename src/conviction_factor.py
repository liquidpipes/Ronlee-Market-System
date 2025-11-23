from __future__ import annotations

"""conviction_factor.py

Implements the Conviction Factor (CF) component of the
Ronlee Market System v2.5 Fusion+ Framework.

Formula:
    CF = Norm[(Sharpe_z + RS_phi + (psi × Model_Conf))]

Where:
    - Sharpe_z:       z-scored Sharpe ratio (risk-adjusted performance)
    - RS_phi:         relative strength term (e.g., sector / benchmark)
    - psi:            sentiment intensity (0–1)
    - Model_Conf:     internal model confidence (0–1)
    - Norm[·]:        normalization to a bounded [0, 1] scale
"""

from dataclasses import dataclass
from typing import Iterable
import math


@dataclass
class ConvictionInputs:
    sharpe_z: float
    rs_phi: float
    psi: float
    model_conf: float


def _logistic_normalize(x: float) -> float:
    """Smoothly squashes any real-valued score into (0, 1)."""
    return 1.0 / (1.0 + math.exp(-x))


def compute_conviction_factor(inputs: ConvictionInputs, scale: float = 1.0) -> float:
    """Compute Conviction Factor (CF)."""
    raw_score = inputs.sharpe_z + inputs.rs_phi + inputs.psi * inputs.model_conf
    return _logistic_normalize(raw_score * scale)


def batch_conviction_factor(data: Iterable[ConvictionInputs], scale: float = 1.0) -> list[float]:
    """Vector-style helper to compute CF over a list of ConvictionInputs."""
    return [compute_conviction_factor(d, scale=scale) for d in data]
