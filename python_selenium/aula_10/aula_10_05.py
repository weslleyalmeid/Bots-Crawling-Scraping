from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    staleness_of
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'

browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

element = browser.find_element_by_tag_name('button')

wdw.until(staleness_of(element))

element.click()

p = browser.find_element_by_tag_name('p')

assert 'quei' in p.text