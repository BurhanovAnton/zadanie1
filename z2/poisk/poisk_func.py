_data = None

def get_last_id (_data):
    n_id = 0
    for i in _data:
        if i['id'] > n_id:
            n_id = i['id']
    return n_id
# Подфункция определения последнего номера задачи функции записи новыз задач

