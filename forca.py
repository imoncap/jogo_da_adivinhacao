import random
def jogar():
    print('-'*50)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*50)

    arquivo = open("palavras.txt" ,encoding='utf-8', mode='r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

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
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("\nVocê acertou a palavra!\n")
    else:
        print("\nTentativas esgotadas. Você não conseguiu acertar a palavra :(\n")
    print("Fim de jogo.")

if (__name__ == "__main__"):
    jogar()