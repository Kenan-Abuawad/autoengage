from langchain_core.tools import tool
from fpdf import FPDF
import os

LEADS = []


@tool
def create_lead_magnet_outline(
    topic: str,
    target_audience: str
) -> str:
    """
    Create a lead magnet outline.
    """

    result = f"Title: {topic}\n\n"

    for i in range(1, 6):
        result += (
            f"Chapter {i}: {topic} Part {i}\n"
            f"Summary for chapter {i}\n\n"
        )

    return result


@tool
def generate_lead_magnet_pdf(
    title: str,
    chapters: list,
    filename: str
) -> str:
    """
    Generate a PDF lead magnet.
    """

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, "Table of Contents", ln=True)

    for i, chapter in enumerate(chapters):
        pdf.cell(
            0,
            10,
            f"{i+1}. {chapter['title']}",
            ln=True
        )

    pdf.add_page()

    for chapter in chapters:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(
            0,
            10,
            chapter["title"],
            ln=True
        )

        pdf.set_font("Arial", "", 12)

        pdf.multi_cell(
            0,
            10,
            chapter["content"]
        )

        pdf.ln(5)

    pdf.output(filename)

    return os.path.abspath(filename)


@tool
def write_cta_for_lead_magnet(
    magnet_title: str,
    platform: str
) -> str:
    """
    Create CTA versions.
    """

    return (
        f"1. Download the {magnet_title} guide\n"
        f"2. Get your free copy of {magnet_title}\n"
        f"3. Learn more with {magnet_title}"
    )


@tool
def capture_lead(
    username: str,
    platform: str,
    interest: str
) -> str:
    """
    Save lead information.
    """

    lead = {
        "username": username,
        "platform": platform,
        "interest": interest
    }

    LEADS.append(lead)

    return f"Lead saved: {username}"