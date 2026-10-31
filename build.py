import re,sys
import os
up=os.path.join(os.path.dirname(os.path.abspath(__file__)),'src','logos')+os.sep
logo=open(up+'logo-horizontal-fundo-preto.svg',encoding='utf-8').read()
inner=re.search(r'<g id="Camada_2"[^>]*>([\s\S]*)</g>\s*</svg>',logo).group(1)
inner=inner.replace('class="cls-1"','fill="#3dcb7f"').replace('class="cls-2"','fill="#3dcb7f" fill-rule="evenodd"').replace('class="cls-3"','fill="#fff"')
LOGO='<svg viewBox="163 161 1594 463" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gerando Tráfego">'+inner+'</svg>'
sym=open(up+'simbolo-verde.svg',encoding='utf-8').read()
body=re.search(r'</defs>([\s\S]*)</svg>',sym).group(1).replace('class="cls-1"','fill="#3dcb7f"')
SYMBOL='<svg viewBox="137 139 508 508" xmlns="http://www.w3.org/2000/svg">'+body+'</svg>'
items=["Meta Ads","Google Ads","Alavancando seu faturamento","Leads qualificados","Em busca do seu melhor cliente","Remarketing","Funis de venda","Escala com lucro"]
MAR=''.join(f'<span>{t}</span>' for t in items*4)
h=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src','template.html'),encoding='utf-8').read().replace('{{LOGO}}',LOGO).replace('{{SYMBOL}}',SYMBOL).replace('{{MARQUEE}}',MAR)
assert '—' not in h, 'em dash found'
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'index.html'),'w',encoding='utf-8').write(h); print(len(h))
