'''
Crie um programa que apagará todos os espaços de um texto.
'''

userMessage = input('Digite sua mensagem: ')

for caracter in userMessage:
  if caracter == " ":
    continue
  else:
    print(caracter, end = '') # o end = altera o comportamento do print, que por padrao inclui uma quebra de linha(\n) ao final, assim substituímos este valor por aquele que desejarmos.
    