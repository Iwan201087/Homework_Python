# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала 
# в два раза больше журавликов, чем Петя и Сережа вместе?
# Введем общее число сделанных детьми журавликов  и преобразуем его в тип int
count = int(input("Введите количество сделаных детьми журавликов: "))
# Выведем результат
print(f"Петя сделал:\t{int(count/6)} журавликов;"+f"\nКатя сделала:\t{int((count/6)*4)} журавликов;"+f"\nСережа сделал:\t{int(count/6)} журавликов;")