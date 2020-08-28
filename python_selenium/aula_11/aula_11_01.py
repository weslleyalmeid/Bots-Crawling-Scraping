from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')
sleep(3)
browser.find_element_by_id('alert').click()

alerta = browser.switch_to.alert
sleep(3)

alerta.accept() # Confirma, clica no OK
#  alerta.dismiss() # Confirma, clica no OK
