# import logging

# from microservices.services.account_service import AccountService
# from microservices.services.transaction_service import TransactionService
# from microservices.services.validation_service import ValidationService


# def run_cli():
#     logging.basicConfig(
#         filename="microservices.log",
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s",
#     )
#     account_service = AccountService()
#     validation_service = ValidationService()
#     transaction_service = TransactionService(account_service, validation_service)

#     while True:
#         print("\n=== Microservices Bank CLI ===")
#         print("1) Create account")
#         print("2) Show balance")
#         print("3) Transfer money")
#         print("4) List accounts")
#         print("0) Exit")
#         choice = input("Choose: ").strip()

#         try:
#             if choice == "1":
#                 account_id = int(input("Account ID: ").strip())
#                 name = input("Name: ").strip()
#                 initial_balance = float(input("Initial balance: ").strip())
#                 ok, message = account_service.create_account(account_id, name, initial_balance)
#                 print(message if ok else f"Error: {message}")
#             elif choice == "2":
#                 account_id = int(input("Account ID: ").strip())
#                 balance = account_service.get_balance(account_id)
#                 print(f"Balance: {balance}" if balance is not None else "Error: Account not found")
#             elif choice == "3":
#                 from_id = int(input("From account ID: ").strip())
#                 to_id = int(input("To account ID: ").strip())
#                 amount = float(input("Amount: ").strip())
#                 ok, message = transaction_service.transfer(from_id, to_id, amount)
#                 print(message if ok else f"Error: {message}")
#             elif choice == "4":
#                 for account_id, data in account_service.list_accounts().items():
#                     print(f"- id={account_id}, name={data['name']}, balance={data['balance']}")
#             elif choice == "0":
#                 print("Bye!")
#                 break
#             else:
#                 print("Invalid choice")
#         except ValueError:
#             print("Invalid input")
# import requests

# BASE_URL = "http://localhost:8000"

# def main():
#     while True:
#         print("\n1. Create Account\n2. Check Balance\n3. Transfer\n4. Exit")
#         choice = input("Choose: ")
#         if choice == "1":
#             account_id = input("Account ID: ")
#             balance = float(input("Initial Balance: "))
#             response = requests.post(f"{BASE_URL}/accounts", json={"account_id": account_id, "initial_balance": balance})
#             print(response.json())
#         elif choice == "2":
#             account_id = input("Account ID: ")
#             response = requests.get(f"{BASE_URL}/accounts/{account_id}/balance")
#             print(response.json())
#         elif choice == "3":
#             from_acc = input("From Account: ")
#             to_acc = input("To Account: ")
#             amount = float(input("Amount: "))
#             response = requests.post(f"{BASE_URL}/transfer", json={"from_account": from_acc, "to_account": to_acc, "amount": amount})
#             print(response.json())
#         elif choice == "4":
#             break

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     run_cli()
import requests

BASE_URL = "http://localhost:8000"

def main():
    while True:
        print("\n=== Microservices Bank CLI ===")
        print("1) Create account")
        print("2) Show balance")
        print("3) Transfer money")
        print("4) List accounts")
        print("0) Exit")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                account_id = int(input("Account ID: ").strip())
                name = input("Name: ").strip()
                initial_balance = float(input("Initial balance: ").strip())
                response = requests.post(f"{BASE_URL}/accounts", json={"account_id": account_id, "name": name, "initial_balance": initial_balance})
                print(response.json())
            elif choice == "2":
                account_id = int(input("Account ID: ").strip())
                response = requests.get(f"{BASE_URL}/accounts/{account_id}/balance")
                print(response.json())
            elif choice == "3":
                from_id = int(input("From account ID: ").strip())
                to_id = int(input("To account ID: ").strip())
                amount = float(input("Amount: ").strip())
                response = requests.post(f"{BASE_URL}/transfer", json={"from_account": from_id, "to_account": to_id, "amount": amount})
                print(response.json())
            elif choice == "4":
                response = requests.get(f"{BASE_URL}/accounts")
                accounts = response.json()
                for account_id, data in accounts.items():
                    print(f"- id={account_id}, name={data['name']}, balance={data['balance']}")
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")
        except requests.RequestException as e:
            print(f"API Error: {e}")

if __name__ == "__main__":
    main()