'''
Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada areaque  calcula  e  retorna  a  área  do  círculo  e  outra  função  chamada perimetroque  calcula  e  retorna  o perímetro docírculo.Utilize as fórmulas abaixo
Área = π * r2
Perímetro = π * 2 * r
'''

import math

def area (r):
    return math.pi * r**2

def perimetro(r):
    return math.pi* 2* r

raio = float(input('Informe o raio do circulo: '))

print(f'Area do circulo: {area(raio)}')
print(f'perimetro do circulo: {perimetro(raio)}')