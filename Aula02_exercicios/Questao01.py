# Escreva um programa que recebe 2 valores e devolve o maior entre eles.

numero_1 = int(input("Informe o primeiro número"))

numero_2 = int(input("Agora o segundo número"))

if (numero_1 > numero_2):
    print("o numero {} é maior que o numero {}".format(numero_1, numero_2))
elif (numero_2 > numero_1):
    print("O numero {} é maior que o {}".format(numero_2, numero_1))
else:
    print("Os numeros são iguais")