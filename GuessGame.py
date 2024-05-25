import random

def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number

def get_guess_from_user(difficulty):
    print("please choose a nuber between 1 to", difficulty, ":", end =" ")
    user_input_number = int(input())
    return user_input_number

def compare_results(user_number, secret_number):
    if user_number == secret_number:
        result = True
    else:
        result = False
    return result

def play(game_difficulty):
    user_number = get_guess_from_user(game_difficulty)
    secret_number = generate_number(game_difficulty)
    print("The user number is =", user_number)
    print("The secret number is =", secret_number)
    result = compare_results(user_number, secret_number)
    return result



