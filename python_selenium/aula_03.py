from selenium.webdriver import Firefox
from time import sleep

#todo ------------------ exercicio 1 ------------------------
# url1 = 'https://curso-python-selenium.netlify.app/aula_03.html'
# url2 = 'http://ddg.gg'

# browser = Firefox()
# browser.get(url1)

# sleep(2)

# a = browser.find_element_by_tag_name('a')
# p = browser.find_element_by_tag_name('p')

# for click in range(10):
#     p = browser.find_elements_by_tag_name('p')
#     a.click()

#     print(f'Valor do p: {p[-1].text}, valor do click: {click}')

#     print(f'Os valores são iguais {p[-1].text == str(click)}')

# browser.quit()

#todo ------------------ exercicio 1 ------------------------
# url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
# browser = Firefox()
# browser.get(url)

# sleep(3)

# # h1 = browser.find_element_by_tag_name('h1')
# p = browser.find_elements_by_tag_name('p')
# h1 = browser.find_element_by_tag_name('h1').text
# aux = {h1:{}}
# for i in range(len(p)):
#     atributo = p[i].get_attribute('atributo')
#     texto = p[i].text
#     aux[h1].update({atributo: texto})

# print(aux)
# browser.quit()

# #todo ------------------ exercicio 2 ------------------------
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
