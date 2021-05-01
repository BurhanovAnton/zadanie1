import json

# with open("zadachi.json", "w") as fl:
# data = json.load(fl)
data = None


def opn():
    global data
    with open("zadachi.json", "r",encoding='utf-8') as fl:
        data = json.load(fl)
        for i in data:
            print(f"№{i['id']} {i['title']}")
    nt = int (input())
    for i in data:
        if nt == i['id']:
            for j in i['tasks']:
                print(j['task'])
                ot = input ()
                if ot == j['answers']:
                    print ('Верно')
                else:
                    print('Не верно')




def rd():
    with open("zadachi.json", "r", encoding='utf-8') as fl:
        data = json.load(fl)



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
        new_data["id"] = get_last_id (data) + 1
        while True:
            new_tasks = {
                "task": '',
                "answers": ''
            }
            znew = input ('Введите задачу(команда для выхода 0)')
            if znew == '0':
                break
            new_tasks["task"] = znew
            onew = input('Введите ответ')
            new_tasks["answers"] = onew
            new_data['tasks'].append(new_tasks)
        data.append(new_data)
    with open("zadachi.json", "w", encoding='utf-8') as fl:
        json.dump(data,fl,indent=4)


def get_last_id (data):
    n_id = 0
    for i in data:
        if i['id']>n_id:
            n_id=i['id']
    return n_id



print('Привет, как тебя зовут?')
Name = input()
print(Name, 'Вы открыли сборник задач по информатике')
print('Для вызова списка комманд введи Help, или укажи известную тебе комманду')

while True:
    comand = input('Введите номер команды \n')
    if comand.lower() == 'help':
        print(
            'Help - вызов списка комманд \n 1- Приступить к решенипю задач \n New - Добавить собственное задание в задачник \n  Info - информация о задачнике\n Exit - выход')
        #comand = input()
    elif comand == '1':
        print ('выбери номер темы:')
        opn()
    elif comand == 'new':
        rd()
    # elif comand == '3':

    elif comand.lower() == 'info':
        print(
            'Данный задачник является тестовым заданием для обучения программирования на языке Python,\n все найденные недочеты и зачечания по данному приложению можно отправить по\n електронной почте burhanov08@mail.ru')
        #comand = input()
    elif comand.lower() == 'exit':
        print('До новых встреч!', Name)
        exit()
    elif comand == '':
        print(Name, 'Вы ничего не ввели')
        #comand = input()
    else:
        print(Name, '- Вы ввели неизвенстную мне комманду! Или допустили опечатку попробуйте еще раз')
       # comand = input()
