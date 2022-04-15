def main(palavra):
    if not palavra.isdigit():
        texto_oculto = str()
        count = 0

        for letra in palavra:
            if letra.islower():
                texto_oculto += letra
                count += 1

        if count > 0:
            print('Texto oculto: ' + texto_oculto[::-1])
        else:
            print('Sem mensagem oculta')
    else:
        print('Entrada inválida!')


casos = int(input())

for i in range(0, casos):
    palavra = input('Informe a mensagem: ')
    main(palavra)
