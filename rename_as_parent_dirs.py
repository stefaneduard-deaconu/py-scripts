import os
import sys
import re
import json


with open('data.json') as json_file:
    json_data = json.load(json_file)
    filenames = json_data['filenames']


def tests():
    # testing the regular expression we use for identifying an already renamed file :D
    # ---> as to avoid name collisions
    print(re.search('pasare[0-9]+\.', 'pasare4jpg'))
    print(re.search('pasare[0-9]+\.', 'pasare4.jpg'))
    print(re.search('pasare[0-9]+\.', 'pasare4a.jpg'))


def mkdirs(dir_path):
    for dir_name in filenames:
        if not os.path.isdir(dir_path + '/' + dir_name):
            os.mkdir(dir_path + '/' + dir_name)


def rename(dir_path):
    # TODO  remove the next presumptions:
    if dir_path[-1] in ['/', '\\']:
        dir_path = dir_path[:-1]
    last_position = max(dir_path.find('/'), dir_path.find('\\'))
    dir_name = dir_path[last_position:]
    #
    for index, filename in enumerate(os.listdir(dir_path)):
        if re.search('{}[0-9]+\.'.format(dir_name), filename):
            file_extension = file.split('.')[1]
            os.rename(dir_path + '/' + filename, dir_path +
                      '/' + str(index) + '.' + file_extension)
    for index, filename in enumerate(os.listdir(dir_path)):
        file_extension = filename.split('.')[1]
        os.rename(dir_path + '/' + filename, dir_path + '/' +
                  dir_name + str(index) + '.' + file_extension)


def main():
    # first we verify the command line arguments
    # out script must be given at least one argument: "the path"
    #   the path is the parent folder for the category folders
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and '-cd' in sys.argv):
        print('The script was given no arguments.\nYou should have minimally passed the desired path where all the "action" will take place.')
        quit()
    path = sys.argv[1]
    # this command line flag specifies that the desired folders should be created
    if '-cd' in sys.argv[2:] or '--create-dirs' in sys.argv[2:]:
        mkdirs(path)
    # the last argument is the file containing the json data:
    # TODO
    for dir in os.listdir(path):
        if os.path.isdir(path + '/' + dir):
            rename(path + '/' + dir)


if __name__ == '__main__':
    main()
