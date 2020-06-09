from reportlab.pdfgen import canvas

pdf = canvas.Canvas('Doc.pdf')
pdf.setTitle('Document')
pdf.drawString(0,0,'Text')
pdf.drawCentredString(290,720,"Document Title")


pdf.save()