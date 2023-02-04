import random

print('-'*50)
print('Bem vindos(as) ao jogo da adivinhação!')
print('-'*50)

numero_secreto = random.randrange(1, 101)
tentativas = 3

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
        print('-' * 50)
        break
    else:
        if (maior):
            print('O número escolhido é MAIOR do que o número secreto.')
            print('-' * 50)
        elif (menor):
            print('O número escolhido é MENOR do que o número secreto.')
            print('-' * 50)
print('Fim de jogo.')