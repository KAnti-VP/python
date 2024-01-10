import os


def display_menu():
    print('\nPlease choose, what would you like to do.')
    options = ['1. List directory content', '2. Create directory', '3. Create txt file',
               '4. Moving one directory up', '5. Enter into subdirectory', '6. Exit program']
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
    return os.getcwd()


def list_dir():
    for i, fd in enumerate(os.listdir(get_current_dir())):
        print(fd.rjust(30), end='')
        if i % 5 == 0:
            print()


def create_dir():
    print('Please enter the name of the new folder:')
    new_dir = input()
    try:
        os.mkdir(new_dir)
        print(f'{new_dir} directory has been created.')
    except FileExistsError:
        print('The directory already exists.')


def create_txt():
    print('Please enter the name of the new text file:')
    new_file = input()
    with open(new_file + '.txt', 'a') as f:
        text = input('Please specify the content of the file. Just press ENTER to finish.')
        while text:
            f.write(text + '\n')
            text = input()
    print(f'{new_file} file has been created.')


def parent_dir():
    os.chdir('..')


def sub_dir():
    path = get_current_dir()
    folders = [itm for itm in os.listdir(path) if not os.path.isfile(os.path.join(path, itm)) and itm[0] not in '._']
    while True:
        for i, fd in enumerate(folders, 1):
            print(f'{i}. {fd}')
        option = input('Please enter the number of folder: ')
        if option.isdigit():
            op = int(option)
            if 0 < op < len(folders):
                os.chdir(folders[op-1])
                break
        print('The value is incorrect.\n')


def ends():
    print('Good luck.')


if __name__ == '__main__':
    is_run = True
    while is_run:
        display_menu()
        print(get_current_dir())
        is_run, function = chooser()
        function()
