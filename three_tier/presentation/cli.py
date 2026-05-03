import logging

from three_tier.business.service import TransferService
from three_tier.data.repository import AccountRepository


def run_cli():
    logging.basicConfig(
        filename="three_tier.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    service = TransferService(AccountRepository())

    while True:
        print("\n=== Three-Tier Bank CLI ===")
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
                ok, message = service.create_account(account_id, name, initial_balance)
                print(message if ok else f"Error: {message}")

            elif choice == "2":
                account_id = int(input("Account ID: ").strip())
                ok, result = service.show_balance(account_id)
                print(f"Balance: {result}" if ok else f"Error: {result}")

            elif choice == "3":
                from_id = int(input("From account ID: ").strip())
                to_id = int(input("To account ID: ").strip())
                amount = float(input("Amount: ").strip())
                ok, message = service.transfer(from_id, to_id, amount)
                print(message if ok else f"Error: {message}")

            elif choice == "4":
                all_accounts = service.repository.all_accounts()
                for account_id, data in all_accounts.items():
                    print(f"- id={account_id}, name={data['name']}, balance={data['balance']}")

            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    run_cli()
