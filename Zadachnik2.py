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

def rd():
    with open("zadachi.json", "r", encoding='utf-8') as fl:
        _data = json.load(fl)
    while True:
        new_data = {
            "title": '',
            "id":'',
            "tasks": []
        }
        tnew = input('Введите новую тему (команда для выхода 0)')
        if tnew == '0':
            break
        new_data["title"] = tnew
        new_data["id"] = get_last_id (_data) + 1
        new_t_id = 1
        while True:
            new_tasks = {
                "id":'',
                "task": '',
                "answers": ''
            }
            znew = input ('Введите задачу(команда для выхода 0)')
            if znew == '0':
                break
            new_tasks["task"] = znew
            onew = input('Введите ответ')
            new_tasks["answers"] = onew
            new_tasks["id"] = new_t_id
            new_t_id = new_t_id+1
            new_data['tasks'].append(new_tasks)
        _data.append(new_data)
    with open("zadachi.json", "w", encoding='utf-8') as fl:
        json.dump(_data,fl,indent=4)
# Функция записи нового задания

def get_last_id (_data):
    n_id = 0
    for i in _data:
        if i['id'] > n_id:
            n_id = i['id']
    return n_id
# Подфункция определения последнего номера задачи функции записи новыз задач


def _osn_code():
    while True:
        comand = input('Введите номер команды \n')
        if comand.lower() == 'help':
            print('Help - вызов списка комманд \n 1- Приступить к решенипю задач '
                  '\n New - Добавить собственное задание в задачник \n  Info - информация '
                  'о задачнике\n Exit - выход'
                  )
        elif comand == '1':
            print('выбери номер темы:')
            opn()
        elif comand == 'new':
            rd()
        elif comand.lower() == 'info':
            print('Данный задачник является тестовым заданием для обучения программирования'
                  ' на языке Python,\n все найденные недочеты и зачечания по данному прилож'
                  'ению можно отправить по\n електронной почте burhanov08@mail.ru'
                  )
        elif comand.lower() == 'exit':
            print('До новых встреч!', name)
            exit()
        elif comand == '':
            print(name, 'Вы ничего не ввели')
        else:
            print(name, '- Вы ввели неизвенстную мне комманду! Или допустили опечатку попробуйте еще раз')


print('Привет, как тебя зовут?')
name = input()
print(name, 'Вы открыли сборник задач по информатике')
print('Для вызова списка комманд введи Help, или укажи известную тебе комманду')
if __name__ == "__main__":
    _osn_code ()
