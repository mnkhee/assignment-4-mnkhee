"""
Joshua Chuah
A01334966
"""
# 150 x 50 ascii art
import random
import itertools


def make_board(rows, columns):
    # return a dictionary with positions as keys and what's at those positions as values
    # some rooms will be empty, some rooms will have enemies
    board = {}

    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = ["Field Tepsia"]

    board[(0, 0)] = ["Enemy", "Stowry Village"]
    board[(2, 3)] = ["Lake Tepsia"]
    board[(5, 3)] = ["Lord Drakon's Castle'"]
    return board


def make_character(character):
    character = input('Input your name: \n')
    player_info = {'Name': character, 'X': 0, 'Y': 0, 'Current_HP': 34, 'Max_HP': 34, 'Class': 'Basic'}

    def character_class():
        sub_class_choice = ''
        print('''\nIn the vast world of Tepsia, there are 3 warrior professions, each excelling in different categories.
        Swordsman: Guarantees high damage output, but at a cost.
        Mage: Masters of magic, rely on mana to cast elementals.
        Tank: High defence, can sponge a lot of hits before going down
        \n''')
        while True:
            main_class = ['Swordsman', 'Mage', 'Tank']
            for i in enumerate(main_class):
                print(i)
            class_options = input('\nChoose a profession: \n').title()

            if class_options == '0':
                class_choice = 'Swordsman'
                break
            elif class_options == '1':
                class_choice = 'Mage'
                break
            elif class_options == '2':
                class_choice = 'Tank'
                break
            else:
                print('Invalid profession!')

        print('Great! You chose', class_choice)
        print('Now its time to select a subclass...')

        if class_options == '0':
            print('''\nThere are two types of swordsmen, each providing their pros and cons
              Samurai: Dances around the battle field with their swift movement, striking their opponents down with a katana. [High damage, high speed, low defence].
              Berserker: An immovable object meets an unstoppable force to form a warrior who stops at nothing to strike the enemy down. [High damage, high defence, low speed].\n''')
            while True:
                sword_sub = ['Samurai', 'Berserker']
                for i in enumerate(sword_sub):
                    print(i)
                sub_class_options = input('Choose a subclass: \n 0: Samurai \n 1: Berserker \n').title()
                if sub_class_options == '0':
                    sub_class_choice = 'Samurai'
                    break
                elif sub_class_options == '1':
                    sub_class_choice = 'Berserker'
                    break
                else:
                    print('Invalid sub class!')
        elif class_options == '1':
            print('''\nThere are two types of mages, each casting their own unique elementals
                Sorcerer: Specializes in sorcery, witchcraft and black magic. Can inflict daze and confuse on the enemy, lowering their attack and defence. [High damage, medium speed, low defence, high mana consumption].
                Elementalist: Utilizes the four elementals to inflict damage on their foes. [Medium damage, medium speed, medium defence, medium mana consumption].\n''')
            while True:
                mage_sub = ['Sorcerer', 'Elementalist']
                for i in enumerate(mage_sub):
                    print(i)
                sub_class_options = input('\nChoose a subclass:').title()
                if sub_class_options == '0':
                    sub_class_choice = 'Sorcerer'
                    break
                elif sub_class_options == '1':
                    sub_class_choice = 'Elementalist'
                    break
                else:
                    print('Invalid sub class!')
        elif class_options == '2':
            print('''\nThere is only one Tank type
                Paladin: The only tank type. Never afraid of a fight with their high hp, and armour to tank all the hits. [Low damage, Very low speed, very high defence].\n''')
            while True:
                sub_class_options = input('Choose a subclass: \n Paladin \n').title()
                if sub_class_options == 'Paladin':
                    sub_class_choice = 'Paladin'
                    break
                else:
                    print('Invalid sub class!')

        print('Great! you have finished character customization!')
        print('Class:', class_choice, '\nSub Class:', sub_class_choice)
        return [class_choice, sub_class_choice]

    player_class = character_class()
    player_info['Class'] = player_class[1]
    return player_info


def player_stats(character):

    if character['Class'] == 'Basic':
        character['Attack'] = 14
        character['Defence'] = 14
    elif character['Class'] == 'Samurai':
        character['Current_HP'] = 24
        character['Max_HP'] = 24
        character['Attack'] = 27
        character['Defence'] = 12
    elif character['Class'] == 'Berserker':
        character['Current_HP'] = 29
        character['Max_HP'] = 29
        character['Attack'] = 19
        character['Defence'] = 18
    elif character['Class'] == 'Sorcerer':
        character['Current_HP'] = 20
        character['Max_HP'] = 20
        character['Attack'] = 32
        character['Defence'] = 11
        character['Mana'] = 75
    elif character['Class'] == 'Elementalist':
        character['Current_HP'] = 26
        character['Max_HP'] = 26
        character['Attack'] = 22
        character['Defence'] = 13
        character['Mana'] = 109
    elif character['Class'] == 'Paladin':
        character['Current_HP'] = 36
        character['Max_HP'] = 36
        character['Attack'] = 16
        character['Defence'] = 28
    print(character)
    return character



def describe_current_location(board, character):
    location = board[(character['X'], character['Y'])]  # = [character['Name']]  # placing character at (0, 0)
    character_value = list(board.values()).index(location)
    character_location = list(board.keys())[character_value]  # grabbing coordinate of the user
    # updating the x and y values in charcter dictionary
    character['X'] = character_location[0]
    character['Y'] = character_location[1]
    print('You are located at', character_location, board[character_location])
    return character_location


def get_user_choice():
    directions = ['North', 'East', 'South', 'West']
    while True:
        for i in enumerate(directions):
            print(i)
        user_choice = input('\nPick a direction to move: \n')
        if user_choice == '0':
            user_choice = 'North'
            break
        elif user_choice == '1':
            user_choice = 'East'
            break
        elif user_choice == '2':
            user_choice = 'South'
            break
        elif user_choice == '3':
            user_choice = 'West'
            break
        else:
            print('Invalid option, please type something from this list')
    return user_choice


def validate_move(board, character, direction):
    while True:
        if direction == 'North':
            character['Y'] += 1
        elif direction == 'East':
            character['X'] += 1
        elif direction == 'South':
            character['Y'] -= 1
        elif direction == 'West':
            character['X'] -= 1

        if character['Y'] < 0 or character['X'] < 0:
            return False
        elif character['Y'] > 5 or character['X'] > 5:
            return False
        else:
            return True


def move_character(location, board, character):
    print('Y Position: ', character['Y'])
    board[location] = ['Empty Room']
    location = (character['X'], character['Y'])
    print(location)
    print(character)
    # print(character['X'], character['Y'])
    print(board)


def check_for_challenges():
    # create a random number between x - x and if the value is less than or over randNum, execute challenge
    is_battle = random.randint(0, 20)
    if is_battle > 14:
        return True
    else:
        return False


def execute_challenge_protocol(character):
    # if character is level 1 --> easy challenge. If level 2 --> medium. If level 3 --> big boss
    pass


def check_if_goal_attained(board, character):
    # check if boss is dead
    if character['Name'] in board:
        print('yo')


def character_has_leveled():
    xp = 0
    level = 1
    if level == 1:
        xp += random.randint(123, 156)
    elif level == 2:
        xp += random.randint(109, 122)
    elif level == 3:
        xp += random.randint(78, 108)

    if xp >= 750:
        level += 1
        xp -= 750
    print(level, xp)
    return True


def execute_glow_up_protocol():
    pass


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    player_stats(character)
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        location = describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(location, board, character)
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
    game()
    # character_class()
    # print(make_board(5, 5))
    print('''
     
     
                                        ε  ╣],
                                      Γ]╣╪╠▓▓╣▒ ⌐
                                     [╫▐╣▓╬▓▓╬▓▌▓ ƒ
                                     ╣▓▓▓▓▓╬▓╣▓▓╬▓▌
                         ~-         ╗█▓▓█▓▓▓▓▓▓▓▓╬▓ É
                          ,,,"w▌,   ▐▓▓█╨╙▓▓█▀╙██▓█▌ - ,╓≈"`
                      .,╠▓▓▓▓▓▓▓▓▓▄,╙██▒∩».└ ;░╠███▓▓▓╠▄▄▓▓▓╨╙╙└
                    `""▓▓▓███████████▓╬╝▌#µ░░φå▌╬████████▓█▓▓▓▓Mw
                    ▄▀▀└,▄▄▓███████▀╙╙╚▒└^│,│`╙╗╬░╙╟████████▌╙▀▓▓ └▀w,
                    ,▄▓▓▀╠▓███████▒░░"░╠╟▌▄▄▄▄╬╩░░░φ█████████▓▌  ▀▄
                   ╓▀─ ▄█▀▓████████▌░░░░≥╚▓▓▓▌Å░░░╔▓██████▓^~╙╙▀▄ └╕
                  ,¬ ▄▀└╓▀▓█████████▓▓▓▄▒╠╥,▄▓▓█▓▓█████████▓▄    ▀
                    ▓─ Æ.█████▀ ▀███▓▄╬▀████╬▓▓██████▀╙▀███▓─\
                   └  ' ▓███▀     ╟█████▓██████╣████¬   └███▌
                       ╫▓██╙       ╟███████████████⌐     ╟██╠▒
                      @╣█▌          ╙██████████████▓▄▄,   ▓╬▓╬╕
                     ╬╬▓▌            ╟████████████▌██████▓▄▀███▄
                    ╬╠██▀          ,#▓▓███▓▓▓█████▓▄▄▀█████▓╬╬╬▓▌
                    ▒╬╬█▄         ╣▓▀██▓╬▓████▓▒▒╬██▓   ╙▀██████▓▓^
                   ╚╘██╬╬µ       ▄▓╙╬▓█████████╬█▓▓▓▓▌      └╙▀▀╟
                     ¬▓█▓╢      ███▓██▓▓▒▒╠░╠▒╟▓▌▓╬███▄
                       ╙██▄    ╫███████████▓█▓█████████▄
                        ╙██▄  ▓█████████████████████████
                          █╬▌µ██████████████████████▓▓██▒
                           ▓█╬╬▓████████████████████▓▓▓█▌
                           ╬╠╬╬███j████████╟██▌██████╬╬▓Γ
                           ▒╠▓██ ` ╚└█╝╙█▀▌▐╣█ Γ█▌▀███▒╬
                          ▐▓╬█▌▀⌐    ╟  ╙▌  ▐▌  █   ██░▒µ
                          ▓█▓█  ¬        └  └       ████▌
    ''')

    print('''
     
                                          ,  ▓█
                                         ╗▌ ▐██▓
                              ▐⌐    ].  ╓█▌]███▓▌  ]▌    ║▄
                              ▓▌   ╓█▒ ]██▒█████▓▌ ╟█▌   █▓▌
                             ▐█▓▒ ╔██▌]██▓▓█████▓▓▌██▓▌ ╫█▓▓▌
                            ╓██▓▓▄███▓███▓██████▓▓▓██▓▓▄██▓▓▓▌
                        ]  ▄███▓████████████████▓▓▓▓█▓▓▓██▓▓▓▓▒
                        ▓▒▐██████████████████████▓▓▓▓▓▓▓▓█▓▓▓▓▓   ]╕
                       ╟█▌███████████████████████▓▓▓▓▓▓▓▓█▓▓▓▓▓▌ ]█▒
                      j██▓███████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄█▓▒  ,╕
                      ▓██▓██████████████████████▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓██▓▒ ▄█⌐
                  ╓  ]███████████████████████████▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▒▓█▓
                  ╙█,╟███████████████████████████▓▓▓▓▓▓▓█▓█▓▓▓▓█▓▓▓██▓▓
                  "██▓█╬██████████▓▒╠╠╠▀╬████████▓▓▓▓█▓╨▀██▓▓▓█▓▓▓██▓▓▌
                ╟▌░████╬█████▓█╬▒╠╠╠╠╠╠╠╠╠░▒█████▓▓▓▓█╩  └ ╙███▓╬▀▀╩╫▓
                 ██▓█████████▓▒╠╠╠╠╠╠╠╠╠╠╠╠╠╠╣███▓▓▀▐╙      ▐▓▓▓▓▌░╟▓,▄∩
                 ╙███████████▌╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠▀▓▓└         ╠╠█▓█▓║▓█▓┘
                  ██████████╬░░╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠           ╠╠▓██▓▓█▌,,
                  ╙███████▌╠╠╠▒╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠⌐          ╙╠╣█▓▓▓██▓╙
                  '▓█████▌▒╣▒╠╔╠╠╠╠╠╠▒╠╠φ╦╚░╠╩░▒▒▒ε   .  ""  └╠╬█▓▓▓╨
                  .φ╠╙▀██╬╠╫█▒╠╠▄▓▓██▓█▓▄▒╩╩░▒▒▒▒▒╠╔░ ,╓φφφφ╔, ╠╣█▓░
                 ╔╠╙╣▒▒╖╙▀╠▒╬█████╬╬╬▓▒╙╙██▒╚▒▒▒▒╠╠╠╓▒███▀▀███▄█▀░▒,»
                ⁿ╠░╬╠▒╬▒╠╦╠╠╠▀███╬▓████▒╠╠█▒░╚▒╠╠]╠╠╟█╬╬▄██▄╓██▒▐▓╙╚ '
                 ╚╠╦ └╙▀▒╠╠╩╠╠╠██▓▓████░╠▒██▄≥░╠╠╠╩╣█╬▓╠████▒╣█╠╠▒▄ '
                  `╚╠╦▒╠╠╠╠░╠╠╠░╣██╬╬▓▓▓▓█▌░░░╙╓,┐~╙██╬▓╬╬╬▒▄█▌╠╩╬,⌐
                      "╙╙"╚╠╬╫▄▒╠░╬╬╬╬╬╬░╩╙╔╠▒╙ ."'^Ç ╨▀▀▀▀▀╨╙]╠φ╬ε
                          '╠╠╠▓█▌╠╠╠╠╠▒▒▒▒╠╠╠½∩  ▓ ⌐ └└      ,▄╛╚▄Γ
                           `╠╠╠███▄╓╠╠╠▒╠▒╠╠'╫▒ ,╙,░     ╠▒▓▓█" ▐╚∩
                            `╠╠╠╬███▓▒▒▒╠╠╠╠▒╠╠Γ'^^`^^"""j█▀╠└ ╔▓▓▒▒
                             ]╠╠╠╠░╬██████████▓▄▄▓▓▓▓▓▓▓▓█▌╠╙  `╫▓╩
                              └╠▒╙╚╠▒████▓███████▓█▓█▓██▀└]╠'
                                 ╚▒╠╠╠█████████████████▌ ≤╙
                         ╓▄▄▄▓██████▌╠░▀██████████████▀¿
                    ,▄▓██████▀▀▀█╙╝▀█▓▒╠╠░╬╬╬░,╓,╙╙╙└╓███▓▄
                                   ╙?██▒╠╠░╠╠╠╠╙╙╙░ ,╙" └^ └
                                    .█▒"▒╠╠╠╠╠╡    .
                                   .▓▌ "██▄╩╠╠▒╓╓»≈~
                                   ]█▒ !███   █▌
                                    ╟▌ ▄███▄  ╫▒
                                    j▌▐█████▓░╫,
                                    ,█▐█╩ ╙██▌█
                                    `██▌    █▒█▌
                                    7█╟█   .█╩▓█⌐
                                       ╟▄  .█
                                       .█, ╟▒
                                       .█. ╟▌
                                        ▀  '▀
    ''')


if __name__ == '__main__':
    main()
