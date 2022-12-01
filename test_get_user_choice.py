from unittest import TestCase
from unittest.mock import Mock, patch
from game import get_user_choice


class Test(TestCase):
    def test_get_user_choice_north(self):
        with patch('builtins.input', new=Mock(return_value='0')):
            assert get_user_choice()

    def test_get_user_choice_east(self):
        with patch('builtins.input', new=Mock(return_value='1')):
            assert get_user_choice()

    def test_get_user_choice_south(self):
        with patch('builtins.input', new=Mock(return_value='2')):
            assert get_user_choice()

    def test_get_user_choice_west(self):
        with patch('builtins.input', new=Mock(return_value='3')):
            assert get_user_choice()
