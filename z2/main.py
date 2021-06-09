from otc.otc_func import opn
# Функция открытия файла нового задания

from zap.zap_func import rd
# Функция записи нового задания

from poisk.poisk_func import get_last_id
# Подфункция определения последнего номера задачи функции записи новыз задач

#from osn.osn_func import _osn_code
def main():
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
#  Функция выполнения основного кода



if __name__ == "__main__":
    print('Привет, как тебя зовут?')
    name = input()
    print(name, 'Вы открыли сборник задач по информатике')
    print('Для вызова списка комманд введи Help, или укажи известную тебе комманду')
    main()
