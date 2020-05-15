from pprint import pprint
from urllib.parse import urlparse
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

# todo ------------------ exemplo 1 ------------------------

lista_n_ordenada = browser.find_element_by_tag_name('ul')  # 1

lis = lista_n_ordenada.find_elements_by_tag_name('li')  # 2

lis[0].find_element_by_tag_name('a').text  # 3

"""
1. buscamos `ul`
2. buscamos todos `li`
3. No primeiro `li`, buscamos `a` e pegamos o seu texto
ul
    li
        a
            texto
    li
        a
            texto
"""

# todo ------------------ exemplo 2 ------------------------


def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto `text`.
    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """Encontrar o elemento `a` com o link `link`.
    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - link = link que será procurado em todos as tags `a`
    """
    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

# elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')


elemento_ddg = find_by_href(browser, 'ddg')

# todo ------------------ exemplo 3 ------------------------

browser.get('http://selenium.dunossauro.live/aula_04_b.html')


nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.back()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.forward()

# todo ------------------ exemplo 4 ------------------------

browser.get('http://selenium.dunossauro.live/aula_04_b.html')


parse = urlparse(browser.current_url)

print(parse.scheme)
print(parse.netloc)

# todo ------------------ exemplo 5 ------------------------
"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04.html')


def get_links(browser, elemento):  # dicionario
    """
    Pega todos os links dentro de um elemento
    - browser = a instância do navegador
    - element = webelement [aside, main, body, ul, ol]
    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for acora in ancoras:
        resultado[acora.text] = acora.get_attribute('href')

    return resultado


"""
Parte 1
"""
sleep(2)

aulas = get_links(browser, 'aside')

pprint(aulas)

"""
browser.get(resultado_1['Aula 3'])
browser.get(resultado_1['Aula 4'])
"""


"""
Parte 2
"""
exercicios = get_links(browser, 'main')

pprint(exercicios)

browser.get(exercicios['Exercício 3'])
