#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
# Введем параметры шоколадки, и преобразуем значения в тип int
len = int(input("Введите длину шоколадки: ")) 
wid = int(input("Введите ширину шоколадки: ")) 
count = int(input("Введите нужное количество долек, которые необходимо отломить: ")) 
# Делаем проверку и выводим результат
if count < len * wid and ((count % len == 0) or (count % wid == 0)):
    print("Такое количество долек отломить можно")
else:
    print("Такое количество долек отломить нельзя")