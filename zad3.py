# -*- coding: utf-8 -*-
"""
Задача 3. Поиск делителей
Условие: найти первые 5 чисел > 600000, у которых есть делитель,
оканчивающийся на 7, не равный 7 и не равный самому числу.
Для каждого числа вывести само число и наименьший такой делитель.
"""

import math


def find_min_divisor_ending_with_7(n):
    """
    Находит наименьший делитель числа n, который:
    - оканчивается на 7 (последняя цифра 7)
    - не равен 7
    - не равен самому числу n
    
    Возвращает наименьший такой делитель или None, если его нет.
    """
    min_divisor = float('inf')
    
    # Перебираем возможные делители от 1 до корня из n
    # Это оптимально, т.к. делители идут парами
    limit = int(math.sqrt(n))
    
    for i in range(1, limit + 1):
        if n % i == 0:
            # Проверяем делитель i
            if i != 7 and i != n and i % 10 == 7:
                if i < min_divisor:
                    min_divisor = i
            
            # Проверяем парный делитель n // i
            paired = n // i
            if paired != 7 and paired != n and paired % 10 == 7:
                if paired < min_divisor:
                    min_divisor = paired
    
    # Если нашли подходящий делитель — возвращаем его
    if min_divisor != float('inf'):
        return min_divisor
    return None


def solve_task3():
    print("=" * 50)
    print("Задача 3. Поиск делителей")
    print("=" * 50)
    print()
    print("Условие:")
    print("  Найти первые 5 чисел > 600000, у которых есть делитель,")
    print("  оканчивающийся на 7, не равный 7 и не равный самому числу.")
    print("  Вывести число и наименьший такой делитель.")
    print()
    
    results = []           # Список для хранения найденных пар (число, делитель)
    current_number = 600001  # Начинаем с первого числа больше 600000
    
    print("Решение:")
    print("  Выполняем перебор чисел, начиная с 600001...")
    print()
    print("  Найденные числа:")
    print("  " + "-" * 40)
    print("  №  | Число      | Наименьший делитель на 7")
    print("  " + "-" * 40)
    
    # Продолжаем поиск, пока не найдём 5 чисел
    while len(results) < 5:
        divisor = find_min_divisor_ending_with_7(current_number)
        
        if divisor is not None:
            results.append((current_number, divisor))
            print(f"  {len(results)}   | {current_number:10} | {divisor}")
        
        current_number += 1
    
    print("  " + "-" * 40)
    print()
    
    # Вывод в формате, требуемом в условии задачи
    print("Ответ (в требуемом формате):")
    for number, divisor in results:
        print(number)
        print(divisor)
    print()
    
    return results


def main():
    """Демонстрация работы с дополнительными пояснениями"""
    
    # Пример 1: проверка числа 600001
    print("Дополнительно: проверка числа 600001 для наглядности")
    print("-" * 50)
    n = 600001
    print(f"Число: {n}")
    print(f"Делители числа {n}:")
    
    # Выводим все делители для демонстрации
    divisors = []
    limit = int(math.sqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    print(f"  Все делители: {divisors}")
    
    # Находим подходящие делители
    suitable = [d for d in divisors if d != 7 and d != n and d % 10 == 7]
    print(f"  Делители, оканчивающиеся на 7 (кроме 7 и {n}): {suitable}")
    if suitable:
        print(f"  Наименьший из них: {min(suitable)}")
    print()
    print("Теперь запускаем основной алгоритм...")
    print()
    
    # Запускаем основное решение
    solve_task3()


if __name__ == "__main__":
    # Для простого запуска раскомментируйте нужную строку:
    
    # Только вывод ответа в нужном формате:
    solve_task3()
    
    # Или с демонстрацией:
    # main()