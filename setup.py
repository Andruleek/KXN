import re

contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
        
    return wrapper

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(name, phone):
    if name.lower() == "add" and phone.isdigit():
        return "Invalid command. Please try again."
    elif name.lower() == "add" or name.lower() != "adder":
        return "Invalid name. Please choose a different name."
    contacts[name] = phone
    return f"Contact {name} added successfully."


@input_error
def change_phone(name, new_phone):
    contacts[name] = new_phone
    return f"Phone number for {name} updated successfully."

@input_error
def get_phone(name):
    return f"The phone number for {name} is {contacts.get(name, 'not found')}."

@input_error
def show_all():
    if not contacts:
        return "No contacts found."
    else:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result

def main():
    print("Welcome to the Console Assistant!")

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input in ["good bye", "exit", "close"]:
            print("Good bye!")
            break

        elif user_input == "hello":
            print(hello())

        elif user_input.startswith("add"):
            try:
                _, name, phone = re.split(r'\s+', user_input, 2)
                print(add_contact(name, phone))
            except ValueError:
                print("Give me name and phone please")

        elif user_input.startswith("change"):
            try:
                _, name, new_phone = re.split(r'\s+', user_input, 2)
                print(change_phone(name, new_phone))
            except ValueError:
                print("Give me name and new phone please")

        elif user_input.startswith("phone"):
            try:
                _, name = re.split(r'\s+', user_input, 1)
                print(get_phone(name))
            except ValueError:
                print("Give me name please")

        elif user_input == "show all":
            print(show_all())

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()