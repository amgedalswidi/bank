class ValidationService:
    """Service responsible for validating transfer pre-conditions."""

    @staticmethod
    def validate_accounts_exist(from_account, to_account):
        if from_account is None or to_account is None:
            return False, "Account not found"
        return True, "OK"

    @staticmethod
    def validate_amount(amount: float):
        if amount <= 0:
            return False, "Amount must be greater than zero"
        return True, "OK"

    @staticmethod
    def validate_balance(from_balance: float, amount: float):
        if from_balance < amount:
            return False, "Insufficient balance"
        return True, "OK"
