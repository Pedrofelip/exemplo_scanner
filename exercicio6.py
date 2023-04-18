'''
Criar um algoritmo que leia deznúmeros inteiros e informe o maior e o menor número.
'''

numero = int(input('numero: '))
menor = numero
maior = numero

for i in range (9):
    numero = int(input('Numero: '))
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print(f'Menor numero: {menor}')
print(f'Maior numero: {maior}')