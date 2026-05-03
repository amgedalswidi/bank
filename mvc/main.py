import logging

from mvc.controller.bank_controller import BankController
from mvc.model.repository import AccountRepository
from mvc.view.cli_view import CLIView


def run_cli():
    logging.basicConfig(
        filename="mvc.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    repo = AccountRepository()
    controller = BankController(repo)
    view = CLIView()

    while True:
        choice = view.menu()
        try:
            if choice == "1":
                account_id, name, initial_balance = view.prompt_create()
                ok, message = controller.create_account(account_id, name, initial_balance)
                view.show_message(message if ok else f"Error: {message}")
            elif choice == "2":
                account_id = view.prompt_balance()
                ok, result = controller.show_balance(account_id)
                view.show_message(f"Balance: {result}" if ok else f"Error: {result}")
            elif choice == "3":
                from_id, to_id, amount = view.prompt_transfer()
                ok, message = controller.transfer(from_id, to_id, amount)
                view.show_message(message if ok else f"Error: {message}")
            elif choice == "4":
                for acc in repo.list_all():
                    view.show_message(f"- id={acc.id}, name={acc.name}, balance={acc.balance}")
            elif choice == "0":
                view.show_message("Bye!")
                break
            else:
                view.show_message("Invalid choice")
        except ValueError:
            view.show_message("Invalid input")


if __name__ == "__main__":
    run_cli()
