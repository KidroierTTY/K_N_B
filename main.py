import time as ti
from random import randint

print("Привет! Это КНБ")
ti.sleep(1)
print("КНБ-это игра про (камень, ножницы, бумага) а точнее это она и есть! Начнем?")

while True:
    n = randint(1, 3)

    ti.sleep(1)

    print("Я выбрал а ты?")

    vibor = input("Выбирай из (К/Н/Б): ")

    vibor = vibor.lower()

    ti.sleep(1)

    print("Молодец просчитываю кто выиграл)")

    if vibor == "к" or vibor == "н" or vibor == "б":
        if n == 1:
            if vibor == str("к"):
                print("Я выбрал тоже самое что и ты (К/К)")

            elif vibor == str("н"):
                print("Я выиграл! (К/Н)")

            elif vibor == str("б"):
                print("Вы выиграли! (К/Б)")

        elif n == 2:
            if vibor == str("к"):
                print("Вы выиграли! (Н/К)")

            elif vibor == str("н"):
                print("Я выбрал тоже самое что и ты (Н/Н)")

            elif vibor == str("б"):
                print("Я выиграл! (Н/Б)")

        elif n == 3:
            if vibor == str("к"):
                print("Я выиграл! (Б/К)")

            elif vibor == str("н"):
                print("Вы выиграли! (Б/Н)")

            elif vibor == str("б"):
                print("Я выбрал тоже самое что и ты (Б/Б)")

    elif vibor != "к" or vibor != "н" or vibor != "б":
        print("Вы выбрали не правильный символ!!!")

    ti.sleep(0.5)

    print("Хорошо поиграли, заново!!")
