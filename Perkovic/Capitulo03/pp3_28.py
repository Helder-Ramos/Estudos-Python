'''3.28 Implemente um programa que solicita quatro números (inteiro ou ponto flutuante) do usuário.
Seu programa deverá calcular a média dos três primeiros números e comparar a média com o
quarto número. Se elas forem iguais, seu programa deverá exibir 'Igual' na tela.
>>>
Digite o primeiro número: 4.5
Digite o segundo número: 3
Digite o terceiro número: 3
Digite o quarto número: 3.5
Igual'''

num_1 = eval(input('Digite o primeiro número: '))
num_2 = eval(input('Digite o segundo número: '))
num_3 = eval(input('Digite o terceiro número: '))
num_4 = eval(input('Digite o quarto número: '))

if (num_1 + num_2 + num_3)/3 == num_4:
    print('Igual')

