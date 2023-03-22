import os

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('такая папка уже существует')

def get_list():
    print(os.listdir())

def get_list1(Folders_only=False):
    result = os.listdir()
    if Folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f')
    get_list()
    get_list1(True)