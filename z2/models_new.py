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

    def get_correct_answer(self):
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


# Класс пользователь
class User:
    id: int
    name: str
    level: int

    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level

# Метод сериализации
def serialize_data(file_path):
    with open(file_path, "r", encoding='utf-8') as fl:
        _data = json.load(fl)
        for row in _data:
            lesson = LessonInitialization(row['topic_id'], row['title'], [])
            for task_row in row['tasks']:
                lesson_task = Task(task_row['task_id'], task_row['task'], [])
                for answers_row in row['answers']:
                    lesson_answer = Answer(
                                           answers_row['answer_id'], task_row['task_id'], answers_row['answer'],
                                           bool(answers_row['is_correct'])
                                          )
                    print(f'Ответы{lesson_answer.answer_id}. {lesson_answer.task_id}. {lesson_answer.answer}. '
                          f'{lesson_answer.is_correct}.')  # контрольная печать
                print(f'№{lesson_task.task_id}. {lesson_task.task}')  # контрольная печать
            print(f'№{lesson.topic_id}. {lesson.title}') # контрольная печать


def output_object():
    for title in lesson.title:
        print('*' * 50)
        print(f'Тема №{lesson.topic_id}. {lesson.title}')
        for task in lesson_task.task:
            print(f'Задача №{lesson_task.task_id}. {lesson_task.task}')
            print('Варианты ответов')
            for answer in lesson_answer.answer:
                print(f'№{lesson_answer.answer_id}. {lesson_answer.answer}')
            in_answer = input ('Выберите номер правильного ответа ')
            for corect_answer in lesson_answer.is_correct:
                if corect_answer == 'True'
                    if in_answer == lesson_answer.answer_id
                        print('Верно')
                    elif:
                        print ('Не верно')


serialize_data('zadachi.json')
output_object()
