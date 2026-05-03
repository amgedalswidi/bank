"""
Spaghetti version: intentionally mixed concerns in one file.
This file demonstrates why unstructured code is hard to maintain.
"""

import logging


logging.basicConfig(
    filename="spaghetti.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Mock data (global state)
accounts = {
    1: {"name": "amgad ", "balance": 1000.0},
    2: {"name": "amer", "balance": 500.0},
    3: {"name": "ahmad", "balance": 200.0},
}


def create_account(account_id, name, initial_balance):
    if account_id in accounts:
        return False, "Account already exists"
    if initial_balance < 0:
        return False, "Initial balance cannot be negative"
    accounts[account_id] = {"name": name, "balance": float(initial_balance)}
    logging.info("Created account id=%s name=%s balance=%s", account_id, name, initial_balance)
    return True, "Account created"


def show_balance(account_id):
    if account_id not in accounts:
        return False, "Account not found"
    balance = accounts[account_id]["balance"]
    logging.info("Checked balance id=%s balance=%s", account_id, balance)
    return True, balance


def transfer_money(from_id, to_id, amount):
    if from_id not in accounts or to_id not in accounts:
        logging.warning("Transfer failed. Account missing from=%s to=%s", from_id, to_id)
        return False, "Account not found"
    if amount <= 0:
        return False, "Amount must be greater than zero"
    if accounts[from_id]["balance"] < amount:
        logging.warning("Transfer failed. Insufficient funds from=%s amount=%s", from_id, amount)
        return False, "Insufficient balance"
    accounts[from_id]["balance"] -= amount
    accounts[to_id]["balance"] += amount
    logging.info("Transfer success from=%s to=%s amount=%s", from_id, to_id, amount)
    return True, "Transfer successful"


def _print_menu():
    print("\n=== Spaghetti Bank CLI ===")
    print("1) Create account")
    print("2) Show balance")
    print("3) Transfer money")
    print("4) List accounts")
    print("0) Exit")


def _list_accounts():
    print("\nAccounts:")
    for account_id, data in accounts.items():
        print(f"- id={account_id}, name={data['name']}, balance={data['balance']}")


def main():
    while True:
        _print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                account_id = int(input("Account ID: ").strip())
                name = input("Name: ").strip()
                initial_balance = float(input("Initial balance: ").strip())
                ok, message = create_account(account_id, name, initial_balance)
                print(message if ok else f"Error: {message}")
            except ValueError:
                print("Invalid input")

        elif choice == "2":
            try:
                account_id = int(input("Account ID: ").strip())
                ok, result = show_balance(account_id)
                print(f"Balance: {result}" if ok else f"Error: {result}")
            except ValueError:
                print("Invalid input")

        elif choice == "3":
            try:
                from_id = int(input("From account ID: ").strip())
                to_id = int(input("To account ID: ").strip())
                amount = float(input("Amount: ").strip())
                ok, message = transfer_money(from_id, to_id, amount)
                print(message if ok else f"Error: {message}")
            except ValueError:
                print("Invalid input")

        elif choice == "4":
            _list_accounts()

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
