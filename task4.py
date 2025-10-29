import json


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter valid arguments for the command"
        except IndexError:
            return "Not enough arguments provided"
        except KeyError:
            return "Contact not found, please try again"
        except Exception as ex:
            return f"An unexpected error occurred: {str(ex)}"
    return inner


def parse_input(user_input: str) -> tuple:
    """
    Parse the user input into command and arguments
    """
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    """
    Add a new contact to the contacts dictionary
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args: list, contacts: dict) -> str:
    """
    Update an existing contact's phone number
    """
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated"


@input_error
def show_phone(args: list, contacts: dict) -> str:
    """
    Show the phone number of a contact
    """
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts: dict) -> str:
    """
    Show all contacts in the dictionary
    """
    # decorator is not needed here for now but added for future consistency
    if not contacts:
        return "No contacts saved"
    return json.dumps(contacts, indent=4)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
