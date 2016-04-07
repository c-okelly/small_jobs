<<<<<<< HEAD
import os, sys, getopt

"""
The program will take the location of a directroy from command line. It will then change all of the
"""

def rename_file(directory):
    items_current_directory = []


    # Confrim that user wants to proced
    message = "Please enter y to proceed with change all files in directory " + directory + "\n"
    user_in = input(message)


    if user_in == "y":
        items_current_directory_dirty = os.listdir(directory)
        # Remove hidden files
        for i in items_current_directory_dirty:
            if i[0] != ".":
                items_current_directory.append(i)

        print(items_current_directory)

        for i in items_current_directory:
            new_name = clean_name(i)
            current_locaiton = directory + "/" + i
            new_location = directory + "/" +new_name
            os.renames(current_locaiton,new_location)
    else:
        print("Now exiting")

def clean_name(name):
    name = name.replace("-","")
    name = name.replace(".","")
    name = name.replace("jpg",".jpg")
    name = name.replace(" ", "_")
=======
import os

def rename_file():
    items_current_directory = []

    items_current_directory_dirty = os.listdir()

    # Remove hidden files
    for i in items_current_directory_dirty:
        if i[0] != ".":
            items_current_directory.append(i)

    print(items_current_directory)

    for i in items_current_directory:
        os.renames(i,clean_name(i))

def clean_name(name):
    name = name.replace("png.png",".png")
    name = name.replace("mp4.mp4",".mp4")
>>>>>>> 6f18dcda0697a5d265c33c1359dd85941e33804f

    return name

if __name__ == '__main__':
<<<<<<< HEAD
    try:
        command_line_directory_input = sys.argv[1]
        rename_file(command_line_directory_input)
    except IndexError:
        print("No directory was given")
    except FileNotFoundError:
        print("The directory could not be found")
=======
   rename_file()
>>>>>>> 6f18dcda0697a5d265c33c1359dd85941e33804f
