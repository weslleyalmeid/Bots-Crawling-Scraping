from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_elemento(by, elemento, webdriver):
    print(f'Tentando encontrar "{elemento}" by {by}')
    if webdriver.find_elements(by, elemento):
        return True
    return False


def esperar_class(by, elemento, webdriver):
    aux = 'selenium'
    print(f'Tentando encontrar "{aux}" by {by}')
    elementos = webdriver.find_elements(by, elemento)
    if elementos:
        if aux in elementos[0].get_attribute('class'):
            return True
    return False


url = 'https://selenium.dunossauro.live/exercicio_09.html'
driver = Firefox()

driver.get(url)
wdw = WebDriverWait(driver, 30)

esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR, 'button')
esperar_class = partial(esperar_class, By.CSS_SELECTOR, 'button')

wdw.until(esperar_botao, 'Deu ruim button')
result = wdw.until(esperar_class, 'Deu ruim class')

assert result == True
