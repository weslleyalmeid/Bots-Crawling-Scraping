from selenium.webdriver import Firefox
from time import sleep

#todo ------------------ exercicio 1 ------------------------
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)

sleep(3)

# h1 = browser.find_element_by_tag_name('h1')
p = browser.find_elements_by_tag_name('p')
h1 = browser.find_element_by_tag_name('h1').text
aux = {h1:{}}
for i in range(len(p)):
    atributo = p[i].get_attribute('atributo')
    texto = p[i].text
    aux[h1].update({atributo: texto})

print(aux)
browser.quit()
