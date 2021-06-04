import json

_data = None


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