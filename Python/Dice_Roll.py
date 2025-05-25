import random

MAXN = 100
MINN = 0

MAX_ROLLS = 3
MIN_ROLLS = 1


def check_sides():
    while True:
        sides = input(f"Insira o número de lados entre {MINN + 1} e {MAXN}: ")
        try:
            sides = int(sides)
            if sides > MINN and sides <= MAXN:
                return sides
            else:
                print(
                    f"O número deve ser maior que {MINN} e menor ou igual a {MAXN}.")
        except ValueError:
            print("Por favor, insira um número válido.")


cube_sides = check_sides()
print(f"Número de lados: {cube_sides}")


def check_rolls():
    while True:
        try:
            rolls = input(
                f"Insira o número de dados a serem jogados entre ({MIN_ROLLS} - {MAX_ROLLS}): ")
            rolls = int(rolls)
            if rolls > MIN_ROLLS and rolls <= MAX_ROLLS:
                return rolls
            else:
                print(
                    f"O número deve ser maior que {MIN_ROLLS} e menor ou igual a {MAX_ROLLS}")
        except ValueError:
            print("Por favor, insira um número válido.")


roll_count = check_rolls()
print(f"O número de roladas é: {roll_count}.")


def dice_roll():
    rolls = [random.randint(1, cube_sides) for _ in range(roll_count)]
    print(f"Resultados dos {roll_count} dados de {cube_sides} lados: {rolls}")


dice_roll()