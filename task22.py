# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами
# элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

len_n = int(input("Введите количество элементов первого множества: "))
len_m = int(input("Введите количество элементов второго множества: "))

list_1 = {int(input("Введите элемент первого множества: "))
          for i in range(len_n)}
list_2 = {int(input("Введите элемент второго множества: "))
          for i in range(len_m)}

# через преобразовние в список с использованием цикла

result_list = list(list_1.intersection(list_2))
for i in range(len(result_list)-1):
    if result_list[i] > result_list[i+1]:
        result_list[i], result_list[i+1] = result_list[i+1], result_list[i]
print(*result_list)

# через метод для списка
# result_list.sort()
# print(*result_list)

# через метод без преобразования в список
# result_list = list_1.intersection(list_2)
# print(*sorted(result_list))
