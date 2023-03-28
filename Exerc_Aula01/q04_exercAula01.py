# Fazer um programa em que o usuário entra com o ano de seu nascimento e o programa imprime na tela sua idade.

import datetime

birthdayYear = int(input("por favor informe o ano do seu nascimento: "))

current_year = datetime.datetime.now()

userAge = current_year.year - birthdayYear

print(userAge)