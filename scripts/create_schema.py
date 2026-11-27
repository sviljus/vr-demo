"""Maintainer helper: regenerate the documented JSON Schema (not needed to build)."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
text={'type':'string','minLength':1};url={'type':'string','pattern':'^https://'}
def obj(props,required=None):return {'type':'object','properties':props,'required':required or list(props),'additionalProperties':False}
def block(role,props):return obj({'role':{'const':role},**props})
crystal=obj({k:text for k in ['name','image','image_alt','description','connection','reminder','credit_text']}|{'credit_url':url,'license_url':url})
variants=[block(r,{'text':text}) for r in ['text','heading','subheading','label','quote','card']]
variants += [block('link',{'text':text,'url':url}),block('crystals',{'items':{'type':'array','minItems':1,'items':crystal}}),block('gallery',{'items':{'type':'array','minItems':1,'items':obj({'image':text,'alt':text})}})]
offer=obj({'role':{'const':'offer'},'name':text,'price':text,'regular_price':text,'description':text,'cta':text,'url':url,'images':{'type':'array','minItems':1,'maxItems':2,'items':obj({'image':text,'alt':text})},'caption':text},['role','name','price','description','cta','url'])
offer['dependentRequired']={'images':['caption']}
variants.append(offer)
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'https://raw.githubusercontent.com/sviljus/vr-demo/main/data/reading.schema.json','title':'Vaimuraamat production reading',**obj({'schema_version':{'const':1},'number':{'type':'string','pattern':'^[1-9][0-9]*$'},'energy_name':text,'keywords':{'type':'array','minItems':3,'maxItems':3,'items':text},'tagline':text,'opening_quote':text,'pages':{'type':'array','minItems':1,'items':{'type':'array','minItems':1,'items':{'oneOf':variants}}}})}
(root/'data/reading.schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
