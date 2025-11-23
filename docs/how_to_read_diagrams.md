# How to Read the Fusion+ Diagrams

This guide explains how to interpret the diagrams used throughout the Ronlee Market System v2.5 Fusion+ documentation.

---

## 1. Boxes Represent Functional Modules
Each box in a diagram corresponds to a logical component of the system:
- Base Engine (trend structure)
- Overlay (risk filtering)
- Fusion+ Core (CF, DSG, SD, PC)
- CSI Sentiment Engine
- Validation Layer

---

## 2. Arrows Show Flow of Information
Arrows indicate how data transforms and moves:
- Left → Right = raw data becomes processed signals
- Top → Bottom = hierarchical reasoning
- Converging arrows = weighted fusion

---

## 3. Layer Order Matters
Fusion+ diagrams follow a strict hierarchy:
1. Base Engine
2. Overlay (Sharpe & risk)
3. Fusion+ Core
4. CSI v2 Sentiment Engine
5. Final Decision Layer

---

## 4. Inputs vs Outputs
Inputs are placed on the left or top:
- Price, volume, sentiment, volatility

Outputs are placed on the right or bottom:
- Fusion Score
- BUY / HOLD / SELL decisions

---

## 5. Parallel Blocks = Independent Calculations
Sections such as CF, DSG, SD, and PC run independently before merging.

---

## 6. Merging Blocks = Fusion
Where lines combine, the system performs weighted blending:
- 40% CF
- 25% DSG
- 20% SD
- 15% PC

---

## 7. Behavioral Components Are Explicit
Sentiment and psychological factors appear in:
- CSI Sentiment Engine
- Sentiment Damping

---

## 8. Decision Layer Is the Final Output
All diagrams terminate with actionable intelligence:
- BUY
- HOLD
- SELL

---

This document helps interpret how each visual component contributes to the overall Fusion+ decision-making process.
