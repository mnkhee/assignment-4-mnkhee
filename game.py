"""
Joshua Chuah
A01334966
"""
# 150 x 50 ascii art
import random
import time
import sys
import itertools


def make_board(rows: int, columns: int) -> dict:
    # return a dictionary with positions as keys and what's at those positions as values
    # some rooms will be empty, some rooms will have enemies
    board = {}

    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = ["Entia Field"]

    board[(0, 0)] = ["Stowry Village"]
    board[(1, 0)] = ['Margrove Pass']
    board[(0, 1)] = ['Margrove Pass']
    board[(1, 1)] = ['Margrove Pass']
    board[(2, 3)] = ["Entia Lake"]
    board[(4, 3)] = ["Drakon's Castle"]
    board[(1, 4)] = ["Entia Capital City"]
    return board


def make_character(character: str) -> bool:
    # character = input('Input your name: \n')
    player_info = {'Name': character, 'X': 0, 'Y': 0, 'Level': 1, 'Current_HP': 34, 'Max_HP': 34, 'Class': 'Basic'}

    def character_class() -> list:
        sub_class_choice = ''
        print('\nIn the vast lands of Entia, there are 3 warrior professions, each excelling in different categories.'
              f'Swordsman: Masters at the sword, guarantees high damage output, but at a cost.'
              f'Mage: Masters of magic, rely on mana to cast elementals.'
              f'Tank: High defence, can sponge a lot of hits before going down.\n')
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
                print('Invalid profession!\n')

        print('Great! You chose', class_choice)
        print('Now its time to select a subclass...')

        if class_options == '0':
            print('''\nThere are two types of swordsmen, each providing their pros and cons
              Samurai: Dances around the battle field with their swift movement, striking their opponents down with a katana. [High damage, low defence].
              Berserker: An immovable object meets an unstoppable force to form a warrior who stops at nothing to strike the enemy down. [High damage, high defence].\n''')
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
                Sorcerer: Specializes in sorcery, witchcraft and black magic. Can inflict daze and confuse on the enemy, lowering their attack and defence. [High damage, low defence, high mana consumption].
                Elementalist: Utilizes the four elementals to inflict damage on their foes. [Medium damage, medium defence, medium mana consumption].\n''')
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
                Paladin: The only tank type. Never afraid of a fight with their high hp, and armour to tank all the hits. [Low damage, very high defence].\n''')
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

    # player_class = character_class()
    # player_info['Class'] = player_class[1]
    return player_info


def player_stats(character: dict) -> dict:
    if character['Class'] == 'Basic':
        character['Attack'] = 14
        character['Defence'] = 14
        character['Stamina'] = 50
    elif character['Class'] == 'Samurai':
        character['Current_HP'] = 22
        character['Max_HP'] = 22
        character['Attack'] = 29
        character['Defence'] = 12
        character['Stamina'] = 100
    elif character['Class'] == 'Berserker':
        character['Current_HP'] = 29
        character['Max_HP'] = 29
        character['Attack'] = 21
        character['Defence'] = 21
        character['Stamina'] = 100
    elif character['Class'] == 'Sorcerer':
        character['Current_HP'] = 20
        character['Max_HP'] = 20
        character['Attack'] = 32
        character['Defence'] = 11
        character['Mana'] = 75
    elif character['Class'] == 'Elementalist':
        character['Current_HP'] = 25
        character['Max_HP'] = 25
        character['Attack'] = 18
        character['Defence'] = 18
        character['Mana'] = 109
    elif character['Class'] == 'Paladin':
        character['Current_HP'] = 36
        character['Max_HP'] = 36
        character['Attack'] = 14
        character['Defence'] = 28
        character['Stamina'] = 89
    return character


def player_move_set(character: dict) -> dict:
    character['Move_Set'] = {}
    if character['Class'] == 'Basic':
        character['Move_Set']['Punch'] = character['Attack']
    elif character['Class'] == 'Samurai':
        character['Move_Set']['Swift Strike'] = character['Attack']
        # character['Move_Set']['Shadow Blade'] = character['Attack'] + 4
    elif character['Class'] == 'Berserker':
        character['Move_Set']['Running Slash'] = character['Attack']
    elif character['Class'] == 'Sorcerer':
        character['Move_Set']['Magic Missile'] = character['Attack']
        character['Move_Set']['Starlight Kick'] = 5
    elif character['Class'] == 'Elementalist':
        character['Move_Set']['Wind Gust'] = character['Attack']
    elif character['Class'] == 'Paladin':
        character['Move_Set']['Hammer Down'] = character['Attack']
    print(character)
    return character


def describe_current_location(board: dict, character: dict) -> tuple:
    character_location = character['X'], character['Y']
    print('You are located at', character_location, board[character_location])
    if board[character_location] == ['Entia Field']:
        print('A vast field connecting each part of Entia')
    elif board[character_location] == ['Entia Capital City']:
        print("The capital city of Entia, houses many shops to buy goods from.")
    elif board[character_location] == ['Entia Lake']:
        print("Home of the Varya, Entia's water tribe. Very deadly if you get on the wrong terms.")
    elif board[character_location] == ['Stowry Village']:
        print(character['Name'] + "'s home. There is a very nostalgic feeling every time you are here...")
        print("If you are ever in need of health, come here to restore some health!")
        if character['Current_HP'] < character['Max_HP']:
            character['Current_HP'] += random.randint(10, character['Max_HP'])
            print('Your health has been restored to max!')
    elif board[character_location] == ['Margrove Pass']:
        print(
            'The border between Stowry Village and Entia Field. This desolate area keeps residence of Stowry stuck. Home to many monsters...')
    return character_location


def get_user_choice() -> str:
    directions = ['North', 'East', 'South', 'West', 'Quit']
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
        elif user_choice == '4':
            print('GAME OVER!')
            sys.exit()
        else:
            print('Invalid option, please type something from this list')
    return user_choice


def validate_move(character: dict, direction: str) -> bool:
    if direction == 'North' and character['Y'] == 4:
        return False
    elif direction == 'South' and character['Y'] == 0:
        return False
    elif direction == 'East' and character['X'] == 4:
        return False
    elif direction == 'West' and character['X'] == 0:
        return False
    else:
        return True


def move_character(character: dict, direction: str):
    if direction == 'North':
        character['Y'] += 1
    elif direction == 'East':
        character['X'] += 1
    elif direction == 'South':
        character['Y'] -= 1
    elif direction == 'West':
        character['X'] -= 1


def check_for_challenges(character: dict) -> bool:
    if character['X'] == 1 and character['Y'] == 0:
        return True
    elif character['X'] == 0 and character['Y'] == 1:
        return True
    elif character['X'] == 1 and character['Y'] == 1:
        return True
    elif character['X'] == 4 and character['Y'] == 3:
        return True

    is_battle = random.randint(0, 20)
    if is_battle > 12:
        return True
    else:
        return False


def execute_challenge_protocol(character: dict):
    # if character is level 1 --> easy challenge. If level 2 --> medium. If level 3 --> big boss
    if character['Level'] == 1:
        execute_battle(character, 'easy')
    elif character['Level'] == 2:
        execute_battle(character, 'medium')
    elif character['Level'] == 3:
        execute_battle(character, 'hard')


def execute_battle(character: dict, difficulty: str):
    enemy = choose_enemy(character)
    choices = ['Quit']  # append move set to character dictionary and grab the move set and put it in choices
    if difficulty == 'easy':
        print('You are going against', enemy['Name'])
    while enemy['Current_HP'] > 0:
        print("What's your move?")
        for i in enumerate(character['Move_Set']):
            print(i)
        user_choice = int(input(''))
        if user_choice < len(character['Move_Set'].keys()):
            move = (character['Move_Set'][list(character['Move_Set'].keys())[user_choice]])
            enemy['Current_HP'] -= move
            character['Current_HP'] -= enemy['Attack']
            print('You dealt', move, 'Damage!')
        else:
            print(f"Invalid selection, please select a number from the move set")


def choose_enemy(character: dict):
    selection = random.randint(0, 1)
    varyan = {'Name': 'Varyan Warrior', 'Current_HP': 37, 'Max_HP': 37, 'Attack': 18, 'Defence': 17, 'XP_Gain': 177}
    imp = {'Name': 'Imp', 'Current_HP': 13, 'Max_HP': 13, 'Attack': 9, 'Defence': 9, 'XP_Gain': 56}
    goblin = {'Name': 'Goblin', 'Current_HP': 19, 'Max_HP': 19, 'Attack': 16, 'Defence': 17, 'XP_Gain': 123}
    slime = {'Name': 'Slime', 'Current_HP': 7, 'Max_HP': 7, 'Attack': 5, 'Defence': 4, 'XP_Gain': 43}
    drakon = {'Name': "'Demon King' Drakon", 'Current_HP': 256, 'Max_HP': 256, 'Attack': 82, 'Defence': 54}
    if character['X'] == 2 and character['Y'] == 3:
        return varyan
    if character['X'] == 4 and character['Y'] == 3 and character['Level'] == 3:
        return drakon
    if selection == 0:
        return imp
    elif selection == 1:
        return goblin
    else:
        return slime


def execute_boss(character: dict, enemy: dict):
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
    print('\n')
    print(f"As you enter the castle, you get a trickling feeling down your spine. Something is clearly off...")
    time.sleep(2)
    print(f"Step by step you make ur way up the castle")
    time.sleep(2)
    print(f"Drakon: Who dares step foot here?")
    time.sleep(2)
    print(f"*Deep gulp. \n{character['Name']}: The person who will put an end to the suffering you caused on Entia")
    time.sleep(2)
    print(f"Drakon: MWAHAHAHAHA... Don't make me laugh...")
    print(f"What's your move?")
    for i in enumerate(character['Move_Set']):
        print(i)
    user_choice = int(input(''))
    move = (character['Move_Set'][list(character['Move_Set'].keys())[user_choice]])
    print(f'You chose', list(character["Move_Set"].keys())[user_choice])
    print(f"You dealt...")
    print(f"")


def check_if_goal_attained(board: dict, character: dict) -> bool:
    # check if boss is dead
    if "Drakon's Castle" in board[(4, 3)]:
        return False
    else:
        return True


def character_has_leveled(character: dict) -> bool:
    if character['Level'] == 2:
        print(''' ▄█          ▄████████  ▄█    █▄     ▄████████  ▄█            ███    █▄     ▄███████▄ 
███         ███    ███ ███    ███   ███    ███ ███            ███    ███   ███    ███ 
███         ███    █▀  ███    ███   ███    █▀  ███            ███    ███   ███    ███ 
███        ▄███▄▄▄     ███    ███  ▄███▄▄▄     ███            ███    ███   ███    ███ 
███       ▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀     ███            ███    ███ ▀█████████▀  
███         ███    █▄  ███    ███   ███    █▄  ███            ███    ███   ███        
███▌    ▄   ███    ███ ███    ███   ███    ███ ███▌    ▄      ███    ███   ███        
█████▄▄██   ██████████  ▀██████▀    ██████████ █████▄▄██      ████████▀   ▄████▀      
▀                                              ▀                                      ''')
        print(f"Great job {character['Name']}! You are one step away from Drakon.")
        return True
    elif character['Level'] == 3:
        print(''' ▄█          ▄████████  ▄█    █▄     ▄████████  ▄█            ███    █▄     ▄███████▄ 
███         ███    ███ ███    ███   ███    ███ ███            ███    ███   ███    ███ 
███         ███    █▀  ███    ███   ███    █▀  ███            ███    ███   ███    ███ 
███        ▄███▄▄▄     ███    ███  ▄███▄▄▄     ███            ███    ███   ███    ███ 
███       ▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀     ███            ███    ███ ▀█████████▀  
███         ███    █▄  ███    ███   ███    █▄  ███            ███    ███   ███        
███▌    ▄   ███    ███ ███    ███   ███    ███ ███▌    ▄      ███    ███   ███        
█████▄▄██   ██████████  ▀██████▀    ██████████ █████▄▄██      ████████▀   ▄████▀      
▀                                              ▀                                      ''')
        print(f"Great job {character['Name']}! The cloudy skies start to darken at Drakon's Castle (4, 3)"
              f"Its time to put an end to the wrath put down on Entia.")
        return True


def execute_glow_up_protocol(character: dict) -> dict:
    print(character['Class'])
    if character['Class'] == 'Samurai':
        character['Current_HP'] += 56
        character['Max_HP'] += 56
        character['Attack'] += 29
        character['Defence'] += 12
        character['Stamina'] += 100
    elif character['Class'] == 'Berserker':
        character['Current_HP'] += 67
        character['Max_HP'] += 67
        character['Attack'] += 21
        character['Defence'] += 21
        character['Stamina'] += 100
    elif character['Class'] == 'Sorcerer':
        character['Current_HP'] += 48
        character['Max_HP'] += 48
        character['Attack'] += 34
        character['Defence'] += 11
        character['Mana'] += 75
    elif character['Class'] == 'Elementalist':
        character['Current_HP'] += 73
        character['Max_HP'] += 73
        character['Attack'] += 18
        character['Defence'] += 18
        character['Mana'] += 109
    elif character['Class'] == 'Paladin':
        character['Current_HP'] += 87
        character['Max_HP'] += 87
        character['Attack'] += 14
        character['Defence'] += 28
        character['Stamina'] += 89
    return character


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    player_stats(character)
    player_move_set(character)
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        location = describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            # describe_current_location(board, character)
            print(location)
            there_is_a_challenge = check_for_challenges(character)
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled(character):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print('Invalid direction! Try again... ')

            # Tell the user they can’t go in that direction
        # Print end of game stuff like congratulations or sorry you died

    print('you win')


def main():
    game()


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
