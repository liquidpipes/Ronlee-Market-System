from __future__ import annotations

"""pdf_generator.py

Generates a simple one-page PDF summary of Fusion+ results.

Requires:
    pip install fpdf2
"""

from dataclasses import asdict

from fpdf import FPDF

from src.fusion_score import FusionResult


def create_fusion_pdf(symbol: str, result: FusionResult, filename: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Ronlee Market System v2.5 Fusion+ Report", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.ln(5)
    pdf.cell(0, 8, f"Symbol: {symbol}", ln=True)
    pdf.cell(0, 8, f"Fusion Score: {result.fusion_score:.4f}", ln=True)
    pdf.cell(0, 8, f"Decision: {result.decision.name}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Components:", ln=True)

    pdf.set_font("Arial", "", 12)
    for k, v in asdict(result.components).items():
        pdf.cell(0, 8, f"{k.upper()}: {v:.4f}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "I", 9)
    pdf.multi_cell(
        0,
        5,
        "Generated using the Ronlee Market System v2.5 Fusion+ Framework. "
        "For educational and research use only.",
    )

    pdf.output(filename)
