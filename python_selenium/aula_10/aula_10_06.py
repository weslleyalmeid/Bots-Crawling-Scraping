from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    url_changes
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

link = browser.find_element_by_css_selector('.body_b a')
link.click()

# url_changes verifica se a url que passou é diferente da url atual
wdw.until(url_changes(url))

print)