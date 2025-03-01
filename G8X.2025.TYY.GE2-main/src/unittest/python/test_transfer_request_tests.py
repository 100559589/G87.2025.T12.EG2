"""class for testing the regsiter_order method"""
import unittest
import sys
import os

# Dynamically add the main source folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../main/python')))

# Now import the module
from uc3m_money import AccountManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_iban(self):
        self.assertEqual(AccountManager.validate_iban(200), True)


if __name__ == '__main__':
    unittest.main()
