from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_b')

browser.find_element_by_id('popup').click()

def find_window(content: str):
    wids = browser.window_handles
    for window in wids:
        # switch_to.window muda de janela
        browser.switch_to.window(window)
        if content in browser.page_source.lower():
            break

find_window('<h1>popup')
