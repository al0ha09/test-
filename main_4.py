# Функция для подсчёта количества цифр в числе
def count_numbers(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


# Функция для изменения числа (меняет местами первую и последнюю цифры)
def change_number(number):
    num_count = count_numbers(number)
    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    # Меняем первую и последнюю цифры местами
    new_number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return new_number


# Основная функция программы
def main():
    # Вводим первое число и проверяем его
    first_n = int(input("Введите первое число: "))
    if count_numbers(first_n) < 3:
        print("В первом числе меньше трёх цифр.")
        return

    first_n = change_number(first_n)
    print('Изменённое первое число:', first_n)

    # Вводим второе число и проверяем его
    second_n = int(input("\nВведите второе число: "))
    if count_numbers(second_n) < 4:
        print("Во втором числе меньше четырёх цифр.")
        return

    second_n = change_number(second_n)
    print('Изменённое второе число:', second_n)

    # Выводим сумму
    print('\nСумма чисел:', first_n + second_n)


# Запускаем программу
main()
