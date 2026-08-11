'''3.25 Implemente um programa que solicita um inteiro positivo n do usuário e exiba os quatro
primeiros múltiplos de n:
>>>
Digite n: 5
0
5
10
15'''

inteiro = int(input('Digite um inteiro positivo: '))

for i in range(4):
    print(inteiro * i)
