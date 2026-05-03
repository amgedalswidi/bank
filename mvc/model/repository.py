from mvc.model.account import Account


class AccountRepository:
    def __init__(self):
        self._accounts = {
    1: {"name": "amgad ", "balance": 1000.0},
    2: {"name": "amer", "balance": 500.0},
    3: {"name": "ahmad", "balance": 200.0},
}

    def add_account(self, account: Account) -> bool:
        if account.id in self._accounts:
            return False
        self._accounts[account.id] = account
        return True

    def get(self, account_id: int):
        return self._accounts.get(account_id)

    def list_all(self):
        return list(self._accounts.values())
