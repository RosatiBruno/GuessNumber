import random
import tkinter

#! Def para quando ganhar 
def ganhou(numeroAleatorio, difiEscolhida) :
    print(f"\nParabéns! Você adivinhou o número {numeroAleatorio} corretamente!\n")
    chancesRestantes = 0
    respostaJogarNovamente = int(input("Jogar novamente? 1 - Sim | 2 - Não \n"))

    if (respostaJogarNovamente == 1) :
        facil()
    elif (respostaJogarNovamente == 2) :
        return
    else:
        print("Opção inválida!")
        ganhou() 

#! Def para quando perder 
def perdeu(numeroAleatorio, difiEscolhida) :
    print(f"\nVocê não acertou o número! Ele era o número {numeroAleatorio}\n")
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
    difiEscolhida = 1
    chancesRestantes = 5
    numeroAleatorio = random.randint(1,10)

    while (chancesRestantes > 0) :
        print(f"\nVocê tem {chancesRestantes} chances para acertar um número aleatório entre 1 e 10")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio) :                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0) :                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Normal
def normal() :
    difiEscolhida = 2
    chancesRestantes = 8
    numeroAleatorio = random.randint(1, 25)

    while (chancesRestantes > 0) :
        print(f"\nVocê tem {chancesRestantes} chances para acerter um número aleatório entre 1 e 25")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio) :                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0) :                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Difícil
def dificil() :
    difiEscolhida = 3
    chancesRestantes = 10
    numeroAleatorio = random.randint(1, 50)

    while (chancesRestantes > 0) :
        print(f"\nVocê tem {chancesRestantes} chances para acerter um número aleatório entre 1 e 50")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio):                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0):                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Extremo
def extremo() :
    difiEscolhida = 4
    chancesRestantes = 10
    numeroAleatorio = random.randint(1, 100)

    while(chancesRestantes > 0) :
        print(f"\nVocê tem {chancesRestantes} chances para acerter um número aleatório entre 1 e 100")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio):                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0):                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Dificuldade Impossível
def impossivel() :
    difiEscolhida = 5
    chancesRestantes = 1
    numeroAleatorio = random.randint(1, 1000)

    while (chancesRestantes > 0) :
        print(f"\nVocê tem apenas 1 chance para acerter um número aleatório entre 1 e 1000")
        chancesRestantes -= 1
        palpite = int(input("Digite seu palpite: "))

        if (palpite == numeroAleatorio):                        #! Vai p/ a tela de ganhar o jogo
            ganhou(numeroAleatorio, difiEscolhida)

        elif (chancesRestantes == 0):                           #! Vai p/ a tela de perder o jogo
            perdeu(numeroAleatorio, difiEscolhida)

#! Menu de escolha de dificuldade
def dificuldade() :
    print("-" * 30)
    print("Escolha a Dificuldade".center(30))
    print("-" * 30)
    print("[1] - Fácil")
    print("[2] - Normal")
    print("[3] - Difícil")
    print("[4] - Extremo")
    print("[5] - Impossível")

    dificuldadeEscolhida = int(input("Escolha sua dificuldade: "))

    if (dificuldadeEscolhida == 1) :
        facil()

    elif (dificuldadeEscolhida == 2) :
        normal()

    elif (dificuldadeEscolhida == 3) :
        dificil()

    elif (dificuldadeEscolhida == 4) :
        extremo()

    elif (dificuldadeEscolhida == 5) :
        impossivel()

    else :
        print("Opção inválida!")
        dificuldade()

#! Main do programa
def main() :
    while True :
        print("-" * 30)
        print("Adivinhe o Número".center(30))
        print("-" * 30)
        print("[1] - Jogar")
        print("[2] - Fechar o Jogo")
        print("-" * 30)

        respostaMenu = int(input("Digite a opção desejada: "))

        if (respostaMenu == 1) :                                #! Vai p/ a escolha das dificuldades
            dificuldade()

        elif (respostaMenu == 2) :
            print("Fechando o jogo...")
            break

        else :
            print("Opção Inválida!")                            #! Opção inválida, retorna para a main
            main()

#! Chamada
main()