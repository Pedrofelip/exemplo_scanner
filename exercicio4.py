'''
Escreva um algoritmo que leia quinze números informados pelo usuário e exiba a raiz quadrada de cada número (Dica: utilize a biblioteca math)
'''
import math

for n in range(15):
    numero = int(input('numero'))
    resultado = math.sqrt(numero)
    print (f'A raiz quadrada de {numero} é {round(resultado,2)}')