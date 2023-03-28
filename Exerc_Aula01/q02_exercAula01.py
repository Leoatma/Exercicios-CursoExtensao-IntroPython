# EXERCÍCIOS AULA O1


## QUESTAO 02
## - Fazer um programa em que o usuário digita o raio de um circunferência e o programa imprime na tela o seu comprimento.

import math

raio = int(input("Digite o raio da circunferência: "))

comprimento = 2 * math.pi * raio

print("O comprimento do círculo é {} cm".format(comprimento))
