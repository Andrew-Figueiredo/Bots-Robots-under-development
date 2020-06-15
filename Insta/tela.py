import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        self.users = []
        #layout
        layout = [
            [sg.Text('Voce deseja adicionar um usuario no grupo?'),
            sg.Radio('sim','Add', key='querAdd'), sg.Radio('não','Add',default=True, key='NquerAdd')],
            [sg.Text('Qual o usuario: '), sg.Input( key='nameUser')],
            [sg.Button('Finalizar')]

        ]
        #janela
        self.janela = sg.Window('Program Instagram').layout(layout)


    def Iniciar(self):
        while(True):
                    # Extrair dados da tela
            self.event, self.values = self.janela.Read()
            print(self.values['querAdd'])
            print(self.values['NquerAdd'])

            radioSim = self.values['querAdd']
            if(radioSim == True):
                nameUser = self.values['nameUser']
                self.users.append(nameUser)
                print(f"add com sucesso! confirmar: {nameUser}")
            else:
                break

    def getUsers(self):
        return self.users

