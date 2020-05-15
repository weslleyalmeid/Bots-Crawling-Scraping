from bs4 import BeautifulSoup
import requests

def post_http(url, nome_livro):
    payload = {
        'palavra': nome_livro,
        'enviar': 'Buscar'
    }
    try:
        return requests.post(url, payload)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        print(str(e))
        pass
    except Exception as e:
        raise
    return None

def tratar_dados(lista_auxiliar):

    preco = lista_auxiliar[7].replace('Preço: ', '')

    d = {   'titulo': lista_auxiliar[0],
            'url_capa': lista_auxiliar[8],
            'url_produto': lista_auxiliar[9],
            'preco': preco
        }

    return d


def parser_html(content):
    soup = BeautifulSoup(content, 'lxml')

    produtos = soup.find_all('table')[10].find_all('td')

    # f = open('td.html', 'w')

    # for produto in produtos:
    #     f.write(str(produto))
    #     f.write('\n\n\n')

    # f.close()

    lista_produto = []
    lista_auxiliar = []

    url = 'https://novatec.com.br/'
    url_capa = ''
    url_produto = ''
    for produto in produtos:
        tag_a = produto.find('a')
        if tag_a:
            if tag_a.next_element.next_element.name == 'img':
                url_capa = "{0}".format(tag_a.img.get('src'))
                url_produto = "{0}{1}".format(url, tag_a.get('href'))
                
        for string in produto.stripped_strings:
            if string == 'Esgotado':
                continue
            lista_auxiliar.append(string)

        if len(lista_auxiliar) > 6:
            lista_auxiliar.append(url_capa)
            lista_auxiliar.append(url_produto)
            lista_produto.append(tratar_dados(lista_auxiliar))
       
        del lista_auxiliar[:]


    if len(lista_produto) > 0:
        del lista_produto[0]
    
    return lista_produto




if __name__ == "__main__":
    url = 'https://novatec.com.br/busca.php'
    nome_livro = 'redes de computadores'

    r = post_http(url, nome_livro)

    lista_produto = []
    if r:
        lista_produto = parser_html(r.text)
        
    for i in lista_produto:
        print(str(i) + '\n')

    # with open('result.html', 'w') as f:
    #     f.write(r.text)