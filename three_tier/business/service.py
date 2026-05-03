import logging

from three_tier.data.repository import AccountRepository


class TransferService:
    """Business Layer: transfer rules and validation."""

    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def create_account(self, account_id: int, name: str, initial_balance: float):
        if initial_balance < 0:
            return False, "Initial balance cannot be negative"
        ok = self.repository.create(account_id, name, initial_balance)
        return (True, "Account created") if ok else (False, "Account already exists")

    def show_balance(self, account_id: int):
        balance = self.repository.get_balance(account_id)
        if balance is None:
            return False, "Account not found"
        return True, balance

    def transfer(self, from_id: int, to_id: int, amount: float):
        if amount <= 0:
            return False, "Amount must be greater than zero"
        if not self.repository.exists(from_id) or not self.repository.exists(to_id):
            return False, "Account not found"

        from_balance = self.repository.get_balance(from_id)
        to_balance = self.repository.get_balance(to_id)
        if from_balance < amount:
            logging.warning("BLL transfer failed (insufficient) from=%s amount=%s", from_id, amount)
            return False, "Insufficient balance"

        self.repository.update_balance(from_id, from_balance - amount)
        self.repository.update_balance(to_id, to_balance + amount)
        logging.info("BLL transfer success from=%s to=%s amount=%s", from_id, to_id, amount)
        return True, "Transfer successful"
