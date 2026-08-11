'''3.22 Implemente um programa que solicita uma lista de palavras do usuário e depois exibe cada
palavra na lista que não seja 'segredo'.
>>>
Digite lista de palavras: ['cia', 'segredo', 'mi6', 'isi', 'segredo']
cia
mi6
isi'''

lst = input('Digite uma lista de palavras separadas por um espaço: ').split()

for palavra in lst:
    if palavra != 'segredo':
        print(palavra)

