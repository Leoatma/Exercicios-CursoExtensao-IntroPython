'''
Meta de vendas: 50.000 unidades.
Usuário vai informar quantas unidades do produto foram vendidas.

Se a meta não for atingida, o programa deverá informar que a meta não foi atingida e ninguém recebe bonus.
Se a meta for atingida com menos de 500 unidades de diferença, o programa informa que a meta foi atingida e que os vendedores ganharão 5% de bonus.
Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%.
'''

unidadesVendidas = int(input("Informe quantas unidades foram vendidas: "))

metaVendas = 50_000

if (unidadesVendidas < metaVendas):
    print("A meta não foi atingida, portanto nenhum funcionário terá bônus.")
elif (unidadesVendidas > metaVendas):
    if (unidadesVendidas - metaVendas <= 500):
        print("Meta alcançada! Cada vendedor receberá 5% de bônus.")
    else:
        print("A meta foi ultrapassada por mais de 500 unidades, 15% de bônus a todos!")