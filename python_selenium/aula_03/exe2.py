from selenium.webdriver import Firefox
from time import sleep

#todo ------------------ exercicio 2 ------------------------
import re

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser = Firefox()
browser.get(url)

sleep(3)
num = int(
    re.findall('\d+',browser.find_elements_by_tag_name('p')[-1].text)[0])

a = browser.find_element_by_tag_name('a')
a.click()
sleep(1)

while len(browser.find_elements_by_tag_name('p')[-1].text) < 3:
    aux = browser.find_elements_by_tag_name('p')[-1].text
    print(f"numero esperado {num} e o numero que saiu {aux}")
    a.click()
    sleep(1)

sleep(5)
browser.quit()