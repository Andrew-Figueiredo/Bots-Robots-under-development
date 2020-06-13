from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
from infos import info


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        self.seguir = []

    def getDriver(self):
        return self.driver

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        campo_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_password = driver.find_element_by_xpath(
            "//input[@name='password']")
        campo_password.click()
        campo_password.clear()
        campo_password.send_keys(self.password)
        campo_password.send_keys(Keys.RETURN)
        time.sleep(random.randint(2, 3))
        self.Home()

    def curtir_fotos_home(self):
        driver = self.driver
        self.Home()
        agora_nao = driver.find_element_by_xpath(
            "//button[contains(text(),'Agora não')]")
        time.sleep(3)
        agora_nao.click()
        time.sleep(2)

    def loading(self):
        for i in range(1, 5):
            print(".")
            time.sleep(1)

    def Home(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(random.randint(2, 3))

    def aperta_botao_seguir_igual_humano(self, elements):

        for element in elements:
            element.click()
            time.sleep(random.randint(10, 30))

    def seguir_pessoas_de_outra(self, arroba):
        driver = self.driver
        driver.get(f"https://www.instagram.com/{arroba}/")
        time.sleep(3)
        # Abrir a aba de seguidores
        seguidores = driver.find_element_by_xpath(
            f"//a[@href='/{arroba}/followers/']")
        seguidores.click()
        time.sleep(1)
        buttons_seguidores = driver.find_elements_by_xpath(
            "//div[@class='PZuss']//button[@class='sqdOP  L3NKy   y3zKF     ']")
        self.aperta_botao_seguir_igual_humano(buttons_seguidores)
        #fechar aba
        driver.find_element_by_xpath("//div[@class=WaOAr]//button[@class='wpO6b']").click()


        # Abrir a aba de seguindo
        seguindo = driver.find_element_by_xpath(
            "//a[@href='/{arroba}/following/']")
        seguindo.click()
        time.sleep(1)
        buttons_seguindo = driver.find_elements_by_xpath(
            "//div[@class='PZuss']//button[@class='sqdOP  L3NKy   y3zKF     ']")
        self.aperta_botao_seguir_igual_humano(buttons_seguindo)
        driver.find_element_by_xpath("//div[@class=WaOAr]//button[@class='wpO6b']").click()

        time.sleep(3)


if __name__ == '__main__':
    fim = False

    try:

        pessoas = info()
        andrewbot = InstagramBot(pessoas.usuario, pessoas.senha)
        andrewbot.loading()
        driver = andrewbot.getDriver()
        andrewbot.login()
        for pessoa in pessoas.seguir:
            andrewbot.seguir_pessoas_de_outra(pessoa)

        print("Terminou!!")

        time.sleep(5)
        driver.close()

    except Exception as e:
        print(e)
        driver.close()
