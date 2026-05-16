#!/usr/bin/env python3
"""Игра «Проверка на чётность»."""

import random
from brain_games.cli import welcome_user


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def run_game():
    """Запускает игру «Проверка на чётность»."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ').strip().lower()

        is_correct = (answer == 'yes' and is_even(number)) or \
                     (answer == 'no' and not is_even(number))

        if not is_correct:
            correct_answer = 'yes' if is_even(number) else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')
        correct_answers += 1

    print(f'Congratulations, {name}!')


def main():
    run_game()


if __name__ == '__main__':
    main()