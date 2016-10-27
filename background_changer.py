# Author Conor O'Kelly
# Given a specifc directory should run so that it returns a random picture and set this as the background


import os
import subprocess

def main():

    # change_background("/Users/cokelly/Google_Drive/Code/small_jobs/test.jpg")
    # get_random_picture_link("/Users/cokelly/Google_Drive/Google Photos/Sorted Photos/1. General Catagories")

    # change_background("/Users/cokelly/Google_Drive/Code/small_jobs/test.jpg")
    check_first_10_files("/Users/cokelly/Google_Drive/Google Photos/Sorted Photos/1. General Catagories")

def change_background(file_location):

    os_command = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" +file_location + "\"'"
    os.system(os_command)



def get_random_picture_link(search_directory):
    """Return a random picture from the serach directory"""

    # Check that the directory contents is not all directories
    file_list = os.listdir(search_directory)
    for i in file_list: print(os.path.isdir(search_directory + "/" + i))

    # Get list of non hidden files from directory and end with .jpg
    picture_file_list = [file for file in os.listdir(search_directory) if file[0] != "." and file[-3:] == "jpg"]

    print(file_list)


def has_mainly_pictures_in_directory(search_directory):

    # Get file list in current path
    file_list = os.listdir(search_directory)

    # Determine if first 10 files are majority direcories. If so condlue files only contains directories and move to subfolder
    no_directories = 0
    for new_path in file_list[0:10]:

        if (os.path.isdir(search_directory + "/" + new_path)):
            no_directories += 1

    if (no_directories > 6):
        return True
    else:
        return False


if __name__=='__main__':

    main()

