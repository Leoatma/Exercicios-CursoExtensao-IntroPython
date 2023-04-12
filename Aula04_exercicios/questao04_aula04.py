'''
Desenvolva uma calculadora de fatorial em que o usuário digita o número e o programa retorna seu fatorial. Exemplo de saída esperada:
4! = 24

Faça uma verificação se o usuário realmente digitou alguma coisa.

'''

userNumber = input("Informe o número para o fatorial: ")

fatorial = 1

if userNumber.isnumeric():
  idxNumber = int(userNumber)
  
  while idxNumber > 1:
    fatorial *= idxNumber
    idxNumber -= 1
    
  print(f'{userNumber}! = {fatorial}.')

else:
  print('Favor, informe um número válido')

    
  

