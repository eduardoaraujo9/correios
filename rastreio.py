#!/usr/bin/python

import requests, bs4

cod_objeto = 'PY142122833BR'

data = { 'objetos': 'PY142122833BR' }
url = "https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm"
r = requests.post(url, data=data)
output = r.text.encode('utf8')

#print output
html = bs4.BeautifulSoup(output, "html.parser")
rastreio = html.select('table.listEvent.sro')

print rastreio

