"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""

def set_discount():
    mark = int(input("Баллы (0-завершить): "))
    while mark != 0:
        if mark >= 1 and mark <= 49:
            return 10
        elif mark >= 50 and mark <= 99:
            return 15
        elif mark == 100:
            return 20
        else:
            return 0

print("Ваша скидка: ", set_discount(), "%")


