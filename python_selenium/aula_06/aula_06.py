from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
# todo -------------------- exemplo 1 --------------------------

browser.get('https://selenium.dunossauro.live/aula_06_a')

selecionando por tag
browser.find_element_by_css_selector('input').send_keys('Weslley')

# todo -------------------- exemplo 2 --------------------------

browser.get('https://selenium.dunossauro.live/aula_06_a')

selecionando por atributo type [attr=valor]
nome = browser.find_element_by_css_selector('[type="text"]')
senha = browser.find_element_by_css_selector('[type="password"]')
btn = browser.find_element_by_css_selector('[type="submit"]')

selecionando por atributo name [attr=valor]
nome = browser.find_element_by_css_selector('[name="nome"]')
senha = browser.find_element_by_css_selector('[name="senha"]')
btn = browser.find_element_by_css_selector('[name="l0c0"]')

selecionando por atributo de ocorrência [attr*=valor]
nome = browser.find_element_by_css_selector('[name*="ome"]')
senha = browser.find_element_by_css_selector('[name*="nha"]')
btn = browser.find_element_by_css_selector('[name*="l0"]')


selecionando por atributo de ocorrência [attr|=valor]
nome = browser.find_element_by_css_selector('[name|="n"]')
senha = browser.find_element_by_css_selector('[name|="s"]')
btn = browser.find_element_by_css_selector('[name|="l"]')


# selecionando por atributo de ocorrência [attr^=valor]
nome = browser.find_element_by_css_selector('[name^="n"]')
senha = browser.find_element_by_css_selector('[name^="s"]')
btn = browser.find_element_by_css_selector('[name^="l"]')
selecionando por combinação de atributos tag[attr^=valor]
nome = browser.find_element_by_css_selector('input[name^="n"]')
senha = browser.find_element_by_css_selector('input[type="password"]')
btn = browser.find_element_by_css_selector('input[name*="0c"]')


nome.send_keys('Weslley')
senha.send_keys('Weslley')

sleep(2)

btn.click()

sleep(1)
browser.quit()


# todo -------------------- exemplo 3 --------------------------
browser.get('https://selenium.dunossauro.live/aula_06_a')

browser.find_elements_by_css_selector('div.form-group')

# pegou os br irmãos da div.form-group
browser.find_elements_by_css_selector(
    'div.form-group + br')[1].get_attribute('id')

# da tag div com a classe form-group pegue o filho com id dentro-nome
browser.find_elements_by_css_selector(
    'div.form-group > #dentro-nome')[1].get_attribute('id')


# do form pega todas as tags labels existentes ignorando a hierarquia(descendentes)
browser.find_elements_by_css_selector('form label')


# todo -------------------- exemplo 4 --------------------------

browser.get('https://selenium.dunossauro.live/aula_06')