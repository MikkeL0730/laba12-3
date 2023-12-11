import numpy as np

def compute_series_sum(x, k, t):
    total = 0.0
    sign = 1
    prev_factorial = 1
    factorial = 1
    term = 0.0
    n = 1

    while True:
        term = (np.abs(x) * sign) / factorial
        total += term
        sign = -sign
        n += 1

        prev_factorial = factorial
        factorial *= (2 * n - 1) * (2 * n)

        if np.abs(term) < 0.1 ** t:
            break

    return total

k = 3
x = np.random.uniform(-1, 1, size=(k, k)) # Генерация случайной матрицы размера k со значениями от -1 до 1
t = 5  # Точность, количество знаков после запятой

sum_result = compute_series_sum(x, k, t)
print("Сумма знакопеременного ряда:", sum_result)
