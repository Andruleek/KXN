import re

contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError as ve:
            return str(ve)
        except IndexError:
            return "Contact not found"
        
    return wrapper

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(name, phone):
    invalid_names = ["adder", "vo", "don", "vov"]
    if any(invalid_name in name.lower() for invalid_name in invalid_names):
        raise ValueError(f"Error: invalid name '{name}'. Please use a different name.")
    
    for existing_name in contacts:
        if name.capitalize() in existing_name or existing_name in name.capitalize():
            raise ValueError(f"Error: contact {existing_name} already exists.")
    
    contacts[name.capitalize()] = phone
    return f"Contact {name.capitalize()} added successfully."

@input_error
def change_phone(name, new_phone):
    if name.capitalize() not in contacts:
        raise ValueError(f"Error: contact {name.capitalize()} not found.")
    
    contacts[name.capitalize()] = new_phone
    return f"Phone number for {name.capitalize()} updated successfully."

@input_error
def get_phone(name):
    return f"The phone number for {name.capitalize()}: {contacts.get(name.capitalize(), 'not found')}."

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
            _, name, phone = re.split(r'\s+', user_input, 2)
            print(add_contact(name, phone))

        elif user_input.startswith("change"):
            _, name, new_phone = re.split(r'\s+', user_input, 2)
            print(change_phone(name, new_phone))

        elif user_input.startswith("phone"):
            _, name = re.split(r'\s+', user_input, 1)
            print(get_phone(name))

        elif user_input == "show all":
            print(show_all())

        elif any(invalid_name in user_input for invalid_name in ["adder", "add vo", "add don", "add vov"]):
            raise ValueError(f"Error: invalid command '{user_input}'. Please use a different command.")

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()