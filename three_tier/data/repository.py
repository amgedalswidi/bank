import logging
from copy import deepcopy


class AccountRepository:
    """Data Access Layer: handles account persistence (mock in-memory store)."""

    def __init__(self):
        self._accounts = {
    1: {"name": "amgad ", "balance": 1000.0},
    2: {"name": "amer", "balance": 500.0},
    3: {"name": "ahmad", "balance": 200.0},
}

    def create(self, account_id: int, name: str, initial_balance: float) -> bool:
        if account_id in self._accounts:
            return False
        self._accounts[account_id] = {"name": name, "balance": float(initial_balance)}
        logging.info("DAL create account id=%s", account_id)
        return True

    def get_balance(self, account_id: int):
        account = self._accounts.get(account_id)
        return None if account is None else account["balance"]

    def exists(self, account_id: int) -> bool:
        return account_id in self._accounts

    def update_balance(self, account_id: int, new_balance: float) -> None:
        self._accounts[account_id]["balance"] = float(new_balance)
        logging.info("DAL update balance id=%s balance=%s", account_id, new_balance)

    def all_accounts(self):
        return deepcopy(self._accounts)
