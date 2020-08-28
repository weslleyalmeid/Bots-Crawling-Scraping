from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys


browser = Firefox()
#  -------------------- exemplo 1 --------------------------

# url = 'https://selenium.dunossauro.live/keyboard'

# browser.get(url)

# html = browser.find_element_by_tag_name('html')

# html.send_keys('selenium')


#  -------------------- exemplo 2 --------------------------

# url = 'https://selenium.dunossauro.live/aula_08_a'
# texto = 'Selenium'

# browser.get(url)

# # hi-level
# elemento = browser.find_element_by_name('texto')

# # low-level
# ac = ActionChains(browser)
# ac.move_to_element(elemento)
# ac.click(elemento)


# def digita_com(key):
#     ac.key_down(key)
#     for letra in texto:
#         ac.key_down(letra)
#         ac.key_up(letra)
#     ac.key_up(key)


# digita_com(Keys.SHIFT)
# # digita_com(Keys.UP) 


# ac.perform()

#  -------------------- exemplo 3 --------------------------


url = 'https://selenium.dunossauro.live/caixinha'

browser.get(url)

caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)


def caixinha_colorida(key1, key2= None):
    ac.pause(1)
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.click()
    ac.double_click()
    ac.move_to_element(span)
    ac.key_up(key1)
    if key2:
        ac.key_up(key2)

# elemto_a = caixa
# elemto_b = span

# ac.drag_and_drop(elemto_a, elemto_b)

# ac.click_and_hold(elemto_a)
# ac.move_to_element(elemto_b)
# ac.release(elemto_b)

caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
caixinha_colorida(Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(caixa)
ac.context_click()
ac.perform()