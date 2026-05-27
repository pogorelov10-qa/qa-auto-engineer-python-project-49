"""Общий движок для запуска игр."""

from brain_games.cli import welcome_user


def run_game(game_module):
    """Запускает игру с переданной логикой."""
    name = welcome_user()
    print(game_module.RULE)

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game_module.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ').strip()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')
        correct_answers += 1

    print(f'Congratulations, {name}!')
    return name