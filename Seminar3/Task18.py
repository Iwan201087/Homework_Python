# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
# Введем количество элементов списка из консоли и преобразуем его в тип int
count_elements = (int(input('Введите количество элементов списка : ')))
# Создадим список my_list и заполним его целыми числами (от 1 до 100) типа int
my_list = [random.randint(0, 100) for _ in range(count_elements)]
# Выведем на экран сформированный список
print(my_list)
# Введем искомое число из консоли и преобразуем его в тип int
number_desired = int(input('Введите заданное число: '))
# Через цикл найдем в списке my_list искомое число number_desired и подсчитаем, сколько раз оно встречается в списке
count = 0
for i in my_list:
    if i == number_desired:
        count += 1
#Создадим переменную close_element и присвоим ей первоначальное значение равное первому элементу списка
close_element = my_list[0]
# Найдем ближайшее к введенному числу number_desired, число из списка my_list 
if count == 0:
    for index in my_list:
        if abs(number_desired-index) < abs(number_desired-close_element):
            close_element = index
#Выведем результат
print(f'Ближайшее по велечине к числу {number_desired} в списке число {close_element}')
