from selenium.webdriver import  Firefox
from time import sleep

browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_06')



sleep(1)
location_form = browser.find_element_by_css_selector('header p:nth-child(2) span').text

while  'Mentira' not in location_form:
    print(f'estamos no formulário {location_form}')
    form = browser.find_element_by_css_selector(f'.form-{location_form}')
    form.find_element_by_css_selector('[name="nome"]').send_keys('nome')
    form.find_element_by_css_selector('[name="senha"]').send_keys('senha')
    
    sleep(1)
    form.find_element_by_css_selector(f'[name={location_form}]').click()
    sleep(1)
    location_form = browser.find_element_by_css_selector('header span').text


print(location_form)
browser.quit()


