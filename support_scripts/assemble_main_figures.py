
from PIL import Image
import copy, math, os, subprocess
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from svglib.svglib import svg2rlg

def load_panel(path):
    ext=os.path.splitext(path)[1].lower()
    if ext=='.svg':
        d=svg2rlg(path)
        return ('svg', d.width, d.height, d)
    elif ext in ['.png','.jpg','.jpeg']:
        im=Image.open(path)
        return ('img', im.size[0], im.size[1], path)
    raise ValueError(path)

def draw_panel(c, panel, x, y, target_w, target_h):
    kind,w,h,obj=panel
    scale=min(target_w/w, target_h/h)
    draw_w, draw_h = w*scale, h*scale
    dx = x + (target_w-draw_w)/2
    dy = y + (target_h-draw_h)/2
    if kind=='svg':
        d=copy.deepcopy(obj)
        d.scale(scale, scale)
        renderPDF.draw(d, c, dx, dy)
    else:
        c.drawImage(ImageReader(obj), dx, dy, width=draw_w, height=draw_h, mask='auto')
    return dx,dy,draw_w,draw_h

def render_pdf_to_png(pdf_path, png_path, dpi=300):
    out_base=os.path.splitext(png_path)[0]
    subprocess.run(['pdftoppm','-singlefile','-png','-r',str(dpi),pdf_path,out_base], check=True)

def compose_grid(out_pdf, placements, page_w, page_h):
    c=canvas.Canvas(out_pdf, pagesize=(page_w,page_h))
    c.setFillColor(colors.white); c.rect(0,0,page_w,page_h,fill=1,stroke=0)
    c.setFillColor(colors.black); c.setFont('Helvetica-Bold', 14)
    for p in placements:
        dx,dy,dw,dh = draw_panel(c,p['panel'],p['x'],p['y'],p['w'],p['h'])
        c.drawString(dx-8, dy+dh+8, p['label'])
    c.showPage(); c.save()

# This script is an archival reference for the final composite layouts used in the submission package.
# Paths should be adjusted if you rerun it outside the packaged directory.
