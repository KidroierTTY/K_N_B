import time as ti
from random import randint

print("Привет! Это КНБ")
ti.sleep(1)
print("КНБ-это игра про (камень, ножницы, бумага) а точнее это она и есть! Начнем?")

while True:
    n = randint(1, 3)

    ti.sleep(1)

    print("Я выбрал а ты?")

    visor = input("Выбирай из (К/Н/Б): ")

    visor = visor.lower()

    ti.sleep(1)

    print("Молодец просчитываю кто выиграл)")

    if visor == "к" or visor == "н" or visor == "б":
        if n == 1:
            if visor == str("к"):
                print("Я выбрал тоже самое что и ты (К/К)")

            elif visor == str("н"):
                print("Я выиграл! (К/Н)")

            elif visor == str("б"):
                print("Вы выиграли! (К/Б)")

        elif n == 2:
            if visor == str("к"):
                print("Вы выиграли! (Н/К)")

            elif visor == str("н"):
                print("Я выбрал тоже самое что и ты (Н/Н)")

            elif visor == str("б"):
                print("Я выиграл! (Н/Б)")

        elif n == 3:
            if visor == str("к"):
                print("Я выиграл! (Б/К)")

            elif visor == str("н"):
                print("Вы выиграли! (Б/Н)")

            elif visor == str("б"):
                print("Я выбрал тоже самое что и ты (Б/Б)")

    elif visor != "к" or visor != "н" or visor != "б":
        print("Вы выбрали не правильный символ!!!")

    ti.sleep(0.5)

    print("Хорошо поиграли, заново!!")
