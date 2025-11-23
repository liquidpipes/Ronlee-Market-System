// worker_code.js
// Minimal Cloudflare Worker exposing a Fusion+ style JSON endpoint.

import { computeFusionScore } from "./fusion_runtime.js";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const symbol = url.searchParams.get("symbol") || "NVDA";

    // Placeholder inputs; replace with real calculations / data pipelines.
    const cf = 0.72;
    const dsg = 0.10;
    const sd = 0.65;
    const pc = 0.80;

    const result = computeFusionScore({ cf, dsg, sd, pc });

    const body = {
      symbol,
      fusion_score: result.fusion_score,
      decision: result.decision,
      components: result.components,
      generated_at: new Date().toISOString(),
    };

    return new Response(JSON.stringify(body, null, 2), {
      headers: { "Content-Type": "application/json" },
    });
  },
};
