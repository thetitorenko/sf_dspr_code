'''Игра угадай число'''

import numpy as np


number = np.random.randint(1, 101)      # загадали число от 1 до 100
count = 0                               # счетчик попыток

while True:
    count += 1

    # предполагаемое число
    pred_number = int(input('Угадай число от 1 до 100: '))   

    if pred_number > number:
        print('Число должно быть меньше!')

    elif pred_number < number:
        print('Число должно быть больше!')

    else:
        print(f'Вы угадали число за {count} попыток! Это число {number}.')
        break  # выход из цикла, если угадали                                              