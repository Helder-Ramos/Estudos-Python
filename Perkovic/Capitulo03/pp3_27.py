'''3.27 Implemente um programa que solicita um inteiro positivo n e exibe na tela todos os divisores
positivos de n. Nota: 0 não é um divisor de qualquer inteiro, e n divide por si mesmo.
>>>
Digite n: 49
1
7
49'''

inteiro = int(input('Digite um inteiro positivo: '))

for i in range(1, inteiro + 1):
    if inteiro % (i) == 0:
        print(i)