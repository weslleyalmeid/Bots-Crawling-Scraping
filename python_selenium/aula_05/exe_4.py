from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import  sleep
from json import loads
import numpy as np


browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_04.html')

sleep(2)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()



dados = {
    'nome': 'weslley',
    'email': 'weslley@almeida.com',
    'senha': 'o0i9u8y7',
    'telefone': '7070707070'
}

preenche_form(browser, **dados)


sleep(2)

# tratamento da url
parse = urlparse(browser.current_url)
data_parse = (parse.query).replace('&', ' ')
data_parse = (data_parse).replace('=', ' ')
data_parse = data_parse.replace('%40', '@')
data_parse = data_parse.split(' ')
del(data_parse[-1])
del(data_parse[-1])
data_parse = dict(np.reshape(data_parse, (4,2)))


# tratamento do browser
data_browser = browser.find_element_by_tag_name('textarea').text
data_browser = data_browser.replace('\'', '\"')
data_browser = loads(data_browser)

assert data_browser == data_parse
print('Os dados são iguais')
sleep(2)
browser.quit()
