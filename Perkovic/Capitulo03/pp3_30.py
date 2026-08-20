'''3.30 Escreva um programa que solicita um inteiro positivo de quatro dígitos do usuário e exibe
seus dígitos. Você não poderá usar as operações do tipo de dados string para realizar essa tarefa.
Seu programa deverá simplesmente ler a entrada como um inteiro e processá-la como um inteiro,
usando as operações aritméticas padrão (+, *, -, /, % etc.).
>>>
Digite n: 1234
1
2
3
4'''

numero = int(input('Digite n: ')) # usei a frase do exemplo, embora achei muito vago. Digite n poderia ser -1.3

for i in range(4,0,-1):
    print(numero // 10**(i-1))
    numero = numero % 10**(i-1)