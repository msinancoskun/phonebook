phonebook = {}


def main():
    choices = {1: add_phone,
               2: delete_number,
               3: print_phonebook,
               4: search_number,
               5: change_number,
               6: change_name,
               7: search_name,
               8: exit,
               }
    func_list = ['add_phone', 'delete_number', 'print_phonebook', 'search_number', 'change_number',
                 'change_name', 'search_name', 'exit']
    print("Welcome to your Phonebook!\nWhat do you want to do?")
    index = 1
    for func in func_list:
        print("{}.{}".format(index, func))
        index += 1

    choice = int(input(">"))
    func = choices[choice]
    func()


def add_phone():
    name = input("Provide a name: ")
    number = input("Provide a contact number: ")
    if name and number:
        phonebook[name] = number
    return "{} is added to phonebook".format(name)


def delete_number():
    number_to_delete = input("Whose number do you want to delete?\n")
    for name in list(phonebook.keys()):
        if number_to_delete == name:
            phonebook.pop(name)
            print('{} has been removed from phonebook.'.format(name))
        else:
            print("Couldn't find a number to remove from the book.")


def print_phonebook():
    index = 1
    for key, value in phonebook.items():
        print("{}. Name: {}, Number: {}".format(index, key, value))
        index += 1


def change_number():
    num_to_change = input("Who's number you want to change?\n")
    for name, number in phonebook.items():
        if num_to_change == name:
            which_number = input("Provide new number: ")
            if which_number:
                phonebook[name] = which_number


def change_name():
    name_to_change = input("Whose name you want to change?\n")
    for name in phonebook.keys():
        if name == name_to_change:
            new_name = input("What is the new name to replace?\n")
            phonebook[new_name] = phonebook.pop(name_to_change)
            print("New name is '{}'".format(new_name))


def search_number():
    number_search = input("What is the number you're looking for?\n")
    for name, number in phonebook.items():
        if number == number_search:
            print("You're looking for {}".format(name))
        else:
            print("Number not found!")
            return 1


def search_name():
    name_search = input("What is the name of you want to access?\n")
    for name, number in phonebook.items():
        if name == name_search:
            print("Name: {}, Number: {}".format(name, number))
        else:
            print("Provide a valid name!")


if __name__ == '__main__':
    while True:
        main()
