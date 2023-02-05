import forca
import adivinhacao

print('-'*50)
print('Escolha seu jogo!')
print('-'*50)

jogo = int(input('(1) Forca\n(2) Adivinhação\n'))

if (jogo == 1):
    print('Jogando Forca')
    forca.jogar()
elif (jogo == 2):
    print('Jogando Adivinhação')
    adivinhacao.jogar()