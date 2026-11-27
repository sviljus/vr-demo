#!/usr/bin/env python3
"""Create a genuinely editable DOCX from the same validated JSON as the PDF."""
import argparse,json
from pathlib import Path
from docx import Document
from docx.image.image import Image as WordImage
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from validate import validate
from closing import CLOSING, normalize_closing
ROOT=Path(__file__).resolve().parents[1]

def link(p,label,url,size=8,color="192B43"):
 rid=p.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
 a=OxmlElement('w:hyperlink');a.set(qn('r:id'),rid);r=OxmlElement('w:r');pr=OxmlElement('w:rPr');c=OxmlElement('w:color');c.set(qn('w:val'),color);pr.append(c);s=OxmlElement('w:sz');s.set(qn('w:val'),str(size*2));pr.append(s);r.append(pr);t=OxmlElement('w:t');t.text=label;r.append(t);a.append(r);p._p.append(a)

def shade(p):
 pr=p._p.get_or_add_pPr();s=OxmlElement('w:shd');s.set(qn('w:fill'),'EFF6F6');pr.append(s);p.paragraph_format.left_indent=Cm(.25);p.paragraph_format.right_indent=Cm(.25);p.paragraph_format.keep_together=True
 return p

def picture(p,relpath,height,alt):
 # validate() already checks repository containment and file existence.
 p.alignment=1;img=WordImage.from_file(str(ROOT/relpath));width=min(5.6,height*img.px_width/img.px_height);height=width*img.px_height/img.px_width;shape=p.add_run().add_picture(str(ROOT/relpath),width=Cm(width),height=Cm(height));shape._inline.docPr.set('descr',alt)

def offer_card(d,b):
 table=d.add_table(rows=1,cols=1);table.autofit=False;table.columns[0].width=Cm(16.5);cell=table.cell(0,0);cell.width=Cm(16.5);table._tbl.tblPr.find(qn('w:tblW')).set(qn('w:w'),'9354')
 pr=cell._tc.get_or_add_tcPr();bg=OxmlElement('w:shd');bg.set(qn('w:fill'),'EFF6F6');pr.append(bg)
 margins=OxmlElement('w:tcMar')
 for side in ['top','left','bottom','right']:
  node=OxmlElement('w:'+side);node.set(qn('w:w'),'340');node.set(qn('w:type'),'dxa');margins.append(node)
 pr.append(margins);borders=OxmlElement('w:tcBorders')
 for side in ['top','left','bottom','right']:
  node=OxmlElement('w:'+side);node.set(qn('w:val'),'single');node.set(qn('w:sz'),'4');node.set(qn('w:color'),'BADADD');borders.append(node)
 pr.append(borders);table.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
 cell.paragraphs[0].paragraph_format.space_after=Pt(0);cell.paragraphs[0].paragraph_format.line_spacing=Pt(1);cell.paragraphs[0].add_run().font.size=Pt(1)
 head=cell.add_table(rows=1,cols=2);head.autofit=False;head.columns[0].width=Cm(10.3);head.columns[1].width=Cm(3.8);head.cell(0,0).width=Cm(10.3);head.cell(0,1).width=Cm(3.8);head._tbl.tblPr.find(qn('w:tblW')).set(qn('w:w'),'7994')
 title=head.cell(0,0).paragraphs[0];title.style='Heading 2';title.paragraph_format.space_before=Pt(0);title.paragraph_format.line_spacing=1.2;r=title.add_run(b['name']);r.font.size=Pt(17)
 price=head.cell(0,1).paragraphs[0];price.alignment=2;price.paragraph_format.space_after=Pt(4);price.paragraph_format.line_spacing=1;r=price.add_run(b['price']);r.font.name='Georgia';r.font.size=Pt(8 if '{{' in b['price'] else 29);r.bold=True
 if b.get('regular_price'):
  regular=head.cell(0,1).add_paragraph();regular.alignment=2;regular.paragraph_format.space_after=Pt(0)
  for text,strike in [('Tavahind  ',False),(b['regular_price'],True)]:
   r=regular.add_run(text);r.font.size=Pt(8);r.font.color.rgb=RGBColor.from_string('647080');r.font.strike=strike
 desc=cell.add_paragraph(b['description'],'Normal');desc.paragraph_format.space_before=Pt(4);desc.paragraph_format.space_after=Pt(9)
 if b.get('images'):
  photos=cell.add_table(rows=1,cols=len(b['images'])+1);photos.autofit=False;photos._tbl.tblPr.find(qn('w:tblW')).set(qn('w:w'),'7994')
  for col in photos.columns:col.width=Cm(3.1)
  photos.columns[-1].width=Cm(7.9)
  for c,item in zip(photos.rows[0].cells,b['images']):c.width=Cm(3.1);picture(c.paragraphs[0],item['image'],3.6,item['alt'])
  c=photos.rows[0].cells[-1];c.width=Cm(7.9);caption=c.paragraphs[0];caption.style='Eyebrow';caption.paragraph_format.space_before=Pt(12);caption.add_run(b['caption'])
 if b.get('image_placeholder'):cell.add_paragraph(b['image_placeholder'],'Card')
 ctat=cell.add_table(rows=1,cols=1);ctat.autofit=False;ctat.columns[0].width=Cm(7);ctat._tbl.tblPr.find(qn('w:tblW')).set(qn('w:w'),'3969');cc=ctat.cell(0,0);cc.width=Cm(7)
 cpr=cc._tc.get_or_add_tcPr();fill=OxmlElement('w:shd');fill.set(qn('w:fill'),'192B43');cpr.append(fill);pad=OxmlElement('w:tcMar')
 for side in ['top','left','bottom','right']:
  node=OxmlElement('w:'+side);node.set(qn('w:w'),'120');node.set(qn('w:type'),'dxa');pad.append(node)
 cpr.append(pad);cta=cc.paragraphs[0];cta.paragraph_format.space_before=Pt(0);cta.paragraph_format.space_after=Pt(0);cta.paragraph_format.line_spacing=1.2;link(cta,b['cta'],b['url'],9,'FFFFFF')
 gap=d.add_paragraph();gap.paragraph_format.space_after=Pt(9);gap.paragraph_format.line_spacing=Pt(1);gap.add_run().font.size=Pt(1)

def build(data,out):
 data=normalize_closing(data)
 errors=validate(data)
 if errors:raise ValueError('; '.join(errors))
 d=Document(ROOT/'templates/reading.docx')
 for child in list(d.element.body):
  if child.tag!=qn('w:sectPr'):d.element.body.remove(child)
 for sec in d.sections:
  for hdr in [sec.header,sec.first_page_header]:
   for p in hdr.paragraphs:
    for r in p.runs:
     if '{{NUMBER}}' in r.text:r.text=r.text.replace('{{NUMBER}}',data['number'])
 def p(text,style='Normal'):return d.add_paragraph(text,style)
 z=p(data['tagline'],'Eyebrow');z.alignment=1;z.paragraph_format.space_before=Pt(58)
 z=p(data['number'],'Number');z.alignment=1;z.paragraph_format.line_spacing=.95;z.paragraph_format.space_after=Pt(0)
 for text,style in [('Sinu Punkt A energia','Title'),(data['number']+' · '+data['energy_name'],'Heading 2'),(' · '.join(data['keywords']),'Subtitle'),(data['opening_quote'],'Quote')]:p(text,style).alignment=1
 styles={'text':'Normal','heading':'Heading 1','subheading':'Heading 2','label':'Eyebrow','quote':'Quote','card':'Card'}
 for pi,group in enumerate(data['pages']):
  if pi:d.add_page_break()
  for b in group:
   role=b['role']
   if role in styles:
    z=p(b['text'],styles[role])
    if role in ['quote','card']:shade(z)
    if role=='heading' and any(x['role']=='offer' for x in group):
     for run in z.runs:run.font.size=Pt(27);run.bold=False
     z.paragraph_format.line_spacing=1.12
   elif role=='offer':offer_card(d,b)
   elif role=='link':link(shade(p('','Card')),b['text'],b['url'],10)
   elif role=='gallery':
    table=d.add_table(rows=1,cols=len(b['items']));table.autofit=False
    for cell,item in zip(table.rows[0].cells,b['items']):picture(cell.paragraphs[0],item['image'],5.6,item['alt'])
    table.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
   elif role=='crystals':
    table=d.add_table(rows=1,cols=len(b['items']));table.autofit=False
    for cell,item in zip(table.rows[0].cells,b['items']):
     cell.width=Cm(16.9/len(b['items']));pr=cell._tc.get_or_add_tcPr();bg=OxmlElement('w:shd');bg.set(qn('w:fill'),'FAF8F3');pr.append(bg)
     picture(cell.paragraphs[0],item['image'],3.2,item['image_alt'])
     for text,style in [(item['name'],'Heading 2'),(item['description'],'Card'),('Seos energiaga: '+item['connection'],'Card'),(item['reminder'],'Quote')]:cell.add_paragraph(text,style)
     credit=cell.add_paragraph('','Eyebrow');link(credit,item['credit_text'],item['credit_url']);credit.add_run(' · ');link(credit,'litsents',item['license_url'])
    table.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
 z=p(CLOSING,'Quote');z.alignment=1;z.paragraph_format.space_before=Pt(18);z.paragraph_format.space_after=Pt(0);z.paragraph_format.line_spacing=1.5;z.paragraph_format.keep_together=True
 pr=z._p.get_or_add_pPr();borders=OxmlElement('w:pBdr');border=OxmlElement('w:top');border.set(qn('w:val'),'single');border.set(qn('w:sz'),'4');border.set(qn('w:color'),'57A7B3');border.set(qn('w:space'),'10');borders.append(border);pr.append(borders)
 d.core_properties.title='Sinu Punkt A energia · '+data['number'];d.core_properties.author='Vaimuraamat'
 out.parent.mkdir(parents=True,exist_ok=True);d.save(out)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('data',type=Path);ap.add_argument('--out',type=Path,default=ROOT/'build/lugemine.docx');a=ap.parse_args();build(json.loads(a.data.read_text(encoding='utf-8')),a.out);print(a.out)
