import copy
import unittest

from spaghetti import bank_spaghetti as sp


class TestSpaghetti(unittest.TestCase):
    def setUp(self):
        self._original = copy.deepcopy(sp.accounts)

    def tearDown(self):
        sp.accounts.clear()
        sp.accounts.update(self._original)

    def test_successful_transfer(self):
        ok, message = sp.transfer_money(1, 2, 100)
        self.assertTrue(ok)
        self.assertEqual(message, "Transfer successful")
        self.assertEqual(sp.accounts[1]["balance"], 900.0)
        self.assertEqual(sp.accounts[2]["balance"], 600.0)

    def test_insufficient_balance(self):
        ok, message = sp.transfer_money(3, 2, 1000)
        self.assertFalse(ok)
        self.assertEqual(message, "Insufficient balance")

    def test_account_not_found(self):
        ok, message = sp.transfer_money(999, 2, 10)
        self.assertFalse(ok)
        self.assertEqual(message, "Account not found")


if __name__ == "__main__":
    unittest.main()
