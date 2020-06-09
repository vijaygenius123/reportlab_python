# Generating PDF With Python

## Install Deps

```bash
pip install -r requirements.txt
```
## Create Document

```python
from reportlab.pdfgen import canvas

pdf = canvas.Canvas('Doc.pdf')

pdf.save()
```

## Adding Title & Text


```python

pdf.setTitle('Document')
pdf.drawString(0,0,'Text')
pdf.drawCentredString(290,720,"Document Title")
```