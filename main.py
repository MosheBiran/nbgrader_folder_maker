from shutil import copy
from os import listdir, mkdir, rename
from os.path import isfile, join

origin_path = 'C:\\Users\\biran\\Desktop\\sub'
destination_path = 'G:\\Shared drives\\IR2021_2022_Staff\\Assignments\\IR2021_2022\\submitted'
# destination_path = 'C:\\Users\\biran\\Desktop\\submitted'
assignment_num = ''
assignment_name = "assignment_" + assignment_num


def folder_reader():

    # Creates a submission folder if it does not exist in the system
    try:
        mkdir(destination_path)
    except OSError as error:
        pass

    # Goes through all the student submissions files and creates folders according to the required format
    for f in listdir(origin_path):
        if isfile(join(origin_path, f)):
            student_id_path = join(destination_path, f.replace(".ipynb", ''))

            # If the student does not have a submission folder he creates a new folder for him
            try:
                mkdir(student_id_path)
            except OSError as error:
                pass

            # Creates a new path for the current job according to the student's ID
            student_id_path = join(student_id_path, assignment_name)

            # If the student does not have a folder for the current job it is more for him
            try:
                mkdir(student_id_path)
            except OSError as error:
                pass

            # Copies the student submission file to the newly created folder

            copy(join(origin_path, f), student_id_path)
            rename(join(student_id_path, f), join(student_id_path, assignment_name+".ipynb"))


def main():

    global assignment_num
    global origin_path
    global destination_path
    global assignment_name
    assignment_num = input("Please enter assignment number:\n")
    assignment_name = "assignment_" + assignment_num
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
