def jogar():
    print('-'*50)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*50)

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Digite uma letra.\n>>> ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0 #Index = Posição
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Que pena, essa letra não existe na palavra secreta!\nVocê ainda tem {(len(palavra_secreta) - erros)} tentativas.\n")
        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("\nVocê acertou a palavra!\n")
    else:
        print("\nTentativas esgotadas. Você não conseguiu acertar a palavra :(\n")
    print("Fim de jogo.")

if (__name__ == "__main__"):
    jogar()