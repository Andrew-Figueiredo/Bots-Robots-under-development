from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from info import info


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        self.seguir = []
        self.i = 2
        self.f = 4

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
        time.sleep(random.randint(3, 4))
        self.Home()
        agora_nao = driver.find_element_by_xpath(
            "//button[contains(text(),'Agora não')]")
        time.sleep(2)
        agora_nao.click()
        time.sleep(2)

    def curtir_fotos_home(self):
        driver = self.driver
        self.Home()
        agora_nao = driver.find_element_by_xpath(
            "//button[contains(text(),'Agora não')]")
        time.sleep(3)
        agora_nao.click()
        time.sleep(2)

    def Home(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(random.randint(2, 3))

    def aperta_botao_seguir_igual_humano(self, elements, i, f):

        for element in elements:
            element.click()
            time.sleep(random.randint(i, f))

    def seguir_pessoas_de_outra(self, arroba, i, f):
        try:

            driver = self.driver
            driver.get(f"https://www.instagram.com/{arroba}/")
            time.sleep(3)
            # Abrir a aba de seguidores
            seguidores = driver.find_element_by_xpath(
                f"//a[@href='/{arroba}/followers/']")
            seguidores.click()
            time.sleep(3)
            buttons_seguidores = driver.find_elements_by_xpath(
                "//div[@class ='Pkbci']//button[@class='sqdOP  L3NKy   y3zKF     ']")
            if str(len(buttons_seguidores)) != 0:
                self.aperta_botao_seguir_igual_humano(buttons_seguidores, i, f)
            # fechar aba
            time.sleep(1)

            driver.get(f"https://www.instagram.com/{arroba}/")

            # Abrir a aba de seguindo
            seguindo = driver.find_element_by_xpath(
                f"//a[@href='/{arroba}/following/']")
            seguindo.click()
            time.sleep(3)
            buttons_seguindo = driver.find_elements_by_xpath(
                "//div[@class='Pkbci']//button[@class='sqdOP  L3NKy   y3zKF     ']")
            if str(len(buttons_seguindo)) != 0:
                self.aperta_botao_seguir_igual_humano(buttons_seguindo, i, f )
            time.sleep(1)
            # fechar aba
            driver.get(f"https://www.instagram.com/{arroba}/")


        except Exception as e:
            print(e)
    time.sleep(random.randint(1,3))


if __name__ == '__main__':

    try:
        pessoaInfo = info()
        andrewbot = InstagramBot(pessoaInfo.usuario, pessoaInfo.senha)
        driver = andrewbot.getDriver()
        andrewbot.login()
        for pessoa in pessoaInfo.seguir:
            andrewbot.seguir_pessoas_de_outra(pessoa, pessoaInfo.i, pessoaInfo.f)
            andrewbot.Home()


        print("Terminou!!")
        time.sleep(1)
        i = 3
        while(i>0):
            print("Fechando em "+ i)
            time.sleep(2)
            i-=1
        driver.close()

    except Exception as e:
        print(e)
        driver.close()
