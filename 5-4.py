category = str(input('Введите категорию товара '))
summa = int(input('Введите цену товара '))
if category == 'Продукты':
    if summa < 100:
        print('Купите выпечку ')
    elif 100 <= summa < 500:
        print('Купите орехи в шоколаде ')
    else:
        print('Купите фрукты ')
else:
    print('Идите в товары для дома ')