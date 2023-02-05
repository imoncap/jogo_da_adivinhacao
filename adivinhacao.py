import random

def jogar():
    print('-'*50)
    print('Bem vindo(a) ao jogo da adivinhação!')
    print('-'*50)

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print('Escolha um nível de dificuldade:')
    print('(1) Fácil\n(2) Médio\n(3) Difícil\n')

    while (tentativas == 0):
        nivel = int(input('>>> '))
        if (nivel == 1):
            print('-' * 50)
            print('Nível FÁCIL selecionado.\nVocê tem 10 tentativas!')
            print('-' * 50)
            tentativas = 10
        elif (nivel == 2):
            print('-' * 50)
            print('Nível MÉDIO selecionado.\nVocê tem 5 tentativas!')
            print('-' * 50)
            tentativas = 5
        elif (nivel == 3):
            print('-' * 50)
            print('Nível DIFÍCIL selecionado.\nVocê tem 3 tentativas!')
            print('-' * 50)
            tentativas = 3
        else:
            print('-' * 50)
            print('Digite um valor entre 1 e 3.')
            print('-' * 50)

    for rodada in range (1, tentativas + 1, 1):
        print(f'Rodada {rodada} de {tentativas}')
        print('-' * 50)
        palpite = int(input('Escolha um número entre 1 e 100:\n>>> '))
        print('Você digitou', palpite, '\n')

        if (palpite < 1 or palpite > 100):
            print('Você deve digitar um número entre 1 e 100!\n')
            continue

        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto

        if (numero_secreto == palpite):
            print('Você acertou!')
            print(f'PONTUAÇÃO: {pontos}')
            print('-' * 50)
            break
        else:
            if (maior):
                print('O número escolhido é MAIOR do que o número secreto.')
                print('-' * 50)
            elif (menor):
                print('O número escolhido é MENOR do que o número secreto.')
                print('-' * 50)
            pontos_perdidos = abs(palpite - numero_secreto)
            pontos = pontos - pontos_perdidos
    print('Fim de jogo.')