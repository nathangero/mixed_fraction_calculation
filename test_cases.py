'''
Test cases include, default tests provided, single inputs, and equations. Tests also include error testing as well.
'''

from multiprocessing.sharedctypes import Value
import unittest
import check_syntax as c
import custom_errors as e

class TestUser(unittest.TestCase):

    def test_default_tests(self):
        print("** Testing Given Test Cases **")
        
        print("testing: 1/2 * 3&3/4 | expected: 1&7/8")
        self.assertEqual(c.checkSyntax("1/2 * 3&3/4"), "1&7/8")
        
        print("testing: 2&3/8 + 9/8 | expected: 3&1/2")
        self.assertEqual(c.checkSyntax("2&3/8 + 9/8"), "3&1/2")
        
        print("testing: 1&3/4 - 2 | expected: -1/4")
        self.assertEqual(c.checkSyntax("1&3/4 - 2"), "-1/4")
        
        print("testing: 11 % 3 | expected: 2")
        self.assertEqual(c.checkSyntax("11 % 3"), "2")
        
            
    def test_equations_positive(self):
        print("\n** Testing Equation Positive Cases")
        
        # Positive cases
        print("testing: -1&3/4 - 2 | expected: -3&3/4")
        self.assertEqual(c.checkSyntax("-1&3/4 - 2"), "-3&3/4")
        
        print("testing: -1&3/4 - 2 + 3/4 | expected: -3")
        self.assertEqual(c.checkSyntax("-1&3/4 - 2 + 3/4"), "-3")
        
        print("testing: 1 + 2 + 3 | expected: 6")
        self.assertEqual(c.checkSyntax("1 + 2 + 3"), "6")
        
        print("testing: 1 * 2 + 3 | expected: 5")
        self.assertEqual(c.checkSyntax("1 * 2 + 3"), "5")
        
        print("testing: 1 + 2 * 3 | expected: 7")
        self.assertEqual(c.checkSyntax("1 + 2 * 3"), "7")
        
    # Error cases
    def test_equations_error(self):
        print("\n** Testing Equation Error Cases")
        
        print("testing: -1&0.4/4 - 2 | expected: ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("-1&0.4/4 - 2")
            
        print("testing: -1&a/4 - 2 | expected: ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("-1&a/4 - 2")
        
        print("testing: 1 + 2 * a | expected: NameError")
        with self.assertRaises(NameError):
            c.checkSyntax("1 + 2 * a")
        
        print("testing: 1 + 2 * | expected: e.InvalidOperatorOperandSyntax")
        with self.assertRaises(e.InvalidOperatorOperandSyntax):
            c.checkSyntax("1 + 2 *")
        
        print("testing: 1 + * | expected: e.OperatorSyntaxError")
        with self.assertRaises(e.OperatorSyntaxError):
            c.checkSyntax("1 + *")
        
    
    def test_single_inputs_positive(self):
        print("\n** Testing Single Input Positive Cases")
        
        # Positive cases
        print("testing: 2&3/8 | expected: 2&3/8")
        self.assertEqual(c.checkSyntax("2&3/8"), "2&3/8")
        
        print("testing: 2 | expected: 2")
        self.assertEqual(c.checkSyntax("2"), "2")
        
        print("testing: 9/8 | expected: 1&1/8")
        self.assertEqual(c.checkSyntax("9/8"), "1&1/8")
        
    # Error testing
    def test_single_inputs_error(self):
        print("\n** Testing Single Input Error Cases")
        print("testing: a | expected: ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("a")
        
        print("testing: .3 | expected:", "ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax(".3")
        
        print("testing: b/8 | expected:", "ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("b/8")
        
        print("testing: 1&a/8 | expected:", "ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("1&a/8")
        
        print("testing: 0.56 | expected:", "ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("0.56")
        
        print("testing: 1&0.3/3 | expected:", "ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax("1&0.3/3")
        
        print("testing: .3&1/2 | expected:", "ValueError")
        with self.assertRaises(ValueError):
            c.checkSyntax(".3&1/2")
            
        
        
        

if __name__ == '__main__':
    unittest.main()