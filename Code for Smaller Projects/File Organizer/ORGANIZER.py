import os
import shutil
#/Users/gurpartapsohal/Downloads
def make_folder ():
    print(os.getcwd())
    path = input("Gimme a Name?")
    new_folder = f'{path}'
    os.mkdir(new_folder)
#make_folder()
def extension_of_file ():
    name_path = "/Users/gurpartapsohal/Downloads"
    list_ext = []
    for filename in os.listdir(name_path):
        path = os.path.splitext(f'/Users/gurpartapsohal/Downloads/{filename}')
        path_with_ext = f'/Users/gurpartapsohal/Downloads/{path[1]}'
        if path[1][1:] != '':
            list_ext.append(path[1][1:].upper())
    ext_set = set(list_ext)
    os.chdir(name_path)
    for i in ext_set:
        os.makedirs(i, exist_ok=True)
    print(ext_set)
    for x in os.listdir():
        if os.path.isfile(x):
            ext = os.path.splitext(x)[1][1:].upper()
            if ext in ext_set:
                shutil.move(x, os.path.join(ext, x))
extension_of_file()