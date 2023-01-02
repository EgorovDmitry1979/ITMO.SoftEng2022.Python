# Импортируем модуль random для формирования случайных чисел
import random

# Чтобы каждый раз не задавать значения вручную задаю две условные переменные:
Global = 1000  # будет определять размеры М, K и N для матриц A и B (пусть А и Б будут квадратными)
Interval = 1000  # будет определять интервал для случайного выбора числовых значений полей матрицы

# Формируем матрицу A размером M x K
print("")
print("Введите размерность М матрицы A")
# M = int(input('M = '))
M = Global
print(M)
print("Введите размерность K матрицы A")
# K = int(input('K = '))
K = Global
print(K)

matrixA = []

for row in range(1, M + 1):
    matrixA.append([])
    for col in range(1, K + 1):
        matrixA[row - 1].append(random.randint(1, Interval))

print(matrixA)

# Создание файла csv
file = open('MatrixA.csv', "w")

# запись матрицы в файл csv
count = 0

for row in matrixA:
    count = 0
    for cell in row:
        count += 1
        file.write(str(cell))
        if count < len(row):
            file.write(",")
    file.write("\n")
