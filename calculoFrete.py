#!/usr/bin/python

import requests, xmltodict

cep_origem = '02733080'
cep_destino = '06455000'
cep_destino = '02737000'
cod_servico = '04510' # 04014 SEDEX; 04510 PAC;

cx_comprimento = '20' # cm
cx_altura = '20' # cm
cx_largura = '20' # cm
cx_peso = '1' # kg

data = '<?xml version="1.0" encoding="utf-8"?>' \
       '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/">' \
       '  <soap:Header/>' \
       '  <soap:Body>' \
       '    <tem:CalcPrecoPrazo>' \
       '      <tem:nCdEmpresa></tem:nCdEmpresa>' \
       '      <tem:sDsSenha></tem:sDsSenha>' \
       '      <tem:nCdServico>' + cod_servico + '</tem:nCdServico>' \
       '      <tem:sCepOrigem>' + cep_origem + '</tem:sCepOrigem>' \
       '      <tem:sCepDestino>' + cep_destino +'</tem:sCepDestino>' \
       '      <tem:nVlPeso>' + cx_peso + '</tem:nVlPeso>' \
       '      <tem:nCdFormato>1</tem:nCdFormato>' \
       '      <tem:nVlComprimento>' + cx_comprimento + '</tem:nVlComprimento>' \
       '      <tem:nVlAltura>' + cx_altura + '</tem:nVlAltura>' \
       '      <tem:nVlLargura>' + cx_largura + '</tem:nVlLargura>' \
       '      <tem:nVlDiametro>0</tem:nVlDiametro>' \
       '      <tem:sCdMaoPropria>N</tem:sCdMaoPropria>' \
       '      <tem:nVlValorDeclarado>0</tem:nVlValorDeclarado>' \
       '      <tem:sCdAvisoRecebimento>N</tem:sCdAvisoRecebimento>' \
       '    </tem:CalcPrecoPrazo>' \
       '  </soap:Body>' \
       '</soap:Envelope>'
url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx"
headers = { 'Content-Length': len(data),
            'Connection': 'keep-alive',
            'Content-Type': 'application/soap+xml',
            'charset': 'UTF-8',
            'action': 'http://tempuri.org/CalcPrecoPrazo',
            'host': 'ws.correios.com.br' }
r = requests.post(url, data=data, headers=headers)
xml = xmltodict.parse(r.text)

print xml['soap:Envelope']['soap:Body']['CalcPrecoPrazoResponse']['CalcPrecoPrazoResult']['Servicos']['cServico']['Valor']


