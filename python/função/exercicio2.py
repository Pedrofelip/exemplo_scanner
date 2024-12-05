'''
Faça uma funçãoque receba como parâmetro o número de lados de um polígono e:-Se o número de lados for igual a 3, escrever TRIÂNGULO.-Se o número de lados for igual a 4, escrever QUADRILÁTERO.-Se o número de lados for igual a 5, escrever PENTÁGONO.-Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO.
'''

def poligono(lados):
    if lados == 3:
        print('triangulo')
    elif lados == 4:
        print('quadrilatero')
    elif lados == 5:
        print('pentagono')
    else:
        print('valor invalido')

lados = int(input('informe a quantidade de lados: '))
poligono(lados)    
