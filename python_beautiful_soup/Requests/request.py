import requests

''' 038 Introdução ao módulo requests '''

url = 'https://www.youtube.com/results?'
payload = {'search_query' : 'como fazer estrogonofe de frango'}
r = requests.get(url, params= payload)

print(r.text)
print(r.url)
print(r.encoding)

with open('youtube.html', 'w') as f:
    f.write(r.text)

''' 039 Utilizando o método POST '''

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'

payload = {
            'relaxation':'85505150',
			'tipoCEP':'ALL',
			'semelhante':'N'
          }

response = requests.post(url, data= payload)

with open('correios.html', 'w') as f:
    f.write(response.text)

''' 040 Status code e acessando cabeçalho HTTP '''
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/'

r = requests.get(url)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')

print(r.headers['Set-Cookie'])
print(r.request.headers)

''' 041 Simulando o envio de um cabeçalho HTTP '''
import requests

url = 'http://michaelis.uol.com.br/busca?'

payload = {
            'r':'0',
			'f':'0',
			't':'0',
			'palavra':'talk'
        }

header = {'(Request-Line)':'GET /busca?r=0&f=0&t=0&palavra=talk HTTP/1.1',
		'Host':	'michaelis.uol.com.br',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Referer':'http://michaelis.uol.com.br/'}

r = requests.get(url, params=payload, headers=header)

soup = BeautifulSoup(r.text, 'lxml')

div = soup.find('div', {'id':'content'})
print(div.get_text())

with open('michaelis.html', 'w', encoding='utf-8') as f:
	f.write(r.text) 

print(r.request.headers)

''' 043 Trabalhando com cookies '''
import requests

url = 'http://www.submarino.com.br/'


r = requests.get(url)
cookie = r.cookies.get_dict()


busca = 'notebook'
url = 'https://www.submarino.com.br/busca?conteudo={0}'.format(busca)

r = requests.get(url)
with open('submarino.html', 'w') as f:
	f.write(r.text)

''' 044 Acompanhando redirecionamento '''
import requests

r = requests.get('http://google.com')

#mostra que a url não é mais a mesma, ela foi redirecionada
print(r.url)

#mostrar o código 302 que é o código de redirecionamento
print(r.status_code)

#mostrar que não está vazio
print(r.history)

print(r.history[0].status_code)
#mostrar o headers do redirecionamento
print(r.history[0].headers)
#mostrar a url para qual foi redirecionada
print(r.history[0].headers['Location'])

#mostrar que o parametro allow_redirects=False, ele evita redirecionamento. o valor True é por default, 
#mas pode ser colocar True também.
r = requests.get('http://google.com', allow_redirects=False)

#ai só imprimir para mostrar que é verdade, pois a url atual é a mesma.
print(r.url)

#mostrar que está vazio
print(r.history)

''' 045 Utilizando timeout '''
import requests

r = requests.get('http://www.google.com', timeout= (1, 1))
print(r.url)

''' 046 Erros e exceções '''
import requests

url = 'http://www.google.com'

try:
	r = requests.get(url)
	
except requests.exceptions.ConnectionError as e:
	print('Connection')
	print(str(e))

except requests.exceptions.HTTPError as e:
	print('HTTPError')
	print(str(e))

except requests.exceptions.Timeout as e:
	print('Timeout')
	print(str(e))

except requests.exceptions.TooManyRedirects as e:
	print('TooManyRedirects')
	print(str(e))

except requests.exceptions.RequestException as e:
	print('RequestException')
	print(str(e))

''' 047 Trabalhando com JSON Response '''
import requests

url = 'http://compras.dados.gov.br'
cnpj = '07689002000189' #Embraer

url = '{0}/contratos/v1/contratos.json?cnpj_contratada={1}'.format(url, cnpj)

r = requests.get(url)
print(r.json())
print(r.json()['_embedded']['contratos'])
print(r.json()['_embedded']['contratos'][0])

''' 048 Persistir parâmetros com Session Object '''
import requests

url = 'https://www.trocafone.com/'

s = requests.Session()
s.get(url)

busca = 'iphone'
url = 'https://www.trocafone.com/comprar/list?q={0}'.format(busca)

r = s.get(url)
with open('trocafone.html', 'w') as f:
	f.write(r.text)

''' 050 Trabalhando com proxies '''
import requests

#http://www.ultraproxies.com/
url = 'https://www.hide-my-ip.com/pt/proxylist.shtml'

proxies = {'http':('218.207.102.106:81', '218.207.102.106:81', '218.207.102.106:81')}

try:
	r = requests.get(url, proxies=proxies)
	print(r.status_code)
except requests.exceptions.ConnectionError as e:
	print(str(e))

''' 051 Download de imagens com requests '''
import requests

url = 'https://miro.medium.com/max/5000/1*1BUIofZgqVuR6nj8LbrRtQ.jpeg'

r = requests.get(url)

with open('img.jpg', 'wb') as f:
	f.write(r.content)	

''' 052 Autenticação simples com requests '''
import requests
url = 'http://httpbin.org/basic-auth/user/passwd'

r = requests.get(url)
print(r.status_code)

r = requests.get(url, auth=('user', 'passwd'))
print(r.status_code)
