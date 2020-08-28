from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from time import sleep

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')
sleep(3)

browser.find_element_by_id('alert').click()
sleep(3)

alerta = Alert(browser) # Lidar com erros

alerta = browser.switch_to.alert # Não lida com erros


alerta.accept() # Confirma, clica no OK
alerta.dismiss() # Confirma, clica no OK
