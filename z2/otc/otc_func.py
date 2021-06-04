import json

_data = None


def opn():
    global _data
    with open("zadachi.json", "r",encoding='utf-8') as fl:
        _data = json.load(fl)
        for i in _data:
            print(f"№{i['id']} {i['title']}")
    nt = int (input())
    for i in _data:
        if nt == i['id']:
            for j in i['tasks']:
                print(j['task'])
                ot = input ()
                if ot == j['answers']:
                    print ('Верно')
                else:
                    print('Не верно')
# Функция вывода задания на экран с проверкой ответов