import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Nara", 100)

    def test_deposit(self):
        result = self.account.deposit(50)
        self.assertEqual(result, 150)

    def test_withdraw(self):
        result = self.account.withdraw(30)
        self.assertEqual(result, 70)

    def test_get_balance(self):
        result = self.account.get_balance()
        self.assertEqual(result, 100)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_invalid_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == "__main__":
    unittest.main()
