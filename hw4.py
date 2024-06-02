def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    if cmd in ["add", "change"]:
        if len(args) < 1:  
            return None, None, None
    return cmd, *args

# Создаем декоратор для обработки ошибок ввода юзеров
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # Обработка ошибок KeyError, ValueError и IndexError
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments for 'add' command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments for 'change' command."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Wrong value."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome, USER! This is your personal bot!")
    while True:
        user_input = input("Enter your command: ")
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
            print("Invalid command.")


if __name__ == "__main__":
    main()
