points = int(input("Введите количество баллов: "))

if points >= 85:
    print("Отлично")
elif points >= 70:
    print("Хорошо")
elif points >= 50:
    print("Удовлетворительно")
else:
     print("Плохо")