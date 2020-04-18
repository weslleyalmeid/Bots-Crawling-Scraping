from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

"""executar Firefox em 2° plano"""
# import os
# os.environ['MOZ_HEADLESS'] = '1'


class InstagramBot:
    def __init__(self, username, password, search, qtdeScroll):
        self.username = username
        self.password = password
        self.search = search
        self.qtdeScroll = qtdeScroll
        # Coloque o caminho para o seu geckodriver aqui
        self.driver = webdriver.Firefox(executable_path=r"./geckodriver", )
        # self.driver = webdriver.Chrome(executable_path=r"./chromedriver")  # Coloque o caminho para o seu geckodriver aqui

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login")
        time.sleep(3)

        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)

        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))

        print("Login efetuado com sucesso")
        self.curtir_fotos()

    def curtir_fotos(self):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" +
                   self.search + "/")
        print("Tag {} já pesquisada".format(self.search))
        time.sleep(5)

        """ Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: 
        quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5) """
        ("Realizando {} scrol na página".format(self.qtdeScroll))
        for i in range(1, 1):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

        # obtendo as referências a partir da tag
        hrefs = driver.find_elements_by_tag_name("a")
        # obtendo uma lista de referência, através do list comprehensions
        print("Obtendo as referências")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(self.search + " fotos: " + str(len(pic_hrefs)))

        cont = len(pic_hrefs) - 1
        for pic_href in pic_hrefs:

            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue

            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            try:
                print("Curtindo o perfil: " + pic_href)
                print("Faltam {} fotos".format(cont))
                cont -= 1

                driver.find_element_by_xpath(
                    '//div[@class="eo2As "]/section/span[@class="fr66n"]/button[@class="wpO6b "]').click()
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                time.sleep(5)


login = "login"
password = "name"
search = 'futebol'
qtdeScroll = 1
Bot_instagram = InstagramBot(login, password, search, qtdeScroll)
Bot_instagram.login()
