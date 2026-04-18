import random

numero_secreto = random.randint(1, 10)

chute = int(input("Adivinha o número de 1 a 10: "))

if chute == numero_secreto:
    print("Acertou, miserável 😎")
else:
    print("Errou kkk era", numero_secreto)
