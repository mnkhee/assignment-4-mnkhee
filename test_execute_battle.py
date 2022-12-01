from unittest import TestCase
from unittest.mock import Mock, patch
from game import execute_battle


class Test(TestCase):
    def test_execute_battle_easy(self):
        character = {'Level': 1, 'X': 2, 'Y': 2, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20, 'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        with patch('builtins.input', new=Mock(return_value='1')):
            execute_battle(character, 'easy')

    def test_execute_battle_medium(self):
        character = {'Level': 2, 'X': 2, 'Y': 2, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20, 'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        with patch('builtins.input', new=Mock(return_value='1')):
            execute_battle(character, 'medium')

    def test_execute_battle_hard(self):
        character = {'Level': 3, 'X': 2, 'Y': 2, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20, 'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        with patch('builtins.input', new=Mock(return_value='1')):
            execute_battle(character, 'hard')

    def test_execute_battle_run(self):
        character = {'Level': 3, 'X': 2, 'Y': 2, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20, 'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        with patch('builtins.input', new=Mock(return_value='0')):
            execute_battle(character, 'easy')