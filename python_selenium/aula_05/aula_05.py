
from selenium.webdriver import Firefox
from urllib.parse import urlparse
from json import loads
from time import sleep

# todo -------------- exemplo 1 --------------------------
# url = 'http://selenium.dunossauro.live/aula_05_a.html'

# firefox = Firefox()

# firefox.get(url)

# div_py = firefox.find_element_by_id('python')
# div_hk = firefox.find_element_by_id('haskell')
# print(div_hk.text)

# firefox.quit()

# todo -------------- exemplo 2 --------------------------

# url = 'http://selenium.dunossauro.live/aula_05_b.html'

# firefox = Firefox()

# firefox.get(url)

# topico = firefox.find_element_by_class_name('topico')
# linguagens = firefox.find_elements_by_class_name('linguagens')

# for linguagen in linguagens:
#     print(
#         (linguagen.find_element_by_tag_name('h2').text,
#          linguagen.find_element_by_tag_name('p').text)
#     )


# todo -------------- exemplo 3 --------------------------

url = 'http://selenium.dunossauro.live/aula_05_c.html'

firefox = Firefox()

firefox.get(url)


def melhor_filme(browser, filme, email, telefone):
    """Preenche o formulário do melhor filme de 2020."""
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()


melhor_filme(
    firefox,
    'Parasita',
    'wes@weslley',
    '(012)12345678'
)


sleep(5)
firefox.quit()



# todo -------------- exemplo 4 --------------------------

url = 'http://selenium.dunossauro.live/aula_05.html'

firefox = Firefox()

firefox.get(url)

# nome, email, senha, telefone, btn


def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


sleep(2)

estrutura = {
    'nome': 'Eduardo',
    'email': 'dudu@du.edu',
    'senha': 'q1w2e3r4',
    'telefone': '987654321'
}

preenche_form(firefox, **estrutura)

url_parseada = urlparse(firefox.current_url)

sleep(2)

texto_resultado = firefox.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)


assert dic_result == estrutura

firefox.quit()