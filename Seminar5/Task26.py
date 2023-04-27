#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.#

def degree (base, exponent):
    if exponent == 1:
        return base
    return base * degree(base, exponent - 1)
num = degree(int(input('Введите основание степени: ')), int(input('Введите показатель степени: ')))
print(f'Ответ: {num}')