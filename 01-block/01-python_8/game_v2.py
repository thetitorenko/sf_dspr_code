'''
Игра угадай число (v2).
Компьютер загадывает число и угадывает его
'''

import numpy as np


def random_predict(number: int=1) -> int:
    """Угадываем загаданное число

    Args:
        number (int, optional): Загаданное число. По умолчанию 1.

    Returns:
        int: Число попыток
    """

    count = 0           # счетчик попыток

    while True:
        count += 1

        # предполагаемое число
        pred_number = np.random.randint(1, 101)
        
        if number == pred_number:
            break       # выход из цикла, если угадал

    return count        # возвращаем кол-во попыток


def score_game(random_predict) -> int:
    """Функция подсчета среднего количества попыток угадывания числа
    за 1000 подходов.

    Args:
    random_predict: Функция угадывания числа

    Returns:
        int: Среднее количество попыток
    """

    count_lst = []          # список количества попыток
    np.random.seed(42)      # фиксируем seed для воспроизводимости

    # Создаем список чисел от 1 до 100 размером 1000
    random_array = np.random. randint(1, 101, size=1000)

    for number in random_array:
        count_lst.append(random_predict(number))

    score = int(np.mean(count_lst))

    print(f'Алгоритм в среднем угадывает число за {score} попыток.')

    return score


# Точка вход в программу
if __name__ == '__main__':
    # Запускаем игру 1000 раз, чтобы узнать среднее количество попыток
    score_game(random_predict)