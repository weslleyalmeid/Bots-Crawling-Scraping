from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep


# todo -------------------- exemplo 1 --------------------------
# """
#     1. Checar se a mudança ocorre no span (focus, blur)
#     2. Checar se a mudança ocorre no p (change)
# """
# browser = Firefox()
# browser.get('https://selenium.dunossauro.live/aula_07_d')

# input_text = browser.find_element_by_tag_name('input')
# span = browser.find_element_by_tag_name('span')
# p = browser.find_element_by_tag_name('p')

# """
#     Quando clicar no elemento `input`
#     Então o texto 'está com foco' de ve ser o content de `span`

#     Quando clicar no elemento `span`
#     Então o texto 'está com foco' de ve ser o content de `span`
# """

# input_text.click()
# assert 'está com foco' == span.text, 'está com foco não está em span'

# span.click()
# assert 'está sem foco' == span.text, 'está sem foco não está em span'


# """
#     Dado que o texto '0' deve ser content de `p`
#     Quando enviar "batata" no elemento `input`
#     Então o texto 'está com foco' de ve ser o content de `span`

#     Quando clicar no elemento `span`
#     Então o texto 'está com foco' de ve ser o content de `span`
#     Então o texto '1' deve ser content de `p`
# """

# assert p.text == '0', 'p não é zero'
# input_text.send_keys('batata')
# assert 'está com foco' == span.text, 'está com foco não está em span'
# span.click()
# assert 'está sem foco' == span.text, 'está sem foco não está em span'
# assert p.text == '1', 'p não é um'

# browser.quit()

# todo -------------------- exemplo 2 --------------------------
class Escuta(AbstractEventListener):

    def after_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('voltando para página anterior')

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)

        print(f'antes do click no {elemento.tag_name}\n')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)

        print(f'depois do click no {elemento.tag_name}\n')


browser = Firefox()
rapi_browser = EventFiringWebDriver(browser, Escuta())

rapi_browser.get('https://selenium.dunossauro.live/aula_07_d')


input_text = rapi_browser.find_element_by_tag_name('input')
span = rapi_browser.find_element_by_tag_name('span')
p = rapi_browser.find_element_by_tag_name('p')

input_text.click()
span.click()

rapi_browser.get('https://selenium.dunossauro.live/aula_07_c')
rapi_browser.back()

browser.quit()
