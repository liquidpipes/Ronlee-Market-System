from __future__ import annotations

"""sentiment_damping.py

Implements the Sentiment Damping (SD) component.

Formula:
    SD = CF × (1 - 0.25 × Clamp(Sharpe > 1.2 or psi > 0.7))

When Sharpe is very high or sentiment psi is strong, we dampen the
signal by a fixed penalty factor.
"""

from dataclasses import dataclass


@dataclass
class SentimentDampingInputs:
    cf: float
    sharpe: float
    psi: float


def compute_sentiment_damping(
    inputs: SentimentDampingInputs,
    sharpe_threshold: float = 1.2,
    psi_threshold: float = 0.7,
    penalty: float = 0.25,
) -> float:
    """Compute Sentiment Damping (SD)."""
    hot = (inputs.sharpe > sharpe_threshold) or (inputs.psi > psi_threshold)
    clamp_value = 1.0 if hot else 0.0
    factor = 1.0 - penalty * clamp_value
    return inputs.cf * factor
