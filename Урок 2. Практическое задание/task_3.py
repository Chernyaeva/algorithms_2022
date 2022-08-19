"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def recurs_number(number, sum=0):
    if number:
        rem = number % 10
        number = number // 10
        return recurs_number(number, sum * 10 + rem )
    else:
        return sum


def recurs_number2(number):     # Чтобы нули в начале перевёрнутого числа отображались, надо его представить в виде строки
    if number:
        rem = number % 10
        number = number // 10
        return str(rem) + recurs_number2(number)
    else:
        return ''


print(recurs_number(1234000))
print(recurs_number2(1234000))
