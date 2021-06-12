import json


class Answer:
    id: int
    task_id: int
    answer: str
    is_correct: bool

    def __init__(self, id, task_id, answer, is_correct):
        self.id = id
        self.task_id = task_id
        self.answer = answer
        self.is_correct = is_correct

class Task:
    id: int
    task: str
    answers: [Answer]

    def get_correct_answer(self):
        for answer in self.answers:
            if answer.is_correct:
                return answer

    #def output_of_answer(self):
        #for answer in self.answers:
            #print (answer)

    def __init__(self, id, task, answers):
        self.id = id
        self.task = task
        self.answers = answers

    # Метод вывода задач
    def output_of_task_of_answers(self):
        print('*' * 50)
        print(self.task)
        print('Выберите номер правильного ответа')
        for answer in self.answers:
            print(f'№{answer.id}. {answer.answer}')


# Класс инициализации урока
class LessonInitialization:
    lesson_id: int
    lesson_anthology: str
    tasks: [Task]

    def __init__(self, lesson_id, lesson_anthology, tasks):
        self.lesson_id = lesson_id
        self.lesson_anthology = lesson_anthology
        self.tasks = tasks


# Класс пользователь
class User:
    id: int
    name: str
    level: int

    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level


def serialize_data(file_path):
    with open(file_path, "r", encoding='utf-8') as fl:
        _data = json.load(fl)
        for row in _data:
            lesson = LessonInitialization(row['id'], row['title'], [])
            for task_row in row['tasks']:
                task = Task(task_row['id'], task_row['task'], [])
            print(lesson)

serialize_data('zadachi.json')

'''

answer1 = Answer (1, 1, '1 ot', False)
answer2 = Answer (2, 1, '2 ot', False)
answer3 = Answer (3, 1, '3 ot', True)
answer4 = Answer (4, 1, '4 ot', False)

task1 = Task(1, 'zadacha1', [answer1, answer2, answer3, answer4])

answer1 = Answer (1, 2, '1 ot', False)
answer2 = Answer (2, 2, '2 ot', True)
answer3 = Answer (3, 2, '3 ot', False)
answer4 = Answer (4, 2, '4 ot', False)

task2 = Task(2, 'zadacha2', [answer1, answer2, answer3, answer4])

print (task1.get_correct_answer().id)
print (task2.get_correct_answer().id)
task1.output_of_tasks()
task2.output_of_tasks()'''