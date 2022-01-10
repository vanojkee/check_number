import random


class Psychics:
    '''Модель экстрасенса '''

    def __init__(self):
        name_list = ['Артем', 'Ванга', 'Кассандра', 'Кадони', 'Пахом', 'Алмаз', 'Борман']
        self.name = random.choice(name_list)
        self.psy_answer = 0
        self.trust_level = 0
        self.try_count = 0
        self.all_answer = []

    def potluck(self):
        # Делает попытку угадать загаданное число
        self.psy_answer = random.randint(10, 99)
        self.all_answer.append(self.psy_answer)

    def check_answer(self, user_answer):
        # Проверка ответа
        if user_answer == self.psy_answer:
            self.trust_level += 1
        else:
            self.trust_level -= 1
        self.try_count += 1
