'''
Faça um programa que peça verifica se o usuário digitou um número inteiro.
Caso tenha digitado, mostrar o número na tela.
Caso não tenha digitado, pedir para o usuário digitar novamente.
'''


while True:
  userNumber = input("Favor, digite um número inteiro: ")
  if userNumber.isnumeric():
    print(f'O número digitado foi {userNumber}.')
    break  
  else:
    print("\nPor Favor, verifique se digitou um número inteiro e tente novamente. \n\n")
