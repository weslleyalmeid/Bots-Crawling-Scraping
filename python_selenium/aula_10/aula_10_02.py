from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of,
    invisibility_of_element
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

wdw.until(visibility_of(browser.find_element_by_tag_name('h1')),
          'h1 não encontrado')

print('h1 disponível')
