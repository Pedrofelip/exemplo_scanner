'''
Escreva  um  programa  para solicitaras  notas  de  duas provas.  Faça  umafunçãoque  receba  as  duas notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. Considere 6.0 a média mínima para aprovação.
'''

def aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f'A media foi {media}')
    if media >=6:
        print('Voce foi aprovado')
    else:
        print('Voce foi reprovado')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
aprovacao(nota1, nota2)