import json


class Answer:
    answer_id: int
    task_id: int
    answer: str
    is_correct: bool

    def __init__(self, answer_id, task_id, answer, is_correct):
        self.answer_id = answer_id
        self.task_id = task_id
        self.answer = answer
        self.is_correct = is_correct


class Task:
    task_id: int
    task: str
    answers: [Answer]

    def show_answers(self):
        '''Метод вывода всех вариантов ответов'''
        for answer in self.answers:
            print(f'№{answer.answer_id}. {answer.answer}')

    def get_correct_answer(self):
        '''Метод проверки привильности ответа'''
        for answer in self.answers:
            if answer.is_correct:
                return answer

    def __init__(self, task_id, task, answers):
        self.task_id = task_id
        self.task = task
        self.answers = answers


# Класс инициализации урока
class LessonInitialization:
    lesson_id: int
    lesson_anthology: str
    tasks: [Task]

    def __init__(self, lesson_id, lesson_anthology, tasks):
        self.lesson_id = lesson_id
        self.lesson_anthology = lesson_anthology
        self.tasks = tasks

# Класс уровня обучения
class Level:
    topic_id: int
    task_id: int
    appraisal: int

    def __init__(self, topic_id, task_id, appraisal):
        self.topic_id = topic_id
        self.task_id = task_id
        self.appraisal = appraisal

# Класс пользователь
class User:
    id: int
    name: str
    levels: [Level]

    def __init__(self, id, name, levels):
        self.id = id
        self.name = name
        self.levels = levels

"""    def new_user():
        '''Функция записи нового пользователя'''
        user_list = []
        with open(file_path, "a", encoding='utf-8') as fl:
            _data = json.load(fl)
            for row in _data:
                user = User(row['user_id'], row['name'], [])
                for level_row in row['training']:
                    user_training = Level(level_row['topic_id'], level_row['task_id'], level_row['appraisal'])
                    user_list.append(user_training)
                user_list.append(user)
        return user_list"""

"""    def user_authorization(self):
    '''Метод авторизации пользователя'''
        data_authorization=input('Добрый день, вы являетесь авторизованным пользователем нашего курса?')
        if data_authorization.lower() == "нет":
            new_user()
        else:
            Input ('Введите номер вашей записи')"""


def serialize_user(file_path):
    '''Функция сериализации пользователей'''
    user_list = []
    with open(file_path, "r", encoding='utf-8') as fl:
        _data = json.load(fl)
        for row in _data:
            user = User(row['user_id'], row['name'], [])
            for level_row in row['training']:
                user_training = Level(level_row['topic_id'], level_row['task_id'], level_row['appraisal'])
                user_list.append(user_training)
            user_list.append(user)
    return user_list

def serialize_data(file_path):
    '''функция сериализации заданий и ответов'''
    lessons_list = []
    with open(file_path, "r", encoding='utf-8') as fl:
        _data = json.load(fl)
        for row in _data:
            lesson = LessonInitialization(row['topic_id'], row['title'], [])
            for task_row in row['tasks']:
                lesson_task = Task(task_row['task_id'], task_row['task'], [])
                for answers_row in task_row['answers']:
                    lesson_answer = Answer(
                                           answers_row['answer_id'], task_row['task_id'], answers_row['answer'],
                                           bool(answers_row['is_correct'])
                                           )
                    lesson_task.answers.append(lesson_answer)
                lesson.tasks.append(lesson_task)
            lessons_list.append(lesson)
    return lessons_list

def output_user(user: User):
    ''' Функция вывода пользователей'''
    print(f'Зовут {user.name}. Cохранен под номером {user.id}')
    for row in user['training']:
        print('Изучает')
        print(f'тема № {row.topic_id}.Задание № {row.task_id}. Оценка {row.appraisal}')

def output_object(lesson: LessonInitialization):
    ''' Функция вывода урока, заданий и ответов к ним са проверкой'''
    print('*' * 50)
    print(f'Тема №{lesson.lesson_id}. {lesson.lesson_anthology}')
    print('*' * 50)
    for task in lesson.tasks:
        print(f'Задача №{task.task_id}. {task.task}')
        print('-' * 10)
        print('Варианты ответов')
        task.show_answers()
        in_answer = int(input ('Выберите номер правильного ответа '))
        if in_answer == task.get_correct_answer().answer_id:
            print('_' * 40)
            print('Верно')
            print('_' * 40)
        else:
            print('_' * 40)
            print('Не верно')
            print('_' * 40)

lessons_list = serialize_data('zadachi.json')
user_list = serialize_user('users.json')

for user in user_list:
    output_user(user)

for lesson in lessons_list:
   output_object(lesson)