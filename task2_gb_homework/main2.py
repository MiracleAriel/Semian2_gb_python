# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def calculate_fraction_operations(fraction1, fraction2):
    # Разделение строк на числитель и знаменатель
    numerator1, denominator1 = fraction1.split('/')
    numerator2, denominator2 = fraction2.split('/')

    # Преобразование строк в тип Fraction
    fraction1 = Fraction(int(numerator1), int(denominator1))
    fraction2 = Fraction(int(numerator2), int(denominator2))

    # Вычисление суммы и произведения дробей
    sum_fraction = fraction1 + fraction2
    product_fraction = fraction1 * fraction2

    return sum_fraction, product_fraction

# Получение двух дробей от пользователя
fraction1_input = input("Введите первую дробь в формате a/b: ")
fraction2_input = input("Введите вторую дробь в формате a/b: ")

# Вычисление суммы и произведения дробей
sum_result, product_result = calculate_fraction_operations(fraction1_input, fraction2_input)

# Вывод результатов
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)
