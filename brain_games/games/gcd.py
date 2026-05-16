"""Игра «Наибольший общий делитель (НОД)»."""

import random

RULE = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Возвращает наибольший общий делитель чисел a и b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def get_question_and_answer():
    """Возвращает вопрос и правильный ответ для игры."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer