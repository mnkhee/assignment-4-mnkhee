from unittest import TestCase
from unittest.mock import Mock, patch
from game import make_character


class Test(TestCase):
    def test_make_character(self):
        with patch('builtins.input', new=Mock(return_value='0')):
            assert make_character()
