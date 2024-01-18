import re

contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Invalid command. Please try again."
    return wrapper

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(name, phone):
    if name in contacts:
        raise ValueError("Contact already exists.")
    contacts[name] = phone
    return f"Contact {name} added successfully."

@input_error
def change_phone(name, new_phone):
    if name not in contacts:
        raise KeyError("Contact not found.")
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
            
            _, name, phone = user_input.split(maxsplit=2)
            print(add_contact(name, phone))
            

        elif user_input.startswith("change"):
            
            _, name, new_phone = user_input.split(maxsplit=2)
            print(change_phone(name, new_phone))
            

        elif user_input.startswith("phone"):
            
            _, name = user_input.split(maxsplit=1)
            print(get_phone(name))
            

        elif user_input == "show all":
            print(show_all())

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()


