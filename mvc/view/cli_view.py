class CLIView:
    @staticmethod
    def menu():
        print("\n=== MVC Bank CLI ===")
        print("1) Create account")
        print("2) Show balance")
        print("3) Transfer money")
        print("4) List accounts")
        print("0) Exit")
        return input("Choose: ").strip()

    @staticmethod
    def prompt_create():
        account_id = int(input("Account ID: ").strip())
        name = input("Name: ").strip()
        initial_balance = float(input("Initial balance: ").strip())
        return account_id, name, initial_balance

    @staticmethod
    def prompt_balance():
        return int(input("Account ID: ").strip())

    @staticmethod
    def prompt_transfer():
        from_id = int(input("From account ID: ").strip())
        to_id = int(input("To account ID: ").strip())
        amount = float(input("Amount: ").strip())
        return from_id, to_id, amount

    @staticmethod
    def show_message(message):
        print(message)
