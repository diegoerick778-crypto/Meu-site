import random

while True:
    numero_secreto = random.randint(1, 10)
    tentativas = 3

    while tentativas > 0:
        chute = int(input("Adivinha (1 a 10): "))

        if chute == numero_secreto:
            print("Acerto seu filha da puta")
            break
        elif chute < numero_secreto:
            print("Muito baixo")
        else:
            print("Muito alto")

        tentativas -= 1
        print("Tentativas:", tentativas)

    if tentativas == 0:
        print("Perdeu, era", numero_secreto)

    jogar = input("Quer jogar de novo? (s/n): ")
    if jogar != "s":
        break
