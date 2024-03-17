import re


def input_error(func):
    """Checks if input format is correct and messages if not so"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Wrong format."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid index."

    return inner

@input_error
def parse_input(user_input):
    """
    🔷 Defines command and arguments
    """
    if not user_input.strip():  # Перевіряємо, чи рядок не є пустим або не містить лише пробіли
        return None
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """
    🔷 Adds contact to contact list or changes the existing one 
    """
    name, phone = args
    name_pattern = re.compile(r"^[a-zA-Zа-яА-Я]{3}[a-zA-Zа-яА-Я0-9]*$")

    if name_pattern.match(name):
        if name in contacts:
            return "This name already exist. If you want update contact, use command 'change' {Name} {New Phone}"
        elif re.fullmatch(r"^[+]?[0-9]+$", phone):
            contacts[name] = phone 
            return "Contact added."
        else:
            return "Wrong format of phone numer."
    else:
        return "Wrong format of Name."

@input_error    
def change_contact(args, contacts):
    """
    🔷 Changes contact`s phone number if such contact is in contact list
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."             
    else:
        return "This name wasn't found. If you want add new contact ,use command 'add' {Name} {New Phone}"
    
@input_error
def delete_contact(args, contacts):
    """
    🔷 Deletes contact if it is in contact list
    """
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    return "No such contact."

@input_error
def show_phone(args, contacts):
    """
    🔷 Shows contact`s phone number if such contact is in contact list
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "This name wasn't found."

@input_error
def show_all(contacts):
    """
    🔷 Shows all contacts in contact list
    """
    if contacts:
        all_contacts = ""
        for key, value in contacts.items():
            all_contacts += f"{key}: {value}\n"
        return all_contacts.rstrip("\n")
    else:
        return "You don't have any contact yet"

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit", "goodbye"]:
            # 🔷 ВИХІД. Команда "close" або "exit". Вивід: "Good bye!" та завершення роботи бота
            print("Good bye!")
            break
        elif command == "hello":
            # 🔷 ПРИВІТАННЯ                   
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "delete":  
            print(delete_contact(args, contacts))    
        elif command == "all":
            print(show_all(contacts))
        else:
            # 🔷 КОМАНДИ ЩО НЕ ВІДПОВІДАЮТЬ ФОРМАТАМ. Вивід: "Invalid command."
            print("Invalid command.")

if __name__ == "__main__":
    main()