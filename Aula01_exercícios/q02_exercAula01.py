# EXERCÍCIOS AULA O1


## QUESTAO 02
## - Fazer um programa em que o usuário digita o raio de um circunferência e o programa imprime na tela o seu comprimento.

from math import pi

raio = float(input("Digite o raio da circunferência: "))

comprimento = 2 * pi * raio

print("O comprimento do círculo é {:.2f} cm".format(comprimento)) #com somente duas casas decimais (:.2format)

print(f'O comprimento do círculo é {comprimento:.2f}')
