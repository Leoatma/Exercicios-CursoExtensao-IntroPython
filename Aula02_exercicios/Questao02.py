# Calculadora do Preço da laranja



qtdeLaranjas = int(input('''
A unidade está custando R$0.3, porém acima de uma dúzia seu valor cai para R$0.25.
Informe, portanto, a quantidade de laranjas que deseja e retornamos o valor total: '''))


if (qtdeLaranjas > 12):
    laranjaUn = 0.25
else:
    laranjaUn = 0.3

valorTotal = float(qtdeLaranjas * laranjaUn)

print("O valor total é de {} reais para {} laranjas".format(valorTotal, qtdeLaranjas))


