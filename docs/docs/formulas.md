# Formulas — Ronlee Market System v2.5 Fusion+ Framework

## 1. Conviction Factor (CF)
CF = Norm[(Sharpe_z + RS_phi + (psi × Model_Conf))]

## 2. Dynamic Signal Gradient (DSG)
DSG = d(Sharpe_z)/dt × sign(MACD)

## 3. Sentiment Damping (SD)
SD = CF × (1 - 0.25 × Clamp(Sharpe > 1.2 or psi > 0.7))

## 4. Predictive Confidence (PC)
PC = 1 - |Pred_t - Actual_t| / |Pred_t|

## 5. Fusion Score
FusionScore = 0.40CF + 0.25DSG + 0.20SD + 0.15PC
