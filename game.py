"""
Joshua Chuah
A01334966
"""
import random
import time
import sys
import itertools
import typing


def make_board(rows: int, columns: int) -> dict:
    """
    creates and returns board containing coordinates filled with information

    :precondition: rows must be an integer
    :precondition: columns must be an integer
    :param rows: an integer
    :param columns: an integer
    :return: a board containing tuples as coordinates filled with location names
    """
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
    board[(0, 4)] = ["Makna Harbour"]
    board[(3, 3)] = ["Satorl Forest"]
    board[(2, 3)] = ["Satorl Forest"]
    return board


def story():
    print(f"In the vast world of Entia, there was always peace an unity."
          f"\nEveryone worked together to create 'Entia Capital City', a place where everyone could live in peace"
          f"\nHowever, all was not as peaceful as it seemed. Those who lived in the forest did not receive equal treatment"
          f"\nThis was because they were different than the others."
          f"\nThey were often called 'Demons' because of their looks."
          f"\nDespite the inequality, they did not do anything about it"
          f"\nThat was until one day, a boy named 'Drakon' was born."
          f"\nGrowing up, Drakon despised the inequality. He hated it so much..."
          f"\nHe chose to become an educator amongst the 'demons'."
          f"\nThat was until one day his father was wrongfully killed by the Entian Royal Guards."
          f"\nHis eyes filled with rage and he killed the guards, barely surviving in the process"
          f"\nWith the blood on the floor, One of the guards, with his dying breath, drew a scripture on the floor"
          f"\nIt summoned a demon, but unbeknownst to the guard, the demon would not be killing Drakon.")
    time.sleep(15)
    print(f"\nIt")
    time.sleep(1)
    print(f"\nWould")
    time.sleep(1)
    print(f"\nKill")
    time.sleep(1)
    print(f"\nHim.")
    time.sleep(1)
    print(f"\nThe demon locked eye contact with Drakon and negotiated a deal"
          f"\nDemon: If you sign a contract with me, I will lend you my powers"
          f"\nDrakon: What's the catch"
          f"\nDemon: You kill every single person in Entia"
          f"\nWithout hesitating, Drakon agreed to the contract"
          f"\nHe felt a rush of evil energy coursing through his veins"
          f"\nHe walked slowly towards the capital city"
          f"\nHe killed everyone on sight"
          f"\nNot even the heroes of the city could stop him"
          f"\nOne hero decided to run away, running to the most isolated area of Entia"
          f"\nHe ran to Stowry Village"
          f"\nThat's when he met you, a strongest warrior of Stowry."
          f"\nHe saw promise, and even trained you."
          f"\nHe explained the situation on his deathbed, 12 months after training"
          f"\nHis dying wish was")
    time.sleep(10)
    print(f'\nStop')
    time.sleep(1)
    print(f"Drakon\n\n\n\n\n\n")


def make_character(character: str) -> dict[str, int | str | typing.Any]:
    character = input('Input your name: \n')
    player_info = {'Name': character, 'X': 0, 'Y': 0, 'Level': 1, 'Current_HP': 34, 'Max_HP': 34, 'XP': 0, 'Class': 'Basic', 'Boss_Status': 'Alive'}

    def character_class() -> list:
        sub_class_choice = ''
        print('\nIn the vast lands of Entia, there are 3 warrior professions, each excelling in different categories.'
              f'\nSwordsman: Masters at the sword, guarantees high damage output, but at a cost.'
              f'\nMage: Masters of magic. Cast down elementals that deal a good amount of damage'
              f'\nTank: High defence, can sponge a lot of hits before going down.\n')
        while True:
            main_class = ['Swordsman', 'Mage', 'Tank']
            for index in enumerate(main_class):
                print(index)
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
                for index in enumerate(sword_sub):
                    print(index)
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
                Sorcerer: Specializes in sorcery, witchcraft and black magic.  [High damage, low defence, high mana consumption].
                Elementalist: Utilizes the four elementals to inflict damage on their foes. [Medium damage, medium defence, medium mana consumption].\n''')
            while True:
                mage_sub = ['Sorcerer', 'Elementalist']
                for index in enumerate(mage_sub):
                    print(index)
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

    player_class = character_class()
    player_info['Class'] = player_class[1]
    return player_info


def player_stats(character: dict) -> dict:
    if character['Class'] == 'Basic':
        character['Attack'] = 1000
        character['Defence'] = 85
    elif character['Class'] == 'Samurai':
        character['Current_HP'] = 56
        character['Max_HP'] = 56
        character['Attack'] = 29
        character['Defence'] = 12
    elif character['Class'] == 'Berserker':
        character['Current_HP'] = 67
        character['Max_HP'] = 67
        character['Attack'] = 21
        character['Defence'] = 21
    elif character['Class'] == 'Sorcerer':
        character['Current_HP'] = 48
        character['Max_HP'] = 48
        character['Attack'] = 34
        character['Defence'] = 11
    elif character['Class'] == 'Elementalist':
        character['Current_HP'] = 73
        character['Max_HP'] = 73
        character['Attack'] = 18
        character['Defence'] = 18
    elif character['Class'] == 'Paladin':
        character['Current_HP'] = 87
        character['Max_HP'] = 87
        character['Attack'] = 14
        character['Defence'] = 28
    return character


def player_move_set(character) -> dict:
    special = random.randint(5, 16)
    character['Move_Set'] = {'Run': 0}
    if character['Class'] == 'Basic':
        character['Move_Set']['Punch'] = character['Attack']
    elif character['Class'] == 'Samurai':
        character['Move_Set']['Swift Strike'] = character['Attack']
        character['Move_Set']['Shadow Blade'] = character['Attack'] + special
        character['Move_Set']['Soul Strike'] = character['Attack'] - 10
    elif character['Class'] == 'Berserker':
        character['Move_Set']['Running Slash'] = character['Attack']
        character['Move_Set']['Punishing Blow'] = character['Attack'] * 2
        character['Move_Set']['Crushing Knee'] = character['Attack'] - special
    elif character['Class'] == 'Sorcerer':
        character['Move_Set']['Magic Missile'] = character['Attack']
        character['Move_Set']['Pentagram Beam'] = character['Attack'] * special
        character['Move_Set']['Starlight Kick'] = character['Attack'] - 5
    elif character['Class'] == 'Elementalist':
        character['Move_Set']['Howling Wind'] = character['Attack']
        character['Move_Set']['Fire-Lightning Ball'] = character['Attack'] - 10
        character['Move_Set']['Enchanting Water Spirit'] = character['Attack'] * 3
    elif character['Class'] == 'Paladin':
        character['Move_Set']['Hammer Down'] = character['Attack']
        character['Move_Set']["Paladin's Fury"] = character['Attack'] + special
    return character


def describe_current_location(board: dict, character: dict) -> tuple:
    character_location = character['X'], character['Y']
    print(f'You are located at', character_location, board[character_location])
    if board[character_location] == ['Entia Field']:
        print(f'A vast field connecting each part of Entia')
    elif board[character_location] == ['Entia Capital City']:
        print(f"The capital city of Entia, houses many shops to buy goods from.")
    elif board[character_location] == ['Entia Lake']:
        print(f"Home of the Varya, Entia's water tribe. Very deadly if you get on the wrong terms.")
    elif board[character_location] == ['Makna Harbour']:
        print(f"Many imports come this way. All goods brought to Drakon")
    elif board[character_location] == ["Satorl Forest"]:
        print(f"Home of Drakon. This area is mostly dead and all signs of civilization has vanished.")
    elif board[character_location] == ['Stowry Village']:
        print(f"{character['Name']}'s home. There is a very nostalgic feeling every time you are here...")
        print(f"If you are ever in need of health, come here to restore some health!")
        if character['Current_HP'] < character['Max_HP']:
            character['Current_HP'] += random.randint(10, character['Max_HP'])
            print(f'Your health has been restored to max!')
    elif board[character_location] == ['Margrove Pass']:
        print(
            'The border between Stowry Village and Entia Field. This desolate area keeps residence of Stowry stuck. Home to many monsters...')
    return character_location


def get_user_choice() -> str:
    directions = ['North', 'East', 'South', 'West', 'Quit']
    while True:
        for index in enumerate(directions):
            print(index)
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
    if is_battle > 15:
        return True
    else:
        return False


def execute_challenge_protocol(character: dict):
    if character['Level'] == 1:
        execute_battle(character, 'easy')
    elif character['Level'] == 2:
        execute_battle(character, 'medium')
    elif character['Level'] == 3:
        execute_battle(character, 'hard')


def execute_battle(character: dict, difficulty: str) -> None:
    enemy = choose_enemy(character)
    if enemy['Name'] == "Drakon":
        execute_boss(character, enemy)
        return None
    if difficulty == 'medium':
        enemy['Attack'] *= 2
        enemy['Current_HP'] *= 2
        enemy['Max_HP'] *= 2
        enemy['Defence'] *= 2
        print(enemy)
    if difficulty == 'hard':
        enemy['Attack'] *= 3
        enemy['Current_HP'] *= 3
        enemy['Max_HP'] *= 3
        enemy['Defence'] *= 3
        print(enemy)
    while enemy['Current_HP'] > 0:
        if character['Current_HP'] < 0:
            print(f'GAME OVER! Your journey comes to an unfortunate end...')
            print(f'\nThanks for playing!')
            sys.exit()
        print(f"You are going against {enemy['Name']}")
        print("What's your move?")
        for i in enumerate(character['Move_Set']):
            print(i)
        user_choice = int(input(''))
        if user_choice == 0:
            print(f'You ran away! What a bummer...')
            print(f"You lose {enemy['Attack']} HP")
            character['Current_HP'] -= enemy['Attack']
            return None
        elif user_choice < len(character['Move_Set'].keys()):
            move = (character['Move_Set'][list(character['Move_Set'].keys())[user_choice]])
            enemy['Current_HP'] -= move
            print('You dealt', move, 'Damage!')
            if random.randint(0, 1) == 1:
                character['Current_HP'] -= enemy['Attack']
                print(f"{enemy['Name']} dealt {enemy['Attack']} damage!")
            else:
                print(f"{enemy['Name']} missed!")
        else:
            print(f"Invalid selection, please select a number from the move set")

    print(f'You defeated {enemy["Name"]}!')
    character['XP'] += enemy['XP_Gain']


def filtered_enemies(enemies: dict) -> bool:
    if enemies['Name'] != "varyan" and enemies['Name'] != "guard":
        return False
    else:
        return True


def choose_enemy(character: dict) -> dict | str:
    varyan = {'Name': 'Varyan Warrior', 'Current_HP': 37, 'Max_HP': 37, 'Attack': 18, 'Defence': 17, 'XP_Gain': 177}
    guard = {'Name': 'Demon Guard', 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 32, 'XP_Gain': 254}
    imp = {'Name': 'Imp', 'Current_HP': 13, 'Max_HP': 13, 'Attack': 9, 'Defence': 9, 'XP_Gain': 56}
    goblin = {'Name': 'Goblin', 'Current_HP': 19, 'Max_HP': 19, 'Attack': 16, 'Defence': 17, 'XP_Gain': 123}
    slime = {'Name': 'Slime', 'Current_HP': 7, 'Max_HP': 7, 'Attack': 5, 'Defence': 4, 'XP_Gain': 43}
    drakon = {'Name': "Drakon", 'Current_HP': 256, 'Max_HP': 256, 'Attack': 82, 'Defence': 54}
    rand_num = random.randint(0, 1)
    enemies = [varyan, guard, imp, goblin, slime, drakon]
    harbour_guard = []
    selection = filter(filtered_enemies, enemies)
    for enemy in enemies:
        harbour_guard.append(enemy)
    final_selection = harbour_guard[rand_num]
    if character['X'] == 2 and character['Y'] == 3:
        return varyan
    if character['X'] == 4 and character['Y'] == 3 and character['Level'] == 3:
        return drakon
    if character['X'] == 0 and character['Y'] == 4:
        return final_selection
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
                    ▓─ Æ.█████▀ ▀███▓▄╬▀████╬▓▓██████▀╙▀███▓─
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
    time.sleep(2)
    print(f'Drakon: PATHETIC!')
    time.sleep(2)
    print(f'Drakon: Let me show you what true power looks like')
    time.sleep(2)
    print(f'\n\nDrakon uses Spacial Magic: Eternal Space')
    time.sleep(2)
    print(f'\n\nYou feel the ground shaking from below and notice cracks start to form on the floor. Everything begins to shake...')
    time.sleep(5)
    print(f'Drakon: WELCOME TO MY DOMAIN')
    time.sleep(2)
    print(f'You feel weak! Your attacks do half damage to Drakon... Annoying!')
    time.sleep(1)
    while enemy['Current_HP'] > 100:
        print(enemy)
        if character['Current_HP'] < 0:
            print(f'GAME OVER! Drakon still reigns over the land and your story comes to an unfortunate end...')
            print(f'\nThanks for playing!')
            sys.exit()
        print("What's your move?")
        for i in enumerate(character['Move_Set']):
            print(i)
        user_choice = int(input(''))
        if user_choice == 0:
            print(f'You ran away! What a bummer...')
            print(f"You lose {enemy['Attack']} HP")
            character['Current_HP'] -= enemy['Attack']
            return None
        elif user_choice < len(character['Move_Set'].keys()):
            move = (character['Move_Set'][list(character['Move_Set'].keys())[user_choice]]) // 2
            enemy['Current_HP'] -= move
            character['Current_HP'] -= enemy['Attack']
            print(f'You dealt', move, 'Damage!')
            print(f'')
            if random.randint(0, 1) == 1:
                character['Current_HP'] -= enemy['Attack']
                print(f"{enemy['Name']} dealt {enemy['Attack']} damage!")
            else:
                print(f"{enemy['Name']} missed!")
        else:
            print(f"Invalid selection, please select a number from the move set")
    print(f'\n\nDrakon: ARRGH')
    time.sleep(2)
    print(f"{character['Name']}: It's time to put an end to this")
    time.sleep(2)
    print(f"Drakon: IT'S")
    time.sleep(2)
    print(f"Drakon: NOT")
    time.sleep(2)
    print(f"Drakon: OVER")
    time.sleep(2)
    print(f"\n\nDrakon Uses: ᚷᛁᚨᚾᛏ ᚠᛟᚱᛗᚢᛚᚨ\n\n")
    time.sleep(2)
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
    time.sleep(2)
    print(f"\n\nDrakon is in his giant form. His hits deal a lot of damage, but he has a low chance of hitting. "
          f"You feel a rush of fury over you! Your attacks do normal damage and you gain a x2 health boost")
    enemy['Current_HP'] = enemy['Max_HP'] * 3
    enemy['Attack'] = 119
    character['Current_HP'] = character['Max_HP'] * 2
    while enemy['Current_HP'] > 0:
        if character['Current_HP'] <= 0:
            print(f'GAME OVER! Drakon still reigns over the land and your story comes to an unfortunate end...')
            print(f'\nThanks for playing!')
            sys.exit()
        print("What's your move?")
        for i in enumerate(character['Move_Set']):
            print(i)
        user_choice = int(input(''))
        if user_choice == 0:
            print(f'You ran away! What a bummer...')
            print(f"You lose {enemy['Attack']} HP")
            character['Current_HP'] -= enemy['Attack']
            return None
        elif user_choice < len(character['Move_Set'].keys()):
            move = (character['Move_Set'][list(character['Move_Set'].keys())[user_choice]]) // 2
            enemy['Current_HP'] -= move
            character['Current_HP'] -= enemy['Attack']
            print(f'You dealt', move, 'Damage!')
            print(f'')
            if random.randint(0, 1) == 1:
                character['Current_HP'] -= enemy['Attack']
                print(f"{enemy['Name']} dealt {enemy['Attack']} damage!")
            else:
                print(f"{enemy['Name']} missed!")
        else:
            print(f"Invalid selection, please select a number from the move set")
    print(f"Drakon: HOW")
    time.sleep(2)
    print(f"{character['Name']}: Your reign ends here Drakon. Entia wont have to worry about you any longer")
    time.sleep(2)
    call = list(itertools.repeat('DAMN IT', 10))
    string = ''
    for i in call:
        string += ' ' + i

    print(string)
    time.sleep(2)
    print(f"What's your move?")
    for i in enumerate(character['Move_Set']):
        print(i)
    user_choice = int(input(''))
    move = (character['Move_Set'][list(character['Move_Set'].keys())[user_choice]])
    print(f'You chose', list(character["Move_Set"].keys())[user_choice])
    time.sleep(2)
    print(f'Drakon: ARRGHHHHH')
    character['Boss_Status'] = 'Dead'
    return None


def check_if_goal_attained(character: dict) -> bool:
    if character['Boss_Status'] == 'Dead':
        return True
    else:
        return False


def character_has_leveled(character: dict) -> bool:
    if character['XP'] >= 500:
        print(' ▄█          ▄████████  ▄█    █▄     ▄████████  ▄█            ███    █▄     ▄███████▄ \n'
              '███         ███    ███ ███    ███   ███    ███ ███            ███    ███   ███    ███ \n'
              '███         ███    █▀  ███    ███   ███    █▀  ███            ███    ███   ███    ███ \n'
              '███        ▄███▄▄▄     ███    ███  ▄███▄▄▄     ███            ███    ███   ███    ███ \n'
              '███       ▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀     ███            ███    ███ ▀█████████▀  \n'
              '███         ███    █▄  ███    ███   ███    █▄  ███            ███    ███   ███        \n'
              '███▌    ▄   ███    ███ ███    ███   ███    ███ ███▌    ▄      ███    ███   ███        \n'
              '█████▄▄██   ██████████  ▀██████▀    ██████████ █████▄▄██      ████████▀   ▄████▀      \n'
              '▀                                              ▀                                      ')
        character['XP'] -= 500
        character['Level'] += 1
        if character['Level'] == 3:
            print(f"Great job {character['Name']}! The cloudy skies start to darken at Drakon's Castle (4, 3)"
                  f" Its time to put an end to the wrath put down on Entia.")
            return True
        else:
            print(f"Great job {character['Name']}! You are one step away from Drakon.")
            return True


def execute_glow_up_protocol(character: dict) -> dict:
    if character['Class'] == 'Samurai':
        character['Current_HP'] += 56
        character['Max_HP'] += 56
        character['Attack'] += 35
        character['Defence'] += 12
    elif character['Class'] == 'Berserker':
        character['Current_HP'] += 67
        character['Max_HP'] += 67
        character['Attack'] += 27
        character['Defence'] += 21
    elif character['Class'] == 'Sorcerer':
        character['Current_HP'] += 48
        character['Max_HP'] += 48
        character['Attack'] += 40
        character['Defence'] += 11
    elif character['Class'] == 'Elementalist':
        character['Current_HP'] += 73
        character['Max_HP'] += 73
        character['Attack'] += 25
        character['Defence'] += 18
    elif character['Class'] == 'Paladin':
        character['Current_HP'] += 165
        character['Max_HP'] += 165
        character['Attack'] += 20
        character['Defence'] += 28
    return character


def game(): # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    story()
    character = make_character("Player name")
    player_stats(character)
    player_move_set(character)
    achieved_goal = False
    describe_current_location(board, character)
    while not achieved_goal:
        # Tell the user where they are
        # location = describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(character)
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled(character):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print('Invalid direction! Try again... ')
    print(f'GAME OVER: GOOD ENDING! \nYou beat Drakon and brought peace to Entia')


def main():
    game()


if __name__ == '__main__':
    main()
