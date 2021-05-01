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
    with open("zadachi.json", "a",encoding='utf-8') as fl:
       # for i in data:
            #tnew = input('Введите тему')
            json.dump(tnew, fl)






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
