# Функция для подсчёта количества колебаний
def count_oscillations(initial_amplitude, stop_amplitude):
    count = 0
    current_amplitude = initial_amplitude

    # Пока амплитуда больше конечной, уменьшаем её и увеличиваем счётчик
    while current_amplitude > stop_amplitude:
        current_amplitude *= 0.916  # Амплитуда уменьшается на 8.4%
        count += 1  # Увеличиваем счётчик колебаний

    return count


# Основная функция программы
def main():
    try:
        # Ввод данных
        initial_amplitude = float(input("Введите начальную амплитуду: "))
        stop_amplitude = float(input("Введите амплитуду остановки: "))

        # Проверка на корректность ввода
        if initial_amplitude <= 0 or stop_amplitude <= 0:
            print("Амплитуды должны быть положительными числами.")
            return
        if initial_amplitude <= stop_amplitude:
            print("Начальная амплитуда должна быть больше амплитуды остановки.")
            return

        # Подсчитываем количество колебаний
        oscillations = count_oscillations(initial_amplitude, stop_amplitude)

        # Выводим результат
        print(f"Маятник считается остановившимся через {oscillations} колебаний.")

    except ValueError:
        print("Введены неверные данные. Пожалуйста, вводите числа.")


# Запуск программы
main()
