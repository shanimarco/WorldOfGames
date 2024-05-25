import CurrencyRouletteGame
import MemoryGame
import GuessGame
import Score


def welcome(name):
    welcome_string = "Hello " + name + " and welcome to the World of Games. \nHere you can find many cool games to play"
    return welcome_string

def load_game():
    print("Please choose a game to play:"
          "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back "
          "\n2. Guess Game - guess a number and see if you chose like the computer "
          "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
          "\nI want to play game number:", end=" ")

    game_number = int(input())

    if game_number in range(1, 4):
        print("Please choose game difficulty from 1 to 5:")
        game_difficulty = input()
        if int(game_difficulty) in range(1, 6):
            if game_number == 1:
                result = MemoryGame.play(game_difficulty)
            elif game_number == 2:
                result = GuessGame.play(game_difficulty)
            else:
                result = CurrencyRouletteGame.play(game_difficulty)
        else:
            print("incorrect game difficulty")
    else:
        print("game doesn't exists")

    if result == True:
        print("You won!!")
        Score.add_score(game_difficulty)
    else:
        print("You lost")