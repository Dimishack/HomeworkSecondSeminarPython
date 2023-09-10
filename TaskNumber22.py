"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

first_list = list()
second_list = list()
print()
n = int(input("Введите количество чисел 1-го набора: "))
print("Введите числа для 1-го набора")
for i in range(n):
    first_list.append(int(input("{} число: ".format(i+1))))
m = int(input("Введите количество чисел 2-го набора: "))
print("Введите числа для 2-го набора")
for i in range(m):
    second_list.append(int(input("{} число: ".format(i+1))))
print("1-ый набор чисел: {}".format(first_list))
print("2-ой набор чисел: {}".format(second_list))
first_list = set(first_list)
second_list = set(second_list)
result = sorted(first_list | second_list)
print("Вывод набора чисел в порядке возрастания (без повторений): {}".format(result))