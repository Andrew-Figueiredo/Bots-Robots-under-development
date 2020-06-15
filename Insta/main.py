from instaBot import InstagramBot
from tela import TelaPython
from info import info
from time import sleep


if __name__ == '__main__':

    try:
        # Tela Gráfica
        tela = TelaPython()
        tela.Iniciar()
        users = tela.getUsers()
        # Informações externas do usuario
        pessoaInfo = info(users)
        # Criação do Bot com os dados do Usuario.
        andrewbot = InstagramBot(pessoaInfo.usuario, pessoaInfo.senha)
        driver = andrewbot.getDriver()
        andrewbot.login()
        for pessoa in pessoaInfo.seguir:
            andrewbot.seguir_pessoas_de_outra(
                pessoa, pessoaInfo.i, pessoaInfo.f)
            andrewbot.Home()

        print("Terminou!!")
        sleep(1)
        i = 3
        while(i > 0):
            print("Fechando em " + i)
            sleep(2)
            i -= 1
        driver.close()

    except Exception as e:
        print(e)
        driver.close()
