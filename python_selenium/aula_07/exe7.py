from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep
import os


""" 
    Estado antes do click, durante o click e após o click
"""


class Escuta(AbstractEventListener):

    def before_click(self, elemento, webdriver):

        aux = elemento.get_attribute('id')
        print(f'antes do click no {elemento.tag_name} na id {aux}')

        if aux == 'nome':
            print(webdriver.find_element_by_css_selector(
                '[id="lnome"]\n').text)

        if aux == 'email':
            print(webdriver.find_element_by_css_selector(
                '[id="lemail"]\n').text)

        if aux == 'senha':
            print(webdriver.find_element_by_css_selector(
                '[id="lsenha"]\n').text)

    def after_click(self, elemento, webdriver):

        aux = elemento.get_attribute('id')
        print(f'depois do click no {elemento.tag_name} na id {aux}')

        if aux == 'nome':
            print(webdriver.find_element_by_css_selector(
                '[id="lnome"]\n').text)

        if aux == 'email':
            print(webdriver.find_element_by_css_selector(
                '[id="lemail"]\n').text)

        if aux == 'senha':
            print(webdriver.find_element_by_css_selector(
                '[id="lsenha"]\n').text)


browser = Firefox()
rapi_browser = EventFiringWebDriver(browser, Escuta())

rapi_browser.get('https://selenium.dunossauro.live/exercicio_07')

sleep(2)
input_name = rapi_browser.find_element_by_css_selector('[id="nome"]')
input_name.click()
input_name.send_keys('Weslley')

print('\n')

input_email = rapi_browser.find_element_by_id('email')
input_email.click()
input_email.send_keys('weslley@almeida.com')

print('\n')

input_password = rapi_browser.find_element_by_xpath('//input[@name="senha"]')
input_password.click()
input_password.send_keys('4321')

if os.path.isfile('geckodriver.log'):
    os.remove('./geckodriver.log')
rapi_browser.quit()
