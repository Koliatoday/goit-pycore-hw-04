def parse_input(user_input):
    """Parse user input into command and arguments.
    Args:
        user_input (str): The input string from the user.
    Returns:
        tuple: A tuple containing the command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """Add a new contact to the contacts dictionary.
    Args:
        args (list): A list containing the name and phone number.
        contacts (dict): The dictionary to store contacts.
    Returns:
        str: A message indicating the result of the operation."""
    name, phone, *_ = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Change an existing contact's phone number.
    Args:
        args (list): A list containing the name and new phone number.
        contacts (dict): The dictionary to store contacts.
    Returns:
        str: A message indicating the result of the operation."""
    name, phone, *_ = args
    if not (name in list(contacts.keys())):
      return f"Name {name} not in contacts, please create it at first"
    else:
      contacts[name] = phone
      return f"Contact {name} changed the number to {phone}"


def phone_contact(name, contacts):
    """Retrieve a contact's phone number.
    Args:
        name (str): The name of the contact.
        contacts (dict): The dictionary to store contacts.
    Returns:
        str: A message with the contact's phone number or an error message."""
    if not (name in list(contacts.keys())):
      return f"Name {name} not in contacts, please create it at first"
    else:
      return f"{name} phone is {contacts[name]}"


def all_contacts(contacts):
    """Retrieve all contacts in the contacts dictionary.
    Args:
        contacts (dict): The dictionary to store contacts.
    Returns:
        str: A formatted string of all contacts."""
    
    ret = ""
    for name, phone in contacts.items():
       ret = ret + f"{name}:{phone}\n"

    return ret


def main():
    """Main function to run the assistant bot.
    Args: None
    Returns: None """

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
          if len(args) < 2:
            print("Wrong command format, should be: add name phone")
          else:
            print(add_contact(args, contacts))
        elif command == "change":
          if len(args) < 2:
            print("Wrong command format, should be: change name phone")
          else:
            print(change_contact(args, contacts))
        elif command == "phone":
          if len(args) < 1:
            print("Wrong command format, should be: phone name")
          else:
            print(phone_contact(args[0], contacts))
        elif command == "all":
          if (len(contacts) == 0):
            print("There are no contacts in the list")
          else:
            print(all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()