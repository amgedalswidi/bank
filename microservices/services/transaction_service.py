import logging

from microservices.services.account_service import AccountService
from microservices.services.validation_service import ValidationService


class TransactionService:
    """Service coordinating transfer across Account + Validation services."""

    def __init__(self, account_service: AccountService, validation_service: ValidationService):
        self.account_service = account_service
        self.validation_service = validation_service

    def transfer(self, from_id: int, to_id: int, amount: float):
        valid_amount, message = self.validation_service.validate_amount(amount)
        if not valid_amount:
            return False, message

        from_account = self.account_service.get_account(from_id)
        to_account = self.account_service.get_account(to_id)
        valid_accounts, message = self.validation_service.validate_accounts_exist(from_account, to_account)
        if not valid_accounts:
            return False, message

        valid_balance, message = self.validation_service.validate_balance(from_account["balance"], amount)
        if not valid_balance:
            logging.warning("Microservices transfer failed (insufficient) from=%s amount=%s", from_id, amount)
            return False, message

        self.account_service.update_balance(from_id, from_account["balance"] - amount)
        self.account_service.update_balance(to_id, to_account["balance"] + amount)
        logging.info("Microservices transfer success from=%s to=%s amount=%s", from_id, to_id, amount)
        return True, "Transfer successful"
