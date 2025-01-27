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


number = np.random.randint(1, 101)      # загадываем число от 1 до 100
print(f'Число {number} угадано за {random_predict(number)} попыток.')