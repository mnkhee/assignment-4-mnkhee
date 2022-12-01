from unittest import TestCase
from unittest.mock import patch
from game import choose_enemy


class Test(TestCase):
    def test_choose_enemy_slime(self):
        character = {'Level': 1, 'X': 2, 'Y': 2, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20,
                     'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        slime = {'Name': 'Slime', 'Current_HP': 7, 'Max_HP': 7, 'Attack': 5, 'Defence': 4, 'XP_Gain': 43}
        actual = choose_enemy(character)
        self.assertEqual(actual, slime)

    def test_choose_enemy_varyan(self):
        character = {'Level': 1, 'X': 2, 'Y': 3, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20,
                     'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        varyan = {'Name': 'Varyan Warrior', 'Current_HP': 37, 'Max_HP': 37, 'Attack': 18, 'Defence': 17, 'XP_Gain': 177}
        actual = choose_enemy(character)
        self.assertEqual(actual, varyan)

    def test_choose_enemy_drakon(self):
        character = {'Level': 3, 'X': 4, 'Y': 3, 'XP': 0, 'Current_HP': 54, 'Max_HP': 54, 'Attack': 34, 'Defence': 20,
                     'Class': 'Basic', 'Move_Set': {'Run': 0, 'Punch': 34}}
        drakon = {'Name': "Drakon", 'Current_HP': 256, 'Max_HP': 256, 'Attack': 82, 'Defence': 54}
        actual = choose_enemy(character)
        self.assertEqual(actual, drakon)
