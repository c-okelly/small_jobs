# Author Conor O'Kelly

import os

class DirectoryWalker:

    def fileList(self,target):

        all_files = []
        directores = []
        files = []


        currentDirectoryContents = os.listdir(target)

        for item in currentDirectoryContents:

            if (item[0]== "."):
                pass

            elif (os.path.isdir(target + '/' + item)):
                directores.append(target + '/' + item)

            else:
                files.append(target + '/' + item)

        for dir in directores:
            sub_dir_contents = self.fileList(dir)

            files.extend(sub_dir_contents[0])

        return [files,directores]

if (__name__ == '__main__'):

    newOb = DirectoryWalker()

    results = newOb.fileList("/Users/cokelly/Desktop/Reference cards")

    print(results[0])
