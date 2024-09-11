import time as ti
from random import randint

print("Привет! Это КНБ")
ti.sleep(1)
print("КНБ-это игра про (камень, ножницы, бумага) а точнее это она и есть! Начнем?")

while True:
    n = randint(1, 3)

    ti.sleep(1)

    print("Я выбрал а ты?")

    vibor = str(input("Выбирай из (К/Н/Б):"))

    vibor.lower()

    ti.sleep(1)

    print("Молодец просчитываю кто выиграл)")

    if n == 1:
        if vibor == "к":
            print("Я выбрал тоже самое что и ты (К/К)")

        elif vibor == "н":
            print("Я выиграл! (К/Н)")

        elif vibor == "б":
            print("Вы выиграли! (К/Б)")

        else:

            print("Вы выбрали не правильный символ!!!")

    elif n == 2:
        if vibor == "к":
            print("Вы выиграли! (Н/К)")

        elif vibor == "н":
            print("Я выбрал тоже самое что и ты (Н/Н)")

        elif vibor == "б":
            print("Я выиграл! (Н/Б)")

        else:
            print("Вы выбрали не правильный символ!!!")

    elif n == 3:
        if vibor == "к":
            print("Я выиграл! (Б/К)")

        elif vibor == "н":
            print("Вы выиграли! (Б/Н)")

        elif vibor == "б":
            print("Я выбрал тоже самое что и ты (Б/Б)")

        else:
            print("Вы выбрали не правильный символ!!!")

    ti.sleep(0.5)

    print("Хорошо поиграли, заново!!")