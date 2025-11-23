from __future__ import annotations

"""predictive_confidence.py

Implements the Predictive Confidence (PC) component.

Formula:
    PC = 1 - |Pred_t - Actual_t| / |Pred_t|
"""

from typing import Iterable


def compute_predictive_confidence(prediction: float, actual: float, epsilon: float = 1e-8) -> float:
    """Compute Predictive Confidence (PC) for a single prediction."""
    denom = abs(prediction) + epsilon
    error_ratio = abs(prediction - actual) / denom
    pc = 1.0 - error_ratio
    return pc


def mean_predictive_confidence(predictions: Iterable[float], actuals: Iterable[float], epsilon: float = 1e-8) -> float:
    """Compute the mean PC over a series of predictions and actuals."""
    pcs = [compute_predictive_confidence(p, a, epsilon=epsilon) for p, a in zip(predictions, actuals)]
    if not pcs:
        raise ValueError("No predictions provided.")
    return sum(pcs) / len(pcs)
