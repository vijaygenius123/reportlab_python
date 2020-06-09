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