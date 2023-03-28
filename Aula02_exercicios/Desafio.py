'''
DESAFIO

Um posto de gasolina está vendendo combustíveis com a seguinte tabela de descontos:

Gasolina:
Até 20 litros: desconto de 4% por litro
Acima de 20 litros: desconto de 6% por litro

Álcool:
Até 20 litros: desconto de 3% por litro
Acima de 20 litros: desconto de 5% por litro

Escreva um programa que leia o tipo de combustível (A - Álcool e G - Gasolina), calcule e imprima o valor a ser pago pelo cliente.

PARA TORNAR O DESAFIO INTERESSANTE, VAMOS FAZER O PROGRAMA CRIAR UM NÚMERO ALEATÓRIO PARA O ABASTECIMENTO. ESTE NÚMERO DEVERÁ SER ENTRE 1 E 52
'''


from random import randint

tipoCombustivel = input("Olá, qual combustivel você deseja? \nG - Gasolina \nA - Álcool \n")

volCombustivel = randint(1, 52) # gerando numero aleatorio entre 1 e 52



if (tipoCombustivel == 'G'):
    if(volCombustivel <= 20):
        desconto = 0.96
    else:
        desconto = 0.94
elif (tipoCombustivel == "A"):
    if(volCombustivel <= 20):
        desconto = 0.97
    else:
        desconto = 0.95

valorGasolina = (4.50 * desconto) * volCombustivel
valorAlcool = (1.99 * desconto) * volCombustivel

if (tipoCombustivel == 'G'):
    print("O valor total para {} litro(s) será de {} reais".format(volCombustivel, valorGasolina))
else:
    print("O valor total para {} litro(s) será de {} reais".format(volCombustivel, valorAlcool))
