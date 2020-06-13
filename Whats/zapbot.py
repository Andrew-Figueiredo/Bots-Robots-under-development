import time
from selenium import webdriver

class WhatsappBot:
    def __init__ (self):
        self.mensagem = ""
        self.grupos = ["Grupo1", "Grupo2"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="Grupo1" class="_3ko75 _5h6Y_ _3Whw5">Grupo1</span>
        #<footer tabindex="-1" class="_2vJ01">
        #<span data-icon="send" class="">
        print("Preparando seu Envio")
        self.driver.get('https://web.whatsapp.com')
        time.sleep(5)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(3)

            print(f"Mensagem para o Grupo {grupo} enviado!")
        
        print("Enviado com sucesso!")


bot = WhatsappBot()
bot.EnviarMensagens()