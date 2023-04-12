'''
Considere a lista a seguir como a quantidade de itens vendidos por cada vendedor de uma loja.
vendas = [100, 150, 1500, 2000, 120]
Caso o vendedor tenha vendido mais de 1000 unidades, ele ganha um bônus de 15% sobre seu salário.
Fazer um programa que informa quem conseguiu o bônus.
'''

vendas = [100, 150, 1500, 2000, 120]

for venda in vendas:
  if venda > 1000:        
    print(f'O vendedor {vendas.index(venda) + 1} vendeu R${venda:.2f}, assim ele ganhou o bônus.') 
    
    