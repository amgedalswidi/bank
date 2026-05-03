from fastapi import FastAPI, HTTPException
from microservices.services.account_service import AccountService
from microservices.services.validation_service import ValidationService
from microservices.services.transaction_service import TransactionService

app = FastAPI()
account_service = AccountService()
validation_service = ValidationService()
transaction_service = TransactionService(account_service, validation_service)

@app.post("/accounts")
def create_account(account_id: int, name: str, initial_balance: float = 0.0):
    ok, message = account_service.create_account(account_id, name, initial_balance)
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    return {"message": message}

@app.get("/accounts/{account_id}/balance")
def get_balance(account_id: int):
    balance = account_service.get_balance(account_id)
    if balance is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, "balance": balance}

@app.post("/transfer")
def transfer(from_account: int, to_account: int, amount: float):
    ok, message = transaction_service.transfer(from_account, to_account, amount)
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    return {"message": message}

@app.get("/accounts")
def list_accounts():
    return account_service.list_accounts()