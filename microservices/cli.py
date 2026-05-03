import requests

BASE_URL = "http://localhost:8000"

def main():
    while True:
        print("\n1. Create Account\n2. Check Balance\n3. Transfer\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            account_id = input("Account ID: ")
            balance = float(input("Initial Balance: "))
            response = requests.post(f"{BASE_URL}/accounts", json={"account_id": account_id, "initial_balance": balance})
            print(response.json())
        elif choice == "2":
            account_id = input("Account ID: ")
            response = requests.get(f"{BASE_URL}/accounts/{account_id}/balance")
            print(response.json())
        elif choice == "3":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount: "))
            response = requests.post(f"{BASE_URL}/transfer", json={"from_account": from_acc, "to_account": to_acc, "amount": amount})
            print(response.json())
        elif choice == "4":
            break

if __name__ == "__main__":
    main()