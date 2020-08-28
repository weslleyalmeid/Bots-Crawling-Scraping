from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys


browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_08_a'
texto = 'Selenium'

browser.get(url)

# hi-level
elemento = browser.find_element_by_name('texto')

# low-level
ac = ActionChains(browser)
ac.move_to_element(elemento)
ac.click(elemento)


def digita_com(key1= None, key2= None):

    if key2:
        ac.key_down(key1).key_down(key2)

    elif key1:
        ac.key_down(key1)

    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)

    if key2:
        ac.key_up(key1).key_down(key2)

    elif key1:
        ac.key_up(key1)


digita_com()
digita_com(Keys.SHIFT)

#todo - Falta conseguir o CAPS LOCK
# digita_com(Keys.TAB, Keys.RETURN)


ac.perform()