'''
Faça uma funçãoque recebeum número inteiro por parâmetro e retorna Truese for par e Falsese for ímpar.
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else: 
        return False

numero = int(input('Numero: '))
if par_ou_impar(numero) == True:
    print('Par')
else:
    print('impar')