from fpdf import FPDF
import glob
import pathlib

filepaths = glob.glob("Text+Files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    filepath = pathlib.Path(filepath)
    filename = filepath.stem
    name = filename.title()

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=18, txt=f"{name}", align="L", ln=1)

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("Single-Pdf.pdf")






