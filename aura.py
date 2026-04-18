import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    chute = int(input("Adivinha (1 a 10): "))

    if chute == numero_secreto:
        print("Acertou seu gay do caralho")
        break
    elif chute < numero_secreto:
        print("Muito baixo")
    else:
        print("Muito alto")

    tentativas -= 1
    print("Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Perdeu kkk era", numero_secreto)
