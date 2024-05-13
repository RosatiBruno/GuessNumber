import random
import os
import time

#! Def para quando ganhar 
def ganhou(numeroAleatorio, difiEscolhida) :
    os.system("cls")
    print(f"Parabéns! Você adivinhou o número {numeroAleatorio} corretamente!\n")
    time.sleep(.5)
    respostaJogarNovamente = int(input("Jogar novamente? 1 - Sim | 2 - Não \n"))

    if (respostaJogarNovamente == 1) :
        if (difiEscolhida == 1) :
            facil()
        elif (difiEscolhida == 2) :
            normal()
        elif (difiEscolhida == 3) :
            dificil()
        elif (difiEscolhida == 4) :
            extremo()
        elif (difiEscolhida == 5) :
            impossivel()
    elif (respostaJogarNovamente == 2) :
        main()
    else:
        print("Opção inválida!")
        ganhou() 

#! Def para quando perder 
def perdeu(numeroAleatorio, difiEscolhida) :
    os.system("cls")
    print(f"Você não acertou o número! Ele era o número {numeroAleatorio}\n")
    time.sleep(.5)
    respostaJogarNovamente = int(input("Jogar novamente? 1 - Sim | 2 - Não \n"))

    #! Verificação p/ jogar novamente
    if (respostaJogarNovamente == 1) :
        if (difiEscolhida == 1) :
            facil()
        elif (difiEscolhida == 2) :
            normal()
        elif (difiEscolhida == 3) :
            dificil()
        elif (difiEscolhida == 4) :
            extremo()
        elif (difiEscolhida == 5) :
            impossivel()
    elif (respostaJogarNovamente == 2) :
        return
    else:
        print("Opção inválida!")
        perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Fácil
def facil() :
    global chancesRestantes
    difiEscolhida = 1
    chancesRestantes = 5
    numeroAleatorio = random.randint(1,10)

    while (chancesRestantes > 0) :
        os.system("cls")
        print(f"Você tem {chancesRestantes} chances para acertar um número aleatório entre 1 e 10")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio) :                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0) :                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Normal
def normal() :
    global chancesRestantes
    difiEscolhida = 2
    chancesRestantes = 8
    numeroAleatorio = random.randint(1, 25)

    while (chancesRestantes > 0) :
        os.system("cls")
        print(f"Você tem {chancesRestantes} chances para acerter um número aleatório entre 1 e 25")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio) :                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0) :                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Difícil
def dificil() :
    global chancesRestantes
    difiEscolhida = 3
    chancesRestantes = 10
    numeroAleatorio = random.randint(1, 50)

    while (chancesRestantes > 0) :
        os.system("cls")
        print(f"Você tem {chancesRestantes} chances para acerter um número aleatório entre 1 e 50")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio):                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0):                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Extremo
def extremo() :
    global chancesRestantes
    difiEscolhida = 4
    chancesRestantes = 10
    numeroAleatorio = random.randint(1, 100)

    while(chancesRestantes > 0) :
        os.system("cls")
        print(f"Você tem {chancesRestantes} chances para acerter um número aleatório entre 1 e 100")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio):                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0):                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Impossível
def impossivel() :
    global chancesRestantes
    difiEscolhida = 5
    chancesRestantes = 1
    numeroAleatorio = random.randint(1, 1000)

    while (chancesRestantes > 0) :
        os.system("cls")
        print(f"Você tem apenas 1 chance para acerter um número aleatório entre 1 e 1000")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio):                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0):                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Menu de escolha de dificuldade
def dificuldade() :
    os.system("cls")
    print("-" * 30)
    print("Escolha a Dificuldade".center(30))
    print("-" * 30)
    print("[1] - Fácil")
    print("[2] - Normal")
    print("[3] - Difícil")
    print("[4] - Extremo")
    print("[5] - Impossível")

    dificuldadeEscolhida = input("Escolha sua dificuldade: ")

    if (dificuldadeEscolhida == "1") :
        facil()

    elif (dificuldadeEscolhida == "2") :
        normal()

    elif (dificuldadeEscolhida == "3") :
        dificil()

    elif (dificuldadeEscolhida == "4") :
        extremo()

    elif (dificuldadeEscolhida == "5") :
        impossivel()

    else :
        os.system("cls")
        print("Opção inválida!")
        time.sleep(1)
        dificuldade()

#! Main do programa
def main() :
    global chancesRestantes
    while True :
        os.system("cls")
        print("-" * 30)
        print("Adivinhe o Número".center(30))
        print("-" * 30)
        print("[1] - Jogar")
        print("[2] - Fechar o Jogo")
        print("-" * 30)
  
        respostaMenu = input("Digite a opção desejada: ")

        if (respostaMenu == "1") :                                #! Vai p/ a escolha das dificuldades
            dificuldade()

        elif (respostaMenu == "2") :
            os.system("cls")

            print("Fechando o jogo...")

            if (chancesRestantes > 0) :                         #! Caso ainda tenha tentativas restantes, zera elas p/ encerrar o programa
                chancesRestantes = 0

            time.sleep(1)
            break
            
        else :
            os.system("cls")                                    #! Comando p/ limpar a tela
            print("Opção Inválida!")                            #! Opção inválida, retorna para a main
            time.sleep(1)                                       #! Comando p/ esperar p/ executar a prox. linha
            os.system("cls")
        
        break                                                   #! Break para encerrar o programa

#! Chamada
main()