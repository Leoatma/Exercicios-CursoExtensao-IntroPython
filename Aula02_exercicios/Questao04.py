'''
É triangulo ou Não é triângulo?
Para determinar se 3 segmentos de reta formam um triângulo, podemos fazer a verificação se a soma dos dois menores segmentos é maior do que o segmento maior.

Segmentos: 2, 3 e 4
Soma dos dois menores: 2 + 3 = 5
Verificação: 5 > 4
Conclusão:Estes segmentos formam um triângulo

'''

lado1 = int(input("Informe o valor do segmento 1: "))
lado2 = int(input("Valor do 2 segmento: "))
lado3 = int(input("3 segmento: "))



if ((lado1 > lado2) and (lado1 > lado3)):
    if ((lado2 + lado3) > lado1):
        print("É triângulo")
    else:
        print("Não é triângulo")
elif ((lado2 > lado1) and (lado2 > lado3)):
    if ((lado1 + lado3) > lado2):
        print("É triângulo")
    else:
        print("Não é triângulo")
else:
    if ((lado1 + lado2) > lado3):
        print("é triângulo")
    else:
        print("Não é triângulo")
