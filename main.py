from decorators import two_commands_func, one_command_func


CONTACTS = {}


@two_commands_func
def add_contact(name, phone):
    if not CONTACTS.get(name):
        CONTACTS[name] = phone
        print(f"'{name}' has been added to contact list")
    else:
        print(f"Contact '{name}' already exist")


@two_commands_func
def change_contact(name, phone):
    if CONTACTS.get(name):
        CONTACTS.update({name: phone})
        print(f"Contact '{name}' has been changed")
    else:
        print(f"Contact '{name}' doesn't exist")


@one_command_func
def show_contact_phone(name):
    get_phone = CONTACTS.get(name)
    if get_phone:
        print(f"{get_phone}")
    else:
        print(f"Contact '{name}' doesn't exist")


def show_all(*args):
    if len(CONTACTS) == 0:
        print("Contact list is empty")
    else:
        for name, phone in CONTACTS.items():
            print(f"Name: {name}, phone: {phone}")


funcs_dict = {
    "hello": lambda: print("How can I help you?"),
    "add": add_contact,
    "change": change_contact,
    "phone": show_contact_phone,
    "show": show_all
}


def send_commands_to_func(main_command, user_input_list):
    """
    Returns a function call with arguments 
    from the user_input_list.

        Parameters:
            main_command (str): the first command (add, change, etc.).
            user_input_list (lst): of other commands depending 
                on the number of elements in the list.

        Returns:
            function call that corresponds to main_command 
                with arguments from the list of commands.
    """
    # Call func with 0 args (hello)
    if len(user_input_list) == 0:
        current_execution = funcs_dict[main_command]
        return current_execution()
    # Call func with 1 arg (show phone number)
    elif len(user_input_list) == 1:
        current_execution = funcs_dict[main_command]
        name = user_input_list[0].title()
        return current_execution(name)
    # Call func with 2 arg (add, change)
    elif len(user_input_list) == 2:
        current_execution = funcs_dict[main_command]
        name = user_input_list[0].title()
        phone = user_input_list[1]
        return current_execution(name, phone)
    else:
        print("Too many commands, try again.")


def handler_app():
    while True:
        user_input = input("Input command: ").lower()

        # Check if user want to exit
        if user_input in ("good bye", "close", "exit"):
            print("Good bye!")
            break
        # Check input is empty
        elif len(user_input) == 0:
            print("Empty input, please try again")
            continue

        # Split user input to list
        user_input_list = user_input.split(" ")
        # Take the main command from user input
        main_command = user_input_list.pop(0)

        # Check the main command is valid
        if main_command not in ("hello", "add", "change", "phone", "show"):
            print(
                f"Unkmnown command '{main_command}'. You can use only 'hello', 'add', 'change', 'phone', 'show all'")
            continue

        send_commands_to_func(main_command, user_input_list)


if __name__ == "__main__":
    handler_app()
