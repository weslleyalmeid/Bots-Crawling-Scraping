from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep
import pprint

def links_click(browser, links):
    for link in links:
        if link.text == browser.title:
            link.click()
            break

browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_03.html')

sleep(5)
#todo --------- acesso a 1° homepage - continue ------------------
print('está na 1° página')
main = browser.find_element_by_tag_name('main')
main.find_element_by_tag_name('a').click()


#todo --------- acesso a 2° homepage - operação errada------------------
print('está na 2° página')
sleep(5)
browser.find_element_by_css_selector("a[attr='errado']").click()


#todo --------- acesso a 3° homepage - title ------------------
print('está na 3° página')
print('Esse trecho realmente demora')
sleep(30)
main = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.TAG_NAME, 'main')))
print(main.is_displayed())
sleep(20)
links = main.find_elements_by_tag_name('a')
links_click(browser, links)


#todo --------- acesso a 4° homepage - url------------------#
print('está na 5° página')
sleep(10)


parse = urlparse(browser.current_url)
parse = parse.path.split(sep= '/')[1]

browser.find_element_by_link_text(parse).click()

#todo --------- acesso a 5° homepage - diablonee ------------------#
print('está na 6° página')
sleep(10)

browser.refresh()

#todo --------- acesso a 6° homepage - VENCEU ------------------#
print('está na 7° página - VENCEU!!')
