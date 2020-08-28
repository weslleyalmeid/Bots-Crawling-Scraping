from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_c')

# abre uma nova aba em branco
browser.execute_script('window.open("")')

# abrindo facebook em uma nova guia
url = 'https://facebook.com.br'
browser.execute_script(f'window.open("{url}"")')


browser.switch_to.window(browser.window_handles[-1])

browser.get('http://ddg.gg')
