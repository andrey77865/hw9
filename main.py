from decorators import trace

supported_commands = ("hello", "add", "change", "phone", "show all")
exit_words = ("good bye", "close", "exit")
contacts = {}


@trace
def add_contact(name, phone):
    contacts[name] = phone
    print(f"{name} {phone} has been added to contact list")


def show_all():
    return contacts


handler = {
    "hello": lambda: print("How can I help you?"),
    "add": add_contact,
    "show all": show_all
}


@trace
def trace_command_to_handler(command):
    # регулярка которая выдергивает команду
    # получив команду, возвращаем команду отдельно и введенные данные строкой
    # if command.startswith("add"):
    splitted_command = command.split(" ")
    command = splitted_command[0]

    if command == "add":
        name = splitted_command[1]
        phone = splitted_command[2]
        # print(f"{command}\n{name}\n{phone}\n")
        return handler[command](name, phone)

    # if command ==


while True:
    user_input = input("Input you command: ").lower()

    if user_input in exit_words:
        print("Good bye!")
        break
    elif user_input not in supported_commands:
        print("Command doesn't supported, please try again")
        continue

    splitted_command = trace_command_to_handler(user_input)
    splitted_command = user_input.split(" ")
    print(splitted_command)
    current_execution = handler[splitted_command[0]]
   # current_execution(splitted_command[1])
   # print(contacts)
