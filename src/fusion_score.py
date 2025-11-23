from __future__ import annotations

"""fusion_score.py

Implements the overall Fusion Score for the Ronlee Market System v2.5.

Formula:
    Fusion_Score = 0.40 × CF + 0.25 × DSG + 0.20 × SD + 0.15 × PC

Decision thresholds:
    BUY  >= 0.65
    HOLD 0.45 – 0.65
    SELL < 0.45
"""

from dataclasses import dataclass
from enum import Enum, auto


class Decision(Enum):
    BUY = auto()
    HOLD = auto()
    SELL = auto()


@dataclass
class FusionComponents:
    cf: float   # Conviction Factor
    dsg: float  # Dynamic Signal Gradient
    sd: float   # Sentiment Damping
    pc: float   # Predictive Confidence


@dataclass
class FusionResult:
    fusion_score: float
    decision: Decision
    components: FusionComponents


def compute_fusion_score(
    components: FusionComponents,
    w_cf: float = 0.40,
    w_dsg: float = 0.25,
    w_sd: float = 0.20,
    w_pc: float = 0.15,
    buy_threshold: float = 0.65,
    hold_threshold: float = 0.45,
) -> FusionResult:
    """Compute the Fusion Score and discrete decision."""
    fusion_score = (
        w_cf * components.cf
        + w_dsg * components.dsg
        + w_sd * components.sd
        + w_pc * components.pc
    )

    if fusion_score >= buy_threshold:
        decision = Decision.BUY
    elif fusion_score >= hold_threshold:
        decision = Decision.HOLD
    else:
        decision = Decision.SELL

    return FusionResult(fusion_score=fusion_score, decision=decision, components=components)
