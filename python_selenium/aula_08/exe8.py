from selenium.webdriver import Firefox
import json
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def color():
    print(browser.find_element_by_xpath('//div[@class="centro"]/.//span').text)


def caixinha_colorida(key1=None, key2=None):

    ac.pause(3)
    color()

    if key1:
        ac.key_down(key1)

    if key2:
        ac.key_down(key2)

    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click()
    color()

    ac.pause(1)
    ac.double_click()
    color()

    ac.pause(1)
    # ac.context_click()

    ac.pause(1)
    ac.move_to_element(span)
    ac.click()
    color()

    if key1:
        ac.key_up(key1)

    if key2:
        ac.key_up(key2)



browser = Firefox()
browser.get('https://selenium.dunossauro.live/caixinha')


caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_xpath('//div[@class="centro"]/h1')

ac = ActionChains(browser)

caixinha_colorida()
""" 
    vermelho, amarelo, azul, preto, rosa bosta
"""

ac.pause(2)

# caixinha_colorida(Keys.CONTROL)

"""
    verde marrom, roxo, rosa claro, rosa choque
"""
ac.perform()
