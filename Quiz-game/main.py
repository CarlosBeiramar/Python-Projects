import menu
import os
from QuizGame import QuizGame


def choose_initial_menu():
    os.system('clear')
    menu.menu_initial()
    option = input("Choose an option: ")
    valid = False

    while not valid:
        match option:
            case '1':
                #start the game
                valid = True
            case '0':
                #quit game
                exit()
            case other:
                menu.menu_initial()
                option = input("Choose an option: ")


def choose_your_game():
    os.system('clear')
    menu.menu_difficulty()
    option = input("Choose an option: ")

    while True:
        match option:
            case '1':
                # Easy
                os.system('clear')
                quiz = QuizGame("easy")
                quiz.game_mode()
                break
            case '2':
                # Medium
                quiz = QuizGame("medium")
                quiz.game_mode()
                break
            case '3':
                # Hard
                quiz = QuizGame("hard")
                quiz.game_mode()
                break
            case other:
                menu.menu_difficulty()
                option = input("Choose an option: ")

def choose_game_option_menu():

    os.system('clear')
    menu.game_mode()
    option = input("Choose an option: ")
    valid = False

    while not valid:
        match option:
            case '1':
                choose_your_game()
                break
            case '2':
                # built-in game
                valid = True
            case other:
                menu.game_mode()
                option = input("Choose an option: ")


def main():
    choose_initial_menu()
    choose_game_option_menu()

main()
