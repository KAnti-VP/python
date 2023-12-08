import os


def display_menu():
    print('Please choose, what would you like to do.\n')
    options = ['1. List directory content', '2. Create directory', '3. Create txt file',
               '4. Entzer to parent directory', '5. Enter into subdirectory','6. Exit program']
    for op in options:
        print(op)

def chooser():
    option = input()
    while True:
        if option.isdigit():
            op = int(option)
            if 0 < op < 7:
                return op != 6, [list_dir, create_dir, create_txt, parent_dir, sub_dir, ends][op-1]
        option = input('The value is incorrect.')

def get_current_dir():
    return 'current_dir'

def list_dir():
    print('list_dir')

def create_dir():
    print('create_dir')

def create_txt():
    print('create_txt')

def parent_dir():
    print('parent_dir')

def sub_dir():
    print('sub_dir')

def ends():
    print('Good luck.')

if __name__ == '__main__':
    is_run = True
    while is_run:
        display_menu()
        is_run, function = chooser()
        print(get_current_dir())
        function()