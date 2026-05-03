from fastapi import FastAPI, HTTPException
from services.account_service import AccountService
from services.validation_service import ValidationService
from services.transaction_service import TransactionService

app = FastAPI()
account_service = AccountService()
validation_service = ValidationService()
transaction_service = TransactionService()

@app.post("/accounts")
def create_account(account_id: str, initial_balance: float = 0.0):
    account_service.create_account(account_id, initial_balance)
    return {"message": f"Account {account_id} created with balance {initial_balance}"}

@app.get("/accounts/{account_id}/balance")
def get_balance(account_id: str):
    try:
        balance = account_service.get_balance(account_id)
        return {"account_id": account_id, "balance": balance}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/transfer")
def transfer(from_account: str, to_account: str, amount: float):
    try:
        validation_service.validate_transfer(from_account, amount)
        transaction_service.perform_transfer(from_account, to_account, amount)
        return {"message": f"Transferred {amount} from {from_account} to {to_account}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))