'''
Código para rolagem de dados, para jogar rpg com os amigo durante a pandemia.
'''


from random import randint

while(True):
    numero = int(input('Qual a quantidade de faces do dado: '))
    dado = randint(1, numero)
    
    if dado >= 1:
        print(dado)
    else:
        print('Informação incorreta! Tente novamnte!')

    continuar = input('Digite S para continuar ou N para sair: ')
    if continuar == 'N' or continuar == 'n':
        break