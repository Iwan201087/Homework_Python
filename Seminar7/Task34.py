#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке


def word(words):
    poem = words.lower().split()
    rhythm = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    syllable = rhythm(poem[0])
    if all([rhythm(i) == syllable for i in poem]):
        return 'Парам пам-пам'
    return 'Пам парам'

print(word("пара-ра-рам рам-пам-папам па-ра-па-да"))
print(word("Хорошо-живет-на-свете-Винни-Пух!\ Оттого-поет-он-эти-Песни-вслух!"))
print(word("И-не-важно,-чем-он-занят,\ Если-он-худеть-не-станет,"))
print(word("А-ведь-он-худеть-не-станет,\ Если-конечно,-вовремя-подкрепиться - да")) 