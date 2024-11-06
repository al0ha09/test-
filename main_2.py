# Функция для нахождения максимума из двух чисел
def maximum_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# Функция для нахождения максимума из трёх чисел
def maximum_of_three(a, b, c):
    # Сначала находим максимум между первыми двумя числами
    max_of_first_two = maximum_of_two(a, b)
    # Затем находим максимум из полученного значения и третьего числа
    return maximum_of_two(max_of_first_two, c)

# Вводим три числа
x = float(input("Введите число: "))
y = float(input("Введите число: "))
z = float(input("Введите число: "))

# Находим максимум из трёх чисел
max_number = maximum_of_three(x, y, z)

# Выводим результат
print(f"Самое большое число: {max_number}")
