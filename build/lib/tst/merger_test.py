import unittest
from unittest.mock import patch
from contacts_merge_and_fix.solutions.merger import __merged_value as merge_value

class TestMerger(unittest.TestCase):

    @patch('builtins.input', lambda *args: 'l')
    def test_merged_value_left(self):
        merged_value = merge_value('Mobile', '123', '456')
        self.assertEqual(merged_value, '123')
    
    @patch('builtins.input', lambda *args: 'r')
    def test_merged_value_right(self):
        merged_value = merge_value('Mobile', '123', '456')
        self.assertEqual(merged_value, '456')

if __name__ == '__main__':
    unittest.main()