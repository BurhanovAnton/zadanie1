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

    #def output_of_answer(self):
        #for answer in self.answers:
            #print (answer)

    def __init__(self, task_id, task, answers):
        self.task_id = task_id
        self.task = task
        self.answers = answers

    # Метод вывода задач
    def output_of_task_of_answers(self):
        print('*' * 50)
        print(self.task)
        print('Выберите номер правильного ответа')
        for answer in self.answers:
            print(f'№{answer.answer_id}. {answer.answer}')


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
                task = Task(task_row['task_id'], task_row['task'], [])
            print(f'№{task.task_id}. {task.task}')
           # print(f'№{task.answers.answer_id}. {task.answers}')
            #print(lesson)

# Метод сериализации ответов
def serialize_answers(file_path):
    with open(file_path, "r", encoding='utf-8') as fl:
        _data = json.load(fl)
        for row in _data:
            for task_row in row['tasks']:
                answer_lesson = Answer([], [], [], task_row['task_id'])
                for answers_row in row['answers']:
                    if answers_row.is_correct == true:
                        Answer.is_correct = True
                    elif answers_row['is_correct'] == false:
                        Answer.is_correct = False
                    answer_lesson = Answer(answers_row['answer_id'], answers_row['answer'], [])
                    #answer_lesson = Answer(answers_row['answer_id'], answers_row['answer'],
                    #                                    answers_row['is_correct'], [])
                print(answer_lesson)








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

#print (task1.get_correct_answer().id)
#print (task2.get_correct_answer().id)
#task1.output_of_tasks()
#task2.output_of_tasks()
'''

for out_lesson in
    print (f'Задача №{task.task_id}. {task.task}')
    for answer in self.answers:
        print('Выберите номер правильного ответа ')
        print(f'№{out_answer.answer_id}. {out_answer.answer}')
    comand = input('Введите номер команды \n')



serialize_data('zadachi.json')
#serialize_answers('zadachi.json')
output_of_task_of_answers