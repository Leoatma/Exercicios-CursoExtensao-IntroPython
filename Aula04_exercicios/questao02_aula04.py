'''
Faça um programa de verificação de login e senha. O usuário pode errar a senha até 3 vezes antes do programa terminar informando que o acesso foi bloqueado.
'''

rootLogin = "leoatma"
rootPassword = "minhasenha"

contador = 3

while True:
  user = input("Login: \n").strip() # strip() para cortas espaços acidentais antes ou após a String
  password = input("Senha: \n").strip()
  
  if (user == rootLogin) and (password == rootPassword): 
      print("Acesso permitido.")
      break      
  else:
    contador -= 1
    if contador > 0:       
      print(f'Dados inválidos. Você tem mais {contador} tentativas. \n')
    else:
      print('Tentativas esgotadas. Acesso Bloqueado.')
      break
    
    
  
