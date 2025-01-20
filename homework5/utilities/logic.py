from random import randint

def guess_the_number(start_capital, attempts, number1, number2):
    capital = start_capital
    secret_number = randint(number1, number2)
    print("Добро пожаловать в игру 'Угадай число'")
    print(f"У вас {capital} монет. У вас {attempts} попыток, чтобы угадать число от {number1} до {number2}")
    attempt = 1

    while attempt <= attempts and capital > 0:
        print(f"\nПопытка {attempt} из {attempts}")
        try:
            bet = int(input("Введите вашу ставку: "))
            if bet > capital or bet <= 0:
                print(f"Ставка должна быть от 1 до {capital}. Попробуйте снова")
                continue

            guess = int(input(f"Угадайте число: "))

            if guess < number1 or guess > number2:
                print(f"Число должно быть от {number1} до {number2}. Попробуйте снова")
                continue

            if guess == secret_number:
                winnings = bet * 2
                capital += winnings
                print(f"Поздравляем! Вы угадали число {secret_number}. Вы выиграли {winnings} монет")
                break
            else:
                capital -= bet
                print(f"Неверно! Загаданное число {'меньше' if guess > secret_number else 'больше'} {guess}")

            if capital <= 0:
                print("У вас закончились монеты")
                break
            elif attempt == attempts:
                print("У вас закончились попытки")

            print(f"Ваш текущий капитал: {capital} монет")
            attempt += 1

        except ValueError:
            print("Пожалуйста, вводите только числа")

    print(f"Игра окончена! Загаданное число было: {secret_number}\n"
          f"Ваш итоговый капитал: {capital} монет. Спасибо за игру!")
