def jogar():
    print('-'*50)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*50)

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Digite uma letra.\n>>> ")
        chute = chute.strip()


        index = 0 #Index = Posição
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim de jogo.")

if (__name__ == "__main__"):
    jogar()