# TODO импортировать необходимые молули
import csv # подключаем библиотеку csf
import json # подключаем библиотеку json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME,'r',encoding='utf-8') as csvfile: # открываем и читаем файл csv
        csvreader = csv.DictReader(csvfile, delimiter=',',lineterminator='\n') # используем разделитель ',' и строки разделены '\n'
        data=[] # создаем пустой список для данных
        for row in csvreader: # перебираем строки из csv файла
            data.append(row) # добавляем строку в список
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME,'w',encoding='utf-8') as jsonfile: # открываем json файл для записи
        json.dump(data, jsonfile, indent=4, ensure_ascii=False) # сохраняем данные в json файл

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f: # открываем json файл
        for line in output_f: # перебираем каждую строку в файле
            print(line, end="") # печатаем строку на экран
