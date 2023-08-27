def calculate_bmi(weight, height):
    # Формула для расчёта BMI
    bmi = weight / (height ** 2)
    return bmi


def draw_scale(bmi):
    scale = list("=" * 26)  # создаём шкалу
    position = min(max(int((bmi - 15) / 25 * 26), 0), 25)  # вычисляем позицию риски на шкале
    scale[position] = "|"  # ставим риску соответствующую позицию на шкале
    return "".join(scale)


# Запрос данных у пользователя
weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в метрах: "))

# Расчет BMI и вывод результата
bmi = calculate_bmi(weight, height)
scale = draw_scale(bmi)
print("Ваш BMI равен: {:.2f}".format(bmi))
print(scale)