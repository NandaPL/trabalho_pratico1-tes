"""
O objetivo é extrair de uma mensagem criptografada um texto oculto onde sabe-se que o padrão adotado para o 
texto oculto é ser formado por letras minúsculas ao contrário (o código da questão foi adaptado pensando em 
outras possíveis situações).
"""


def cryptotext(palavra):
    if palavra and not palavra.isdigit():
        texto_oculto = str()
        count = 0

        nova_palavra = palavra.replace(" ", "")

        for letra in nova_palavra:
            if letra.islower():
                texto_oculto += letra
                count += 1

        if count > 0:
            return print('Texto oculto: ' + texto_oculto[::-1])
        else:
            return print('Sem mensagem oculta')
    else:
        return print('Entrada inválida!')
