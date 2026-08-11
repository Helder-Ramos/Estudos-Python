'''3.26 Implemente um programa que solicita um inteiro n do usuário e imprime na tela os
quadrados de todos os números de 0 até, mas não incluindo, n.
>>>
Digite n: 4
0
1
4
9'''

inteiro = int(input('Digite um inteiro positivo: '))

for i in range(inteiro):
    print(i**2)
