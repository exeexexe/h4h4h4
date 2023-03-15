def mark_test(otm):
    return otm > 50
rez = int(input("Сколько учеников? "))
for i in range(rez):
    otmm = int(input("Сколько баллов "))
    result = mark_test(otmm)
    if result:
        print("Ура вы остаетесь")
    else:
        print("Bye-Bye")