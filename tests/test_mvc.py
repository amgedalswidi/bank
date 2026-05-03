import unittest

from mvc.controller.bank_controller import BankController
from mvc.model.repository import AccountRepository


class TestMVC(unittest.TestCase):
    def setUp(self):
        self.repo = AccountRepository()
        self.controller = BankController(self.repo)

    def test_successful_transfer(self):
        ok, message = self.controller.transfer(1, 2, 100)
        self.assertTrue(ok)
        self.assertEqual(message, "Transfer successful")
        self.assertEqual(self.repo.get(1).balance, 900.0)
        self.assertEqual(self.repo.get(2).balance, 600.0)

    def test_insufficient_balance(self):
        ok, message = self.controller.transfer(3, 2, 300)
        self.assertFalse(ok)
        self.assertEqual(message, "Insufficient balance")

    def test_account_not_found(self):
        ok, message = self.controller.transfer(999, 2, 10)
        self.assertFalse(ok)
        self.assertEqual(message, "Account not found")


if __name__ == "__main__":
    unittest.main()
