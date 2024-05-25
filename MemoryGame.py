import random
import time
# import os

def generate_sequence(game_difficulty):
    random_list = []
    for number in range(int(game_difficulty)):
        random_list_number = random.randint(1, 101)
        random_list.append(random_list_number)
    print(random_list)
    time.sleep(0.7)
    # os.system('cls')
    for i in range(20):
        print()
    return random_list

def get_list_from_user(game_difficulty):
    print("now let's see what you remember")
    user_list = []
    for number in range(0, int(game_difficulty)):
        print("enter number", number+1, ":" , end=' ')
        element = int(input())
        user_list.append(element)
    return user_list

def is_list_equal(random_list, user_list):
    if random_list == user_list:
       result = True
    else:
        result = False
    return result



def play(game_difficulty):
    random_list = generate_sequence(game_difficulty)
    user_list = get_list_from_user(game_difficulty)
    result = is_list_equal(random_list, user_list)
    return result
