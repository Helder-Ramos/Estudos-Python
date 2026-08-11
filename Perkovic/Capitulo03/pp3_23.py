'''3.23 Implemente um programa que solicita uma lista de nomes de aluno do usuário e exiba
aqueles nomes que começam com as letras de A até M.
>>>
Digite a lista: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
Ellie
Gavin'''

lista = input('Informe a lista de alunos separados por espaço: ').split()

for nome in lista:
    if nome[0].upper() in 'ABCDEFGHIJKLM':
        print(nome)
