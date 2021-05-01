import json
import random

data = list()
#открытие и запись в Дата
with open("test.json", "r") as tasks:
    data = json.load(tasks)
 print(data)
# проверка на ошибку чтения
if len(data) == 0:
    print('Ошибка чтения файла с задачами')
    exit()

current_type = data[0]
used_tasks = list()
for i in range(len(current_type['tasks'])):
    task_for_print = random.sample(current_type['tasks'], len(current_type['tasks']))[0]
    while task_for_print['id'] in used_tasks:
        task_for_print = random.sample(current_type['tasks'], len(current_type['tasks']))[0]
    print(task_for_print['task'])
    used_tasks.append(task_for_print['id'])

print(current_type['tasks'][0])
used_tasks.append(current_type['tasks'][0])

new_type_task = "Задачи на сложение"
list_tasks = [
    "Сделай раз",
    "Сделай два",
    "Сделай три"
]

print(type(data))

data.append({
    "title": new_type_task,
    "tasks": list_tasks
})

with open("test.json", "w") as tasks:
    json.dump(data, tasks)

