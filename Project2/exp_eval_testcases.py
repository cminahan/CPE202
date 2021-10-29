# Project 2
# Name: Claire Minahan
# Section: CPE202-03

from exp_eval import*
from stack_array import*
import unittest

class TestProject2(unittest.TestCase):

    def test_stack_array(self):
        stack = StackArray()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)

    def test_postfix_eval(self):
        input_str = ' 5 1 2 + 4 ^ + 3 - '
        self.assertEqual(postfix_eval(input_str), 83)
        input_str2 = '8 4 2 / *'
        self.assertEqual(postfix_eval(input_str2), 4)
        input_str3 = '0 3 /'
        self.assertRaises(ValueError, postfix_eval, input_str3)

    def test_infix_to_postfix(self):
        input_str = ' 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
        result_exp = '3 4 2 * 1 5 - 2 3 ^ ^ / + '
        self.assertEqual(infix_to_postfix(input_str), result_exp)
        input_str2 = ' 9 * 4 - 2 - ( 4 / 2 ) ^ 1 7'
        result_exp2 = '9 4 * 2 - 4 2 / 1 7 ^ - '
        self.assertEqual(infix_to_postfix(input_str2), result_exp2)

    def test_prefix_to_postfix(self):
        result_exp = '3 2 1 / - 4 5 / 6 - *'
        input_str = '* - 3 / 2 1 - / 4 5 6'
        self.assertEqual(prefix_to_postfix(input_str), result_exp)
        input_str2 = '* + 4 7 ^ / 8 2 9'
        result_exp2 = '4 7 + 8 2 / 9 ^ *'
        self.assertEqual(prefix_to_postfix(input_str2), result_exp2)

if __name__ == '__main__':
    unittest.main()