casos = input()

if casos.isdigit():
    while casos:
        casos = int(casos)
        palavra = input()
        contrario = str()
        count = 0

        for letra in palavra:
            if letra.islower():
                contrario += letra
                count += 1

        if count > 0:
            saida = contrario[::-1]
            print(contrario[::-1])
        else:
            print("Mensagem desconhecida")

        casos -= 1
else:
    print("Entrada inválida!")
