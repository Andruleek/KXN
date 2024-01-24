from collections import UserDict

class ContactBook(UserDict):
    def __init__(self):
        super().__init__()

    def input_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                return f"Error: {str(e)}"

        return wrapper

    @input_error
    def add_contact(self, name, phone):
        if name.isalpha() and phone.isdigit() and len(phone) == 10:
            self.data[name] = phone
            return f"Contact {name} added successfully."
        else:
            raise ValueError("Invalid name or phone number.")

    @input_error
    def change_contact(self, name, new_phone):
        if name in self.data and new_phone.isdigit() and len(new_phone) == 10:
            self.data[name] = new_phone
            return f"Phone number for {name} changed successfully."
        else:
            raise ValueError("Invalid name or phone number.")

    @input_error
    def show_phone(self, name):
        if name in self.data:
            return f"The phone number for {name} is {self.data[name]}."
        else:
            raise ValueError(f"Contact {name} not found.")

    def show_all(self):
        if not self.data:
            return "No contacts found."
        else:
            return "\n".join([f"{name}: {phone}" for name, phone in self.data.items()])

    def exit_program(self):
        return "Good bye!"

    def main(self):
        while True:
            command = input("Enter your command: ").lower()
            if command in ["good bye", "close", "exit"]:
                print(self.exit_program())
                break
            elif command.startswith("add "):
                _, name, *phone = command.split()
                phone = "".join(phone)
                print(self.add_contact(name, phone))
            elif command.startswith("change "):
                _, name, *new_phone = command.split()
                new_phone = "".join(new_phone)
                print(self.change_contact(name, new_phone))
            elif command.startswith("phone "):
                _, name = command.split()
                print(self.show_phone(name))
            elif command == "show all":
                print(self.show_all())
            elif command == "hello":
                print("How can I help you?")
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.main()