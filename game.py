"""
Joshua Chuah
A01334966
"""
# 150 x 50 ascii art
import random


def make_board(rows, columns):
    # return a dictionary with positions as keys and what's at those positions as values
    # some rooms will be empty, some rooms will have enemies
    board = {}

    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = ["Empty Room", None]

    board[(0, 0)] = ['Enemy', None]
    board[(3, 3)] = ['Enemy', None]
    return board


def make_character(character):
    player_name = input('Input your name: \n')
    character = player_name
    player_info = {'Name': character, 'Current HP': 5, 'Max HP': 120}
    return player_info


def describe_current_location(board, character):
    pass


def get_user_choice():
    directions = ['North', 'East', 'South', 'West']
    while True:
        for i in enumerate(directions):
            print(i)
        user_choice = int(input('Pick a direction to move: \n'))
        if user_choice == 0:
            user_choice = 'north'
            break
        elif user_choice == 1:
            user_choice = 'east'
            break
        elif user_choice == 2:
            user_choice = 'south'
            break
        elif user_choice == 3:
            user_choice = 'west'
            break
        else:
            print('Invalid option, please type something from this list')

    return user_choice


def validate_move(board, character, direction):
    pass


def move_character(character):
    pass


def check_for_challenges():
    # create a random number between x - x and if the value is less than or over randNum, execute challenge
    pass


def execute_challenge_protocol():
    # if character is level 1 --> easy challenge. If level 2 --> medium. If level 3 --> big boss
    pass


def check_if_goal_attained(board, character):
    pass


def character_has_leveled():
    # add something sort of visual to let the user know that they leveled up. maybe ascii art?
    xp = 0
    level = 1
    if level == 1:
        xp += 135
    elif level == 2:
        xp += 120
    elif level == 3:
        xp += 98
    if xp >= 750:
        level += 1
        xp -= 750
        print('You are now level', level, '!')
    return level


def execute_glow_up_protocol():
    return


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled():
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print('Invalid direction! Try again... ')
            # Tell the user they can’t go in that direction
        # Print end of game stuff like congratulations or sorry you died
        if achieved_goal == False:
            print('You Lose!')
        else:
            print('Win')

    print('you win')


def main():
    # game()
    print(make_board(5, 5))


if __name__ == '__main__':
    main()
