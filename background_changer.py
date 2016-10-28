# Author Conor O'Kelly
# Given a specifc directory should run so that it returns a random picture and set this as the background


import os
import subprocess
import random
import time

def main():

    while True:
        set_background_to_random_picture("/Users/cokelly/Google_Drive/Google Photos/Sorted Photos")
        time.sleep(5)

def set_background_to_random_picture(searchDirectroy):

    # Get a directory of mainly photos
    pictureDirectroy = get_random_directory_of_mainly_pictures(searchDirectroy)

    # Exclude certian directories
    banned_list = ["/Users/cokelly/Google_Drive/Google Photos/Sorted Photos/100 sleeps of Eduardo", "/Users/cokelly/Google_Drive/Google Photos/Sorted Photos/Snapchat"]
    if pictureDirectroy in banned_list:
        pictureDirectroy = get_random_directory_of_mainly_pictures(searchDirectroy)

    # Get random picture
    picture_path = get_random_picture_link(pictureDirectroy)

    # Set background
    if picture_path != None:
        change_background(picture_path)

def get_random_directory_of_mainly_pictures(searchDirectory):

    # Set starting directory
    searchDirectory = "/Users/cokelly/Google_Drive/Google Photos/Sorted Photos"

    # If directory contains mainly files

    mostly_files = has_mainly_files_in_directory(searchDirectory)

    while mostly_files:


        # Get list of directories in current directory and choose one at random
        list_directores = [file for file in os.listdir(searchDirectory) if os.path.isdir(searchDirectory+"/"+file) == True]

        position = int(len(list_directores)*random.random())

        searchDirectory = searchDirectory + "/" + list_directores[position]

        # print(list_directores, position, searchDirectory, "\n\n")


        # Check if mostly files
        mostly_files = has_mainly_files_in_directory(searchDirectory)

    # print(searchDirectory)
    return searchDirectory



def change_background(file_location):

    os_command = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" +file_location + "\"'"
    os.system(os_command)



def get_random_picture_link(search_directory):
    """Return a random picture from the serach directory"""

    print(search_directory)
    # Check that the directory contents is not all directories
    file_list = os.listdir(search_directory)
    # for i in file_list: print(os.path.isdir(search_directory + "/" + i))

    # Get list of non hidden files from directory and end with .jpg
    picture_file_list = [file for file in os.listdir(search_directory) if file[0] != "." and file[-3:].lower() == "jpg"]

    # print(file_list)
    position = int(len(picture_file_list)*random.random())

    if len(picture_file_list) > 0:
        choosen_photo_path = search_directory + "/" + picture_file_list[position]
    else:
        choosen_photo_path = None

    return choosen_photo_path


def has_mainly_files_in_directory(search_directory):

    # Get file list in current path
    file_list = os.listdir(search_directory)

    # Determine if first 10 files are majority direcories. If so condlue files only contains directories and move to subfolder
    no_directories = 0
    if len(file_list) < 10:
        searchLength = len(file_list)
    else:
        searchLength = 10

    for new_path in file_list[0:searchLength]:

        if (os.path.isdir(search_directory + "/" + new_path)):
            no_directories += 1

    if (no_directories / searchLength) > 0.5:
        return True
    else:
        return False


if __name__=='__main__':

    main()

