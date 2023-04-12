'''
Fazer uma calculadora em que o usuário digita Altura em metros e Peso em quilos
 e se é do sexo biológico Masculino ou Feminino. O programa devolve ao usuário
 a informação qual seu peso ideal e quando precisa emagrecer para chegar lá.
 Ao final, o programa deve trazer uma frase motivadora para aqueles que estão acima do peso,
 frase parabenizando os que estão no peso ideal e uma outra frase de alerta aos que estão
 abaixo do peso.

 *Fórmulas*
    >Masculino: (72.7 * Altura) - 50
    >Feminino: (62.1 * Altura) - 44.7

'''

altura = float(input("Informe a sua altura em metros: "))
peso = float(input("Agora, informe o seu peso: "))
sexo = input('''Qual o seu sexo? 
                    M = Masculino
                    F = Feminino \n''').lower()

if sexo == 'm':
    pesoIdeal = (72.7 * altura) - 50
elif sexo == 'f':
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("favor reveja sua resposta")

if (peso > pesoIdeal):
    pesoAPerder = peso - pesoIdeal
    print("Olá o seu peso ideal é de {}Kg, para chegar lá você precisa perder {}Kg.\nVamos lá, você consegue!".format(
        pesoIdeal, pesoAPerder))
elif (peso < pesoIdeal):
    print("Atenção, você está abaixo do peso ideal que é {} kg, se alimente melhor!".format(pesoIdeal))
else:
    print("Parabéns, você tem o peso ideal!")
