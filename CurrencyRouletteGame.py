from forex_python.converter import CurrencyCodes
import requests
import random

def get_guess_from_user(random_num):
    symbol = CurrencyCodes()
    print("guess the value of", random_num, symbol.get_symbol('USD'), "in ILS", symbol.get_symbol('ILS'), ":", end=' ')
    user_guess = input()
    return user_guess

def get_money_interval(game_difficulty, random_num):
    url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_zPMBaKFhAi053GmZVx9KlW9FMJ8AZrf7HZS2hBbP&currencies=ILS'
    response = requests.get(url)
    currency_rate_json = response.json()
    currency_rate = currency_rate_json['data']['ILS']
    print (currency_rate)
    lowes_range = (int(random_num) * currency_rate) - (5 - int(game_difficulty))
    highest_range = (int(random_num) * currency_rate) + (5 - int(game_difficulty))
    interval = [int(lowes_range), int(highest_range)]
    print(interval)
    return interval


def play(game_difficulty):
    random_num = random.randint(1, 100)
    user_guess = int(get_guess_from_user(random_num))
    interval = get_money_interval(game_difficulty, random_num)
    start_range = interval[0]
    end_range = interval[1]+1

    #check if the user guess is in the range
    if user_guess in range(start_range, end_range):
        result = True
    else:
         result = False

    return result



