from instaBot import InstagramBot
from tela import TelaPython
from info import info


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
