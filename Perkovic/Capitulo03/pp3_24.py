'''3.24 Implemente um programa que solicite uma lista não vazia do usuário e exiba na tela uma
mensagem mostrando o primeiro e o último elemento da lista.
>>>
Digite uma lista: [3, 5, 7, 9]
O primeiro elemento da lista é 3
O último elemento da lista é 9'''

lista = eval(input('Informe uma lista não vazia (cada item deve ser separado por espaço): '))

print('O primeiro elemento da lista é ', lista[0])
print('O último elemento da lista é ', lista[-1])
