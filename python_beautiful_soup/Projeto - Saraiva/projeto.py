import requests
from bs4 import BeautifulSoup


def get_http(url, nome_livro):

    nome_livro = nome_livro.replace(' ', '%20')
    url = '{0}?q={1}'.format(url, nome_livro)

    try:
        return requests.get(url)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.excepetions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
    except Exception as e:
        raise


def get_produtos(content):
    soup = BeautifulSoup(content, 'lxml')
    produtos = soup.find_all('a', {'class': 'nm-product-img-link'})

    lista_produtos = []

    for produto in produtos:
        info_produto = [produto.get('href'), produto.get('title')]
        lista_produtos.append(info_produto)
    return lista_produtos


def get_http_page_produto(lista_produtos):

    d = {}
    lista_prod = []
    for produto in lista_produtos:

        produto[0] = ('https:' + produto[0])

        try:
            r = requests.get(produto[0])

        except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
        requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(str(e))
            r = None
        
        except Exception as e:
            raise

        d = parse_page_produto(r.text, produto[0], produto[1])
        lista_prod.append(d.copy())
    
    return lista_prod
        

def parse_page_produto(content, url_produto, titulo):

    soup = BeautifulSoup(content, 'lxml')

    meta = soup.find('meta', {'itemprop': 'price'})
    preco = meta.get('content')

    d = {}

    try:
        d = {
            'titulo': titulo,
            'Preco': preco,
            'url_produto': url_produto
        }
    except AttributeError as e:
        pass

    return d

    # ! //div[@class="tab-pane active show"]
    # * //p[@class="mb-0 price-destaque"]



if __name__ == '__main__':

    url = 'https://busca.saraiva.com.br/busca'
    nome_livro = 'redes de computadores'

    r = get_http(url, nome_livro)

    # * Escrever no arquivo
    # with open('result.html', 'w') as f:
    #     f.write(r.text)
    if r:
        lista_produtos = get_produtos(r.text)
        lista = get_http_page_produto(lista_produtos)
        print(lista)
