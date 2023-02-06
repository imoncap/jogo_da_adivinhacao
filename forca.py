def jogar():
    print('-'*50)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*50)

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Digite uma letra.\n>>> ")
        chute = chute.strip()


        index = 0 #Index = Posição
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print(f"Encontrei a letra '{chute}' na posição {index}.")
            index = index + 1

    print("Fim de jogo.")

if (__name__ == "__main__"):
    jogar()