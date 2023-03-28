# Fazer um programa em que o usuário entra com um número e o programa imprime na tela seu antecessor e seu sucessor.

userNumber = int(input("Informe um número inteiro: "))

prevNmber = userNumber - 1
nextNmber = userNumber + 1

print("O seu número fica entre {} e {}.".format(prevNmber, nextNmber))