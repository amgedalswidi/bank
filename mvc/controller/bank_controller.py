import logging

from mvc.model.account import Account
from mvc.model.repository import AccountRepository


class BankController:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def create_account(self, account_id: int, name: str, initial_balance: float):
        if initial_balance < 0:
            return False, "Initial balance cannot be negative"
        account = Account(id=account_id, name=name, balance=initial_balance)
        if not self.repository.add_account(account):
            return False, "Account already exists"
        logging.info("MVC create account id=%s", account_id)
        return True, "Account created"

    def show_balance(self, account_id: int):
        account = self.repository.get(account_id)
        if not account:
            return False, "Account not found"
        logging.info("MVC show balance id=%s balance=%s", account_id, account.balance)
        return True, account.balance

    def transfer(self, from_id: int, to_id: int, amount: float):
        if amount <= 0:
            return False, "Amount must be greater than zero"
        from_account = self.repository.get(from_id)
        to_account = self.repository.get(to_id)
        if not from_account or not to_account:
            return False, "Account not found"
        if from_account.balance < amount:
            return False, "Insufficient balance"

        from_account.balance -= amount
        to_account.balance += amount
        logging.info("MVC transfer from=%s to=%s amount=%s", from_id, to_id, amount)
        return True, "Transfer successful"
