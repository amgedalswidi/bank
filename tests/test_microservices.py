import unittest

from microservices.services.account_service import AccountService
from microservices.services.transaction_service import TransactionService
from microservices.services.validation_service import ValidationService


class TestMicroservices(unittest.TestCase):
    def setUp(self):
        self.account_service = AccountService()
        self.validation_service = ValidationService()
        self.transaction_service = TransactionService(self.account_service, self.validation_service)

    def test_successful_transfer(self):
        ok, message = self.transaction_service.transfer(1, 2, 100)
        self.assertTrue(ok)
        self.assertEqual(message, "Transfer successful")
        self.assertEqual(self.account_service.get_balance(1), 900.0)
        self.assertEqual(self.account_service.get_balance(2), 600.0)

    def test_insufficient_balance(self):
        ok, message = self.transaction_service.transfer(3, 2, 300)
        self.assertFalse(ok)
        self.assertEqual(message, "Insufficient balance")

    def test_account_not_found(self):
        ok, message = self.transaction_service.transfer(999, 2, 10)
        self.assertFalse(ok)
        self.assertEqual(message, "Account not found")


if __name__ == "__main__":
    unittest.main()
