def main(casos, palavras):
    if casos.isdigit() and not casos == '0':
        casos = int(casos)

        if casos > 1:
            for palavra in range(len(palavras)):
                texto_oculto = str()
                count = 0

                for letra in palavras[palavra]:
                    if letra.islower():
                        texto_oculto += letra
                        count += 1

                if count > 0:
                    print('Texto oculto: ' + texto_oculto[::-1])
                else:
                    print('Sem mensagem oculta')
        else:
            c = 0
            texto_escondido = str()

            for l in palavras:
                if l.islower():
                    texto_escondido += l
                    c += 1

            if c > 0:
                print('Texto oculto: ' + texto_escondido[::-1])
            else:
                print('Sem mensagem oculta')

    elif casos == '0':
        print('Sem mensagem para ser descoberta.')
    else:
        print("Entrada inválida!")
