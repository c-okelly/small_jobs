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

    return name

if __name__ == '__main__':
   rename_file()
