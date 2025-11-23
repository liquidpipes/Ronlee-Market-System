from __future__ import annotations

"""dashboard_app.py

Simple Streamlit dashboard for the Ronlee Market System v2.5 Fusion+.
Run with:  streamlit run dashboard_app.py
"""

from dataclasses import asdict

import requests
import streamlit as st

from src.fusion_score import FusionComponents, compute_fusion_score

FUSION_ENDPOINT = "https://your-worker-domain.workers.dev"


def fetch_fusion_from_api(symbol: str):
    params = {"symbol": symbol}
    resp = requests.get(FUSION_ENDPOINT, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def main():
    st.set_page_config(page_title="Ronlee Market System v2.5 Fusion+", layout="wide")
    st.title("Ronlee Market System v2.5 – Fusion+ Dashboard")

    symbol = st.text_input("Symbol", value="NVDA").upper().strip()
    use_local = st.checkbox("Use local sample values instead of API", value=True)

    if st.button("Run Analysis"):
        with st.spinner("Computing Fusion+..."):
            if use_local:
                components = FusionComponents(cf=0.72, dsg=0.10, sd=0.65, pc=0.80)
                result = compute_fusion_score(components)
                data = {
                    "symbol": symbol,
                    "fusion_score": result.fusion_score,
                    "decision": result.decision.name,
                    "components": asdict(result.components),
                }
            else:
                data = fetch_fusion_from_api(symbol)

        st.subheader(f"Result for {symbol}")
        st.metric("Fusion Score", f"{data['fusion_score']:.3f}")
        st.write(f"Decision: **{data['decision']}**")
        st.json(data["components"])

        st.caption(
            "Fusion+ decision engine combining Conviction Factor (CF), "
            "Dynamic Signal Gradient (DSG), Sentiment Damping (SD), "
            "and Predictive Confidence (PC)."
        )

    st.sidebar.header("About")
    st.sidebar.markdown(
        """This dashboard demonstrates the Ronlee Market System v2.5 Fusion+ framework."""
    )


if __name__ == "__main__":
    main()
