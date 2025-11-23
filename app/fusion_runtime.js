// fusion_runtime.js
// Client-side Fusion Score logic mirroring fusion_score.py.

export function computeFusionScore(
  components,
  w_cf = 0.40,
  w_dsg = 0.25,
  w_sd = 0.20,
  w_pc = 0.15,
  buy_threshold = 0.65,
  hold_threshold = 0.45,
) {
  const fusion_score =
    w_cf * components.cf +
    w_dsg * components.dsg +
    w_sd * components.sd +
    w_pc * components.pc;

  let decision;
  if (fusion_score >= buy_threshold) {
    decision = "BUY";
  } else if (fusion_score >= hold_threshold) {
    decision = "HOLD";
  } else {
    decision = "SELL";
  }

  return {
    fusion_score,
    decision,
    components,
  };
}
