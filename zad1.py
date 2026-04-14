
def solve_task1():
    print("=" * 50)
    print("Задача 1. Кодовые слова")
    print("=" * 50)
    print()
    print("Условие:")
    print("  Алфавит: Ш, К, О, Л, А (всего 5 букв)")
    print("  Длина слова: 3 буквы")
    print("  Ограничение: буква 'К' встречается ровно 1 раз")
    print("  Остальные буквы (Ш, О, Л, А) — любое количество раз")
    print()
    
    # Решение
    # Буква К может стоять на одной из 3 позиций: 3 варианта
    positions_for_K = 3
    
    # На каждой из оставшихся двух позиций может быть любая из 4 букв (Ш, О, Л, А)
    # Количество вариантов для каждой позиции = 4
    variants_per_position = 4
    
    # Общее количество по правилу произведения:
    total_words = positions_for_K * variants_per_position * variants_per_position
    
    print("Решение:")
    print(f"  1) Буква 'К' может занимать одну из {positions_for_K} позиций в слове")
    print(f"  2) На каждой из оставшихся 2 позиций может быть любая из {variants_per_position} букв (Ш, О, Л, А)")
    print(f"  3) По правилу произведения: {positions_for_K} × {variants_per_position} × {variants_per_position} = {total_words}")
    print()
    print(f"Ответ: {total_words} кодовых слов")
    print()
    
    return total_words


if __name__ == "__main__":
    solve_task1()