'''
Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as suas notas e exiba a sua respectiva média(a média deve ser arredondada para duas casas decimais).
'''

alunos = int(input('Quantidade de alunos: '))
notas = int(input('Quantidade de notas'))

for i in range(alunos):
    soma = 0
    for n in range(notas):
        nota = float(input('Informe a nota: '))
        soma += nota
    media = soma / notas
    print(f'Media: {round(media, 2)}')