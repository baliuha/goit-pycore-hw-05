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

"""
Parse the user input into command and arguments
"""
def parse_input(user_input: str) -> tuple: 
    # not adding decorator here so it's not masked as invalid command in main loop
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args

"""
Add a new contact to the contacts dictionary
"""
@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone    
    return "Contact added"

"""
Update an existing contact's phone number
"""
@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated"
    
"""
Show the phone number of a contact
"""
@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    return contacts[name]

"""
Show all contacts in the dictionary
"""
@input_error 
def show_all(contacts: dict) -> str:
    # decorator is not needed here for now but added for future consistency
    if not contacts:
        return "No contacts saved"
    return json.dumps(contacts, indent=4)  

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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