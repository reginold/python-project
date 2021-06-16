import webbrowser
from fpdf import FPDF
import os

class PdfReport:
	"""P46
	
	"""
	def __init__(self, filename) -> None:
		self.filename = filename
	
	def generate(self, flatmate1, flatmate2, bill):
		# pdf = FPDF(format='letter', unit='in')
		pdf = FPDF(orientation='P', unit='pt', format='A4')
		pdf.add_page()

		# Add some text
		pdf.set_font(family='Times', size=24, style='B')
		pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="c", ln=1)
		pdf.cell(w=100, h=40, txt='Period', border=0)
		pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

		pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
		pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=1, ln=1)


		pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
		pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=1, ln=1)

		os.chdir("files")
		pdf.output(self.filename)
		webbrowser.open(self.filename)