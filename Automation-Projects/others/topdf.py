#%%
from fpdf import FPDF 
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1)
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)
pdf.set_font(family='Times', size=12)
txt1 = """Texto de exemplo no corpo do arquivo PDF do processo de automação de criação de PDFs com Python na biblioteca fpdf"""
pdf.multi_cell(w=0, h=15, txt=txt1)
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom:')
pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:')
pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)


pdf.output('output.pdf')
