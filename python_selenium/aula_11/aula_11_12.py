from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import (
#
# )


browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get('http://selenium.dunossauro.live/aula_11_d')

# Precisa ser repassado o nome do iframe
browser.switch_to.frame('iframe')

browser.find_element_by_id('nome').send_keys('weslley')
