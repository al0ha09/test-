# Функция для переворачивания числа
def reverse_number(n):
    return int(str(n)[::-1])  # Преобразуем число в строку, переворачиваем и обратно в число

# Вводим два числа
N = int(input("Введите первое число: "))
K = int(input("Введите второе число: "))

# Переворачиваем числа
N_reversed = reverse_number(N)
K_reversed = reverse_number(K)

# Выводим результат
print(f"Первое число наоборот: {N_reversed}")
print(f"Второе число наоборот: {K_reversed}")
