# Author Conor O'Kelly
# Given a specifc directory should run so that it returns a random picture and set this as the background


import os
import subprocess

def main():

    # change_background("/Users/cokelly/Google_Drive/Code/small_jobs/test.jpg")
    get_random_picture_link("/Users/cokelly/Google_Drive/Google Photos/Sorted Photos/1. General Catagories")

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

if __name__=='__main__':

    main()

