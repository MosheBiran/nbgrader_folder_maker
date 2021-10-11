from shutil import copy, move
from os import listdir, mkdir
from os.path import isfile, join

origin_path = 'C:\\Users\\biran\\Desktop\\sub'
destination_path = 'C:\\Users\\biran\\Desktop\\submitted'
assignment_num = ''


def folder_reader():
    # files_names = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    try:
        mkdir(destination_path)
    except OSError as error:
        print(error)

    for f in listdir(origin_path):
        if isfile(join(origin_path, f)):
            student_id_path = join(destination_path, f.replace(".ipynb", ''))

            try:
                mkdir(student_id_path)
            except OSError as error:
                print(error)

            student_id_path = join(student_id_path, "assignment_" + assignment_num)

            try:
                mkdir(student_id_path)
            except OSError as error:
                print(error)

            copy(join(origin_path, f), student_id_path)


def main():

    global assignment_num
    global origin_path
    global destination_path

    assignment_num = input("Please enter assignment number:\n")

    origin_flag = input("Would you like to update the origin path[y/n]\n")
    if origin_flag.lower() == 'y':
        origin_path = input("Please enter new origin path\n")

    destination_flag = input("Would you like to update the destination path[y/n]\n")
    if destination_flag.lower() == 'y':
        destination_path = input("Please enter new destination path\n")

    folder_reader()


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
