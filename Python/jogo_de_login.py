import random
import time
from PIL import Image


user = "Augusto"
senha_inicial = "244466666"


def finalizar():
    print(f"Bem vindo(a), {user}", "\n")
    quit()

def questão10():
    while True:
        q10 = input("Realize a equação: 5x-7=18" "\n:")
        if q10 != "5":
            print("Resposta incorreta")
            continue
        else:
            print("\n" * 2)
            finalizar()

def questão9():
    while True:
        try:
            imagem = Image.open(r'C:\Users\User\Desktop\Vscode\Python\Campo Minado.png')
            imagem.show()
        except FileNotFoundError:
                print("Erro: Arquivo não encontrado. Verifique o caminho.")
            
        q9 = input("Onde é mais provável haver uma mina, na grade F4 ou C5? ")
        if q9 != 'F4':
            print("Resposta incorreta")
            continue
        else:
            questão10()

def questão8():
    while True:
        q8 = input("Cara ou coroa? ").lower()
        cara_ou_coroa = ['cara', 'coroa']
        aleatorio = random.choice(cara_ou_coroa)
        print("E a moeda caiu...")
        for i in range(3):
            print(".", "\n")
            time.sleep(1)
        print(aleatorio)
        if q8 != aleatorio:
            print("Resposta incorreta")
            continue
        else:
            questão9()
        
def questão7():
    while True:
        q7 = input("Qual o nome da bomba atômica jogada em Nagazaki em 9 de agosto de 1945? ").lower()
        if q7 != "fat man":
            print("Resposta incorreta.")
            continue
        else:
            questão8()

def questão6():
    while True:
        q6 = input("Eu gosto de musse de limão? (S/N): ").upper()
        if q6 != "S":
            print("Resposta incorreta.")
            continue
        else:
            questão7()

def questão5():
    while True:
        q5 = input("Resolva: 7x8 = ? ")
        if q5 != "56":
            print("Resposta incorreta.")
            continue
        else:
            questão6()

def questão4():
    while True:
        q4 = input("Quantos anos eu tenho? ")
        if q4 != "15":
            print("Resposta incorreta.")
            continue
        else:
            questão5()

def questão3():
    while True:
        q3 = input("Em que ano a segunda guerra mundial começou? ")
        if q3 != "1945":
            print("Resposta incorreta.")
            continue
        else:
            questão4()

def questão2():
    while True:
        q2 = input("Qual é o nome do meu cachorro branco?: ").lower()
        if q2 != "milk":
            print("Resposta incorreta.")
            continue
        else:
            questão3()

def questão1():
    while True:
        Usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        if Usuario != user or senha != senha_inicial:
            print("Usuário ou senha incorreta.")
            continue
        else:
            questão2()

def iniciar_jogo():
    while True:
        iniciar = input("Deseja iniciar o jogo? (S/N): ").upper()

        if iniciar == "S" or "N":
            if iniciar == "S":
                print("Ok! iniciando o jogo." "\n")
                questão1()             
            else:
                print("Ok.")
                quit()
        else:
            print("Por favor, insira uma ação válida.")
            continue

iniciar_jogo()