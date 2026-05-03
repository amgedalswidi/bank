class AccountService:
    """Service responsible for account storage and balance operations."""

    def __init__(self):
        self._accounts = {
    1: {"name": "amgad ", "balance": 1000.0},
    2: {"name": "amer", "balance": 500.0},
    3: {"name": "ahmad", "balance": 200.0},
}

    def create_account(self, account_id: int, name: str, initial_balance: float):
        if account_id in self._accounts:
            return False, "Account already exists"
        if initial_balance < 0:
            return False, "Initial balance cannot be negative"
        self._accounts[account_id] = {"name": name, "balance": float(initial_balance)}
        return True, "Account created"

    def get_account(self, account_id: int):
        return self._accounts.get(account_id)

    def get_balance(self, account_id: int):
        account = self.get_account(account_id)
        return None if account is None else account["balance"]

    def update_balance(self, account_id: int, new_balance: float):
        self._accounts[account_id]["balance"] = float(new_balance)

    def list_accounts(self):
        return self._accounts
