# TODO решите задачу
import json # подключаем библиотеку json
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f: # открываем и читаем файл json
        data=json.load(f) # сохраняем в переменную
    t=0 # переменная для суммы
    for item in data: # проходим по каждому словарю
            score=item['score'] # получаем значение по ключу score
            weight=item['weight'] # получаем значение по ключу weight
            pr=score*weight # вычисляем произведение
            t=t+pr # добавляем к сумме
            r=round(t,3) # округление до трех знаков
    return r # возвращаем рузультат


print(task()) # печатаем результат
