# Author Conor O'Kelly
# Given a specifc directory should run so that it returns a random picture and set this as the background


import os
import subprocess

def main():

    change_background("/Users/cokelly/Google_Drive/Code/small_jobs/test.jpg")

def change_background(file_location):

    os_command = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" +file_location + "\"'"
    os.system(os_command)


if __name__=='__main__':

    main()

