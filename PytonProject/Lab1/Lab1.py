"""
Спасатель должен добраться до утопающего как можно быстрее. Необходимо преодолеть часть дистанции
по песку, а оставшуюся часть — вплавь. Направление движения определяет общее расстояние, которое
необходимо преодолеть. Скорость движения в воде меньше скорости движения по суше на определённую
постоянную величину. Необходимо написать программу, рассчитывающую время,которое требуется спасателю
для того, чтобы добраться до утопающего.
"""

import math

# Константы для перевода величин друг в друга
J_T_F = 3  # "Jard to foot" - в одном ярде три фута
MH_T_FS = 5280  # "Mills/hour to Foots/sec" - в одном ярде три фута

# Ввести данные для расчета (вручную через консоль или программно через код)
# d1 = int(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды)"))
d1 = 8
# d2 = int(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы)"))
d2 = 10
# h = int(input("Введите боковое смещение между спасателем и утопающим, h (ярды)"))
h = 50
# v_sand = int(input("Введите скорость движения спасателя по песку, v_sand (мили в час)"))
v_sand = 5
# n = int(input("Введите коэффициент замедления спасателя при движении в воде, n"))
n = 2
# θ = float(input("Введите направление движения спасателя по песку, θ (градусы)"))
θ = 39.413

# Промежутоные величины (не для печати)
# Определение тангенса угла направления - Tgθ
Tgθ = math.tan(math.pi * θ / 180)
# print(Tgθ)
# Вертикальное смещения до границы раздела сред - x, (футы)
x = d1 * J_T_F * Tgθ
# print(x)
# Диагональное смещения до границы раздела сред (по песку) - L1, (футы)
L1 = ((d1 * J_T_F) ** 2 + x ** 2) ** 0.5
# print(L1)
# Диагональное смещения от границы раздела сред (по воде) - L2, (футы)
L2 = ((h * J_T_F - x) ** 2 + d2 ** 2) ** 0.5
# print(L2)
# Перевод скорости из миль в час в футы в секунду - v_f_sand
v_f_sand = v_sand * 5280 / (60 * 60)
# print(v_f_sand)

# Определение необходимого времени t, (секунды) c округлением до одного знака
time = round(1 / v_f_sand * (L1 + n * L2), 1)

print("")  # пробел
print("Если спасатель начнёт движение под углом θ =", θ, "градусов, он достигнет утопащего через", time, "секунд.")
