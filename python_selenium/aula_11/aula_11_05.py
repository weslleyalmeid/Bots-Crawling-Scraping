from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = Firefox()
wdw = WebDriverWait(browser, 30)

browser.get('http://selenium.dunossauro.live/aula_11_a')
sleep(3)

# alerta = Alert(browser)

browser.find_element_by_id('alertd').click()

print('antes de esperar o alerta')
alerta = wdw.until(alert_is_present())
print('depois de esperar o alerta')

alerta.accept() # alerta