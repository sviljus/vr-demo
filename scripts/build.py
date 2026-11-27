#!/usr/bin/env python3
"""UTF-8 JSON -> escaped, self-contained Vaimuraamat HTML. Python 3 stdlib only."""
from pathlib import Path
import argparse,json,html,base64,mimetypes
ROOT=Path(__file__).resolve().parents[1]
from validate import validate
from closing import CLOSING, normalize_closing

def render(data,root):
 data=normalize_closing(data)
 errors=validate(data)
 if errors:raise ValueError("; ".join(errors))
 def esc(x):
  if not isinstance(x,str):raise ValueError('Tekstivälja väärtus peab olema string.')
  if '{{' in x or '}}' in x:raise ValueError('Täitmata asendusväli.')
  return html.escape(x,quote=True)
 def image(path):
  f=(root/path).resolve()
  if root.resolve() not in f.parents:raise ValueError('Pilt peab asuma mallipaketis.')
  mime=mimetypes.guess_type(f.name)[0]
  if mime not in ['image/png','image/jpeg','image/svg+xml']:raise ValueError('Lubatud on PNG, JPEG ja SVG.')
  return 'data:'+mime+';base64,'+base64.b64encode(f.read_bytes()).decode()
 def block(b):
  role=b['role']
  if role in ['text','heading','subheading','label','quote','card']:
   tag={'heading':'h2','subheading':'h3'}.get(role,'p');return '<'+tag+' class="'+role+'">'+esc(b['text'])+'</'+tag+'>'
  if role=='link':
   if not b['url'].startswith('https://'):raise ValueError('Link peab kasutama HTTPS-i.')
   return '<p class="link"><a href="'+esc(b['url'])+'">'+esc(b['text'])+'</a></p>'
  if role=='gallery':return '<div class="gallery">'+''.join('<img src="'+image(i['image'])+'" alt="'+esc(i['alt'])+'">' for i in b['items'])+'</div>'
  if role=='crystals':
   cards=[]
   for i in b['items']:
    cards.append('<article class="crystal"><img src="'+image(i['image'])+'" alt="'+esc(i.get('image_alt',i['name']))+'"><h3>'+esc(i['name'])+'</h3><p>'+esc(i['description'])+'</p><p>Seos energiaga: '+esc(i['connection'])+'</p><p class="quote">'+esc(i['reminder'])+'</p><p class="photo-credit"><a href="'+esc(i['credit_url'])+'">'+esc(i['credit_text'])+'</a> · <a href="'+esc(i['license_url'])+'">litsents</a></p></article>')
   return '<div class="crystals">'+''.join(cards)+'</div>'
  raise ValueError('Tundmatu plokitüüp: '+role)
 assert data['schema_version']==1,'Vale skeemiversioon'
 for k in ['number','energy_name','tagline','opening_quote']:esc(data[k])
 if len(data['keywords'])!=3:raise ValueError('Vaja on kolme märksõna.')
 pages=[]
 for n,page in enumerate(data['pages']):
  start=''
  if n==0:start='<div class="masthead"><img src="'+image('assets/logo.svg')+'" alt="Vaimuraamat"></div><div class="identity"><p class="tagline">'+esc(data['tagline'])+'</p><p class="number">'+esc(data['number'])+'</p><h1 class="title">Sinu Punkt A energia</h1><p class="energy">'+esc(data['number'])+' · '+esc(data['energy_name'])+'</p><p class="keywords">'+esc(' · '.join(data['keywords']))+'</p><p class="opening">'+esc(data['opening_quote'])+'</p></div>'
  end='<p class="closing-note">'+esc(CLOSING)+'</p>' if n==len(data['pages'])-1 else ''
  pages.append('<section class="page" style="--page-index:'+str(n)+';--page-count:'+str(len(data['pages']))+'">'+start+''.join(block(b) for b in page)+end+'</section>')
 template=(root/'templates/reading.html').read_text(encoding='utf-8')
 return template.replace('{{TITLE}}',esc('Vaimuraamat · Punkt A · '+data['number'])).replace('{{NUMBER}}',esc(data['number'])).replace('{{BODY}}',''.join(pages))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('data',type=Path);ap.add_argument('--out',type=Path,default=ROOT/'build/lugemine.html');args=ap.parse_args()
 data=json.loads(args.data.read_text(encoding='utf-8'));args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(render(data,ROOT),encoding='utf-8');print(args.out)
