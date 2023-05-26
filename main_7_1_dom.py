
poem = input('Введите стихотворение ').split() # ввод стихотворения пара-ра-рам рам-пам-папам па-ра-па-да
print (poem)
syllables = [] # список с количеством слогов в каждой фразе
for phrase in poem:
    vowels = [letter for letter in phrase if letter in 'аоиеёэыуюя'] # оставляем только гласные буквы  
    syllables.append(len(vowels)) # определяем число слогов и добавляем в список
if len(set(syllables)) == 1: # если все числа в списке одинаковы
    print('Парам пам-пам')
