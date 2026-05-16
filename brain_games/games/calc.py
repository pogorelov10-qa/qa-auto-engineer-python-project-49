"""Игра «Калькулятор»."""

import random

RULE = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def calculate(num1, num2, operator):
    """Вычисляет результат математического выражения."""
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    # Эта ветка не достижима, но на всякий случай
    return None


def get_question_and_answer():
    """Возвращает вопрос и правильный ответ для игры."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(OPERATORS)

    question = f"{num1} {operator} {num2}"
    correct_answer = calculate(num1, num2, operator)

    return question, correct_answer