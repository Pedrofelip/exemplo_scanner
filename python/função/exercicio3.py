'''
Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.
'''

def dobro(num):
   numDobro = num*2
   return numDobro

numero = int(input('adicione um numero: '))
resultado = dobro(numero)
print(f'O dobro de {numero} é {resultado}') 