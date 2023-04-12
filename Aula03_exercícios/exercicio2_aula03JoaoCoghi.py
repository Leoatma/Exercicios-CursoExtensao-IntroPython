'''
Uma loja possui 2 produtos: caixa de som e caneca.

A caixa de som custa 150,00 reais.
A caneca custa 30,00 reais.
Os custos fixos da loja são de 2100 reais.

Calcule o faturamento desta loja e se obteve lucro ou prejuízo. O usuário irá informar quantas canecas e quantas caixas de som foram vendidas no período.
'''

preco_caixaSom = 150
preco_caneca = 30
custos_fixos = 2100


qtdeCanecasVend = int(input("Quantidade de canecas vendidas: "))
qtdeCxaSomVend = int(input("Quantidade de caixas de som vendidas: "))

faturamentoCanecas = qtdeCanecasVend * preco_caneca
faturamentoCxaSom = qtdeCxaSomVend * preco_caixaSom

faturamentoPeriodo = (faturamentoCanecas + faturamentoCxaSom) - custos_fixos

if (faturamentoPeriodo < 0):
    print(f'Prejuízo de {faturamentoPeriodo:.2f} reais')
elif (faturamentoPeriodo > 0):
    print(f'Lucro de {faturamentoPeriodo} reais')
else:
    print("Não houve lucro nem prejuízo")