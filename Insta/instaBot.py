from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
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
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_password = driver.find_element_by_xpath("//input[@name='password']")
        campo_password.click()
        campo_password.clear()
        campo_password.send_keys(self.password)
        campo_password.send_keys(Keys.RETURN)
        time.sleep(random.randint(2,3))
        driver.get('https://www.instagram.com')
        time.sleep(random.randint(2,3))

        


    def curtir_fotos_home(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(4)
        driver.refresh()
        time.sleep(4)
        agora_nao = driver.find_element_by_xpath("//button[contains(text(),'Agora não')]")
        time.sleep(3)
        agora_nao.click()
        time.sleep(2)


    def aperta_botao_seguir_igual_humano(self, elements):
        
        for element in elements:
            element.click()
            time.sleep(random.randint(15,40))


    def seguir_pessoas_de_outra(self, arroba):
        driver = self.driver
        driver.get(f"https://www.instagram.com/{arroba}/")
        time.sleep(3)
        #Abrir a aba de seguidores
        seguidores = driver.find_element_by_xpath("//a[@href='/dellencalcados1/followers/']")
        seguidores.click()
        time.sleep(1)
        buttons_seguidores = driver.find_elements_by_xpath("//div[@class='PZuss']//button[@class='sqdOP  L3NKy   y3zKF     ']")
        
        #Abrir a aba de seguindo
        seguindo = driver.find_element_by_xpath("//a[@href='/dellencalcados1/following/']").click()
        time.sleep(1)

        
        buttons_seguindo = driver.find_elements_by_xpath("//div[@class='PZuss']//button[@class='sqdOP  L3NKy   y3zKF     ']")
        print('teste: ' + str(len(buttons_seguidores)))
        print('teste: ' + str(len(buttons_seguindo)))



        # array_de_lis = driver.find_elements_by_xpath("//li")

        time.sleep(200)

        #<a class=" _81NM2" href="/dellencalcados1/followers/"><span class="g47SY lOXF2" title="6">6</span> seguidores</a>

        



if __name__ == '__main__':

    try:
        pessoas = info()
        andrewbot = InstagramBot(pessoas.usuario, pessoas.senha)
        
        driver = andrewbot.getDriver()
        andrewbot.login()
        for pessoa in pessoas.seguir:
            andrewbot.seguir_pessoas_de_outra(pessoa)

        
        time.sleep(2000)
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
    
    
