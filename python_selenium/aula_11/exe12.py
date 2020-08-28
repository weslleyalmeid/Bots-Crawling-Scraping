from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    new_window_is_opened,
    number_of_windows_to_be,
    alert_is_present,
    visibility_of_element_located
)

browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_12.html')
wdw = WebDriverWait(browser, 20)

# Verificado se campo clickable está disponível
nome =  wdw.until(
    element_to_be_clickable(('name', 'nome'))
)
nome.click()
alerta = wdw.until(alert_is_present())
nome= 'weslley'
alerta.send_keys(nome)
alerta.accept()

sleep(2)

# preencher campo email
email =  browser.find_element_by_name('email').click()
alerta = wdw.until(alert_is_present())
email = 'weslley@almeida.com'
alerta.send_keys(email)
alerta.accept()

sleep(2)

# preencher campo email
signo =  browser.find_element_by_name('signo').click()
alerta = wdw.until(alert_is_present())
signo = 'elefante'
alerta.send_keys(signo)
alerta.accept()

sleep(2)

browser.find_element_by_xpath('//input[@type="submit"]').click()

# Não sei por qual motivo, mas não deu certo
# wdw.until(
#     new_window_is_opened(browser.window_handles)
# )


# verifica se uma segunda página foi aberta
wdw.until(
    number_of_windows_to_be(2)
)

# muda para outra página
browser.switch_to.window(browser.window_handles[-1])

# verificado se campo está disponível para obter texto
locator = (By.CLASS_NAME, 'body_b')
text = wdw.until(
    visibility_of_element_located(locator)
)

text = browser.find_element_by_id('content').text.split('\n')
nome_site = text[1].split(':')[-1].strip()
email_site = text[2].split(':')[-1].strip()
signo_site = text[3].split(':')[-1].strip()

assert nome == nome_site
assert email == email_site
assert signo == signo_site
print('Funcionou com sucesso')