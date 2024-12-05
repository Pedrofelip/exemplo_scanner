'''
Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) e o sexo ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, sendo que:Peso Ideal (para homens) = (72.7 * altura) -58Peso Ideal (para mulheres) = (62.1 * altura) -44.7
'''

def peso_ideal(altura, sexo): 
    if sexo == "M":
        return (72.7 * altura) - 58
    elif sexo == "F":
        return(62.1 * altura) - 44.7
    else: 
        print('Valor invalido')

altura = float(input('Informe a altura: '))
sexo = input('Informe o sexo (M/F): ')

print(f'O peso seu ideal é {peso_ideal(altura, sexo.upper())}')