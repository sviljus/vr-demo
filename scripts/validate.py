#!/usr/bin/env python3
"""Validate production reading JSON using the Python standard library."""
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate(d):
 errors=[]
 def require(test,msg):
  if not test:errors.append(msg)
 def txt(v,label):require(isinstance(v,str) and bool(v.strip()) and '{{' not in v and '}}' not in v,label+' must be nonempty text without placeholders')
 def url(v,label):require(isinstance(v,str) and v.startswith('https://'),label+' must be an HTTPS URL')
 def img(v,label):
  if not isinstance(v,str):errors.append(label+' must be a path');return
  p=(ROOT/v).resolve();require(ROOT in p.parents and p.is_file(),label+' must be an existing repository-local file')
 require(d.get('schema_version')==1,'schema_version must equal 1')
 for k in ['number','energy_name','tagline','opening_quote']:txt(d.get(k),k)
 require(isinstance(d.get('number'),str) and bool(re.fullmatch(r'[1-9][0-9]*',d.get('number',''))),'number must be a positive integer string')
 kw=d.get('keywords');require(isinstance(kw,list) and len(kw)==3,'keywords must contain 3 strings')
 if isinstance(kw,list):
  for i,k in enumerate(kw):txt(k,f'keywords[{i}]')
 pages=d.get('pages');require(isinstance(pages,list) and len(pages)>0,'pages must be a nonempty list')
 for pi,page in enumerate(pages if isinstance(pages,list) else []):
  require(isinstance(page,list) and len(page)>0,f'pages[{pi}] must be a nonempty list')
  if not isinstance(page,list):continue
  for bi,b in enumerate(page):
   loc=f'pages[{pi}][{bi}]'
   if not isinstance(b,dict):errors.append(loc+' must be an object');continue
   role=b.get('role')
   if role in ['text','heading','subheading','label','quote','card','link']:
    txt(b.get('text'),loc+'.text')
    if role=='link':url(b.get('url'),loc+'.url')
   elif role in ['crystals','gallery']:
    items=b.get('items');require(isinstance(items,list) and len(items)>0,loc+'.items must not be empty')
    for ii,item in enumerate(items if isinstance(items,list) else []):
     if not isinstance(item,dict):errors.append(loc+'.items must contain objects');continue
     img(item.get('image'),loc+f'.items[{ii}].image')
     if role=='crystals':
      for k in ['name','image_alt','description','connection','reminder','credit_text']:txt(item.get(k),loc+'.'+k)
      for k in ['credit_url','license_url']:url(item.get(k),loc+'.'+k)
     else:txt(item.get('alt'),loc+'.alt')
   else:errors.append(loc+' has an unknown role')
 return errors
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('data',type=Path);args=ap.parse_args()
 try:
  d=json.loads(args.data.read_text(encoding='utf-8'));errors=validate(d)
 except (OSError,ValueError,TypeError) as e:errors=[str(e)]
 if errors:
  for e in errors:print(e,file=sys.stderr)
  raise SystemExit(1)
 print('Valid production reading JSON:',args.data)
