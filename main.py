from reportlab.pdfgen import canvas

pdf = canvas.Canvas('Doc.pdf')

pdf.save()