"""
1. Реализовать скрипт, в котором должна быть
 предусмотрена функция расчета заработной платы сотрудника. 
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys

def salary(hours=sys.argv[1], rate=sys.argv[2], bonus=sys.argv[3]):
    if len(sys.argv) < 4:
        print('Недостаточно аргументов')
        return
    elif len(sys.argv) > 4:
        print('Слишком много аргументов')
        return
    try:
        print(int(hours) * int(rate) + int(bonus))
    except ValueError:
        print('Ошибка ввода')
        


if __name__ == '__main__':
    salary()