"""Игра «Арифметическая прогрессия»."""

import random

RULE = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression():
    """Генерирует арифметическую прогрессию со скрытым элементом."""
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)

    # Генерируем прогрессию
    progression = [start + i * step for i in range(length)]

    # Выбираем случайный индекс для скрытия
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    # Заменяем элемент на '..'
    progression[hidden_index] = '..'

    # Формируем строку вопроса
    question = ' '.join(str(x) for x in progression)

    return question, correct_answer


def get_question_and_answer():
    """Возвращает вопрос и правильный ответ для игры."""
    return generate_progression()