import unittest
from unittest.mock import patch
from main import create, choose_utensil, choose_length, choose_material, is_monotonic
from utensils.knife import Knife
from utensils.spoon import Spoon
from utensils.fork import Fork
from utensils.tea_spoon import TeaSpoon


class TestUtensilFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='Knife')
    def test_choose_utensil_knife(self, mock_input):
        utensil = choose_utensil()
        self.assertEqual(utensil, 'Knife')

    @patch('builtins.input', return_value='Spoon')
    def test_choose_utensil_spoon(self, mock_input):
        utensil = choose_utensil()
        self.assertEqual(utensil, 'Spoon')

    @patch('builtins.input', return_value='TeaSpoon')
    def test_choose_utensil_teaspoon(self, mock_input):
        utensil = choose_utensil()
        self.assertEqual(utensil, 'TeaSpoon')

    @patch('builtins.input', return_value='Fork')
    def test_choose_utensil_fork(self, mock_input):
        utensil = choose_utensil()
        self.assertEqual(utensil, 'Fork')

    @patch('builtins.input', return_value='20')
    def test_choose_length_valid(self, mock_input):
        length = choose_length()
        self.assertEqual(length, 20)

    @patch('builtins.input', side_effect=['40', '20'])
    def test_choose_length_invalid_then_valid(self, mock_input):
        with self.assertRaises(ValueError):
            choose_length()
        length = choose_length()
        self.assertEqual(length, 20)

    @patch('builtins.input', return_value='gold')
    def test_choose_material_non_monotonic(self, mock_input):
        material = choose_material(False)
        self.assertEqual(material, 'gold')

    @patch('builtins.input', side_effect=['gold', 'silver'])
    def test_choose_material_monotonic(self, mock_input):
        material = choose_material(True)
        self.assertEqual(material, ['gold', 'silver'])

    @patch('builtins.input', return_value='yes')
    def test_is_monotonic_yes(self, mock_input):
        monotonic = is_monotonic()
        self.assertTrue(monotonic)

    @patch('builtins.input', return_value='no')
    def test_is_monotonic_no(self, mock_input):
        monotonic = is_monotonic()
        self.assertFalse(monotonic)

    @patch('builtins.input', side_effect=['Knife', '20', 'yes', 'steel', 'silver'])
    def test_create_knife(self, mock_input):
        utensil = create()
        self.assertIsInstance(utensil, Knife)
        self.assertEqual(utensil.material, ['steel', 'silver'])
        self.assertEqual(utensil.length, 20)
        self.assertTrue(utensil.monotonic)

    @patch('builtins.input', side_effect=['Spoon', '15', 'plastic'])
    def test_create_spoon(self, mock_input):
        utensil = create()
        self.assertIsInstance(utensil, Spoon)
        self.assertEqual(utensil.material, 'plastic')
        self.assertEqual(utensil.length, 15)
        self.assertFalse(utensil.monotonic)

    @patch('builtins.input', side_effect=['Fork', '18', 'gold'])
    def test_create_fork(self, mock_input):
        utensil = create()
        self.assertIsInstance(utensil, Fork)
        self.assertEqual(utensil.material, 'gold')
        self.assertEqual(utensil.length, 18)
        self.assertFalse(utensil.monotonic)

    @patch('builtins.input', side_effect=['TeaSpoon', '10', 'silver'])
    def test_create_teaspoon(self, mock_input):
        utensil = create()
        self.assertIsInstance(utensil, TeaSpoon)
        self.assertEqual(utensil.material, 'silver')
        self.assertEqual(utensil.length, 10)
        self.assertFalse(utensil.monotonic)


if __name__ == '__main__':
    unittest.main()
