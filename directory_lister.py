# Author Conor O'Kelly

import os

class DirectoryWalker:

    def fileList(self,target,extension=""):

        directores = []
        files = []
        otherFiles = []


        currentDirectoryContents = os.listdir(target)

        for item in currentDirectoryContents:

            if (item[0]== "."):
                pass

            elif (os.path.isdir(target + '/' + item)):
                directores.append(target + '/' + item)

            # Add files to files list and filter by extension
            elif (len(extension) == 0):
                files.append(target + '/' + item)

            elif (item[-(len(extension)):]== extension):
                files.append(target + '/' + item)

            else:
                otherFiles.append(target + '/' + item)

        for dir in directores:
            sub_dir_contents = self.fileList(dir,extension)

            files.extend(sub_dir_contents.get("files"))

        # Filter out by extension

        return {"files":files,"directores":directores,"otherFiles":otherFiles}

if (__name__ == '__main__'):

    newOb = DirectoryWalker()

    results = newOb.fileList("/Users/cokelly/Desktop/Reference cards")

    print(results)
