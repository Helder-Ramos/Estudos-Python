'''3.29 Implemente um programa que solicita ao usuário que entre com as coordenadas x e y (cada
um entre –10 e 10) de um dardo e calcula se o dardo atingiu o alvo, um círculo com centro (0,0)
e raio 8. Se tiver atingido, a string Está dentro! deverá ser exibida na tela.
>>>
Digite x: 2.5
Digite y: 4
Está dentro!'''

from math import sqrt

raio = 8

coord_x = float(input('Digite x: '))
coord_y = float(input('Digite y: '))

ponto = sqrt(coord_x**2 + coord_y**2)

if ponto <= raio:
    print('Está dentro!')
