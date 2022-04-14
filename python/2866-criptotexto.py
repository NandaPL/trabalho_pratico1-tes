casos = input()

if casos.isdigit() and not casos == '0':
    while casos:
        casos = int(casos)
        palavra = input()
        texto_oculto = str()
        count = 0

        for letra in palavra:
            if letra.islower():
                texto_oculto += letra
                count += 1

        if count > 0:
            print('Texto oculto: ' + texto_oculto[::-1])
        else:
            print("Mensagem desconhecida")

        casos -= 1
elif casos == '0':
    print('Sem mensagem para descobrir.')
else:
    print("Entrada inválida!")
