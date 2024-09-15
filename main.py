from fpdf import FPDF
import glob
import pathlib

filepaths = glob.glob("Text+Files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filepath = pathlib.Path(filepath)
    filename = filepath.stem.title()

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=18, txt=f"{filename}", align="L", ln=1)


pdf.output("Single-Pdf.pdf")






