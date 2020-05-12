from selenium.webdriver import Firefox
from time import sleep

#todo ------------------ exemplo 1 ------------------------
url1 = 'https://curso-python-selenium.netlify.app/aula_03.html'
url2 = 'http://ddg.gg'

browser = Firefox()
browser.get(url1)

sleep(2)

a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')

for click in range(10):
    p = browser.find_elements_by_tag_name('p')
    a.click()

    print(f'Valor do p: {p[-1].text}, valor do click: {click}')

    print(f'Os valores são iguais {p[-1].text == str(click)}')

browser.quit()
