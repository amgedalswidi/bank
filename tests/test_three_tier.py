import unittest

from three_tier.business.service import TransferService
from three_tier.data.repository import AccountRepository


class TestThreeTier(unittest.TestCase):
    def setUp(self):
        self.repo = AccountRepository()
        self.service = TransferService(self.repo)

    def test_successful_transfer(self):
        ok, message = self.service.transfer(1, 2, 100)
        self.assertTrue(ok)
        self.assertEqual(message, "Transfer successful")
        self.assertEqual(self.repo.get_balance(1), 900.0)
        self.assertEqual(self.repo.get_balance(2), 600.0)

    def test_insufficient_balance(self):
        ok, message = self.service.transfer(3, 1, 300)
        self.assertFalse(ok)
        self.assertEqual(message, "Insufficient balance")

    def test_account_not_found(self):
        ok, message = self.service.transfer(999, 1, 10)
        self.assertFalse(ok)
        self.assertEqual(message, "Account not found")


if __name__ == "__main__":
    unittest.main()
