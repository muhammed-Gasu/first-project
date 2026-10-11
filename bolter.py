import random

hidden_number = random.randint(1,50)
user_guess = 0
attempts = 0

while user_guess !=hidden_number:
    user_guess = int(input("Введите вашу попытку: "))
    attempts += 1
    if user_guess < hidden_number:
        print("Бери выше!")
    elif user_guess > hidden_number:
        print("Бери нижу!")

    print("Победа за", attempts, "попыток(-ки)!")