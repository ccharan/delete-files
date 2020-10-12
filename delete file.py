"""
Created on Mon Oct 12 13:56:30 2020

@author: Charan C
"""

import os


fileExtns = ["en.srt", ".mp4", ".html"]


def filePermission(filePaths):
    for filePath in filePaths:
        os.chmod(filePath, 0o777)


def addPath(folderPath, folderOrFileNames):
    for folderOrFileName in folderOrFileNames:
        yield os.path.join(folderPath, folderOrFileName)


def checkPath(path):
    fileExtnFound = False

    if os.path.isdir(path):
        folderContents = os.listdir(path)

        for subFolderPath in addPath(path, folderContents):
            checkPath(subFolderPath)

    elif os.path.isfile(path):
        for fileExtn in fileExtns:
            if fileExtn in path:
                fileExtnFound = True
                continue

        if fileExtnFound is False:
            os.remove(path)
            print('removing - ', path)


def _filePaths(filePaths):
    for filePath in filePaths:
        yield filePath


if __name__ == "__main__":

    try:
        folderPath = input('Enter the folder path: ')
        path = os.path.join(folderPath)
        os.chmod(path, 0o777)
    except IOError as ioe:
        print('I/o error occured: ', os.strerror(ioe.errno))
    finally:
        folderContents = os.listdir(path)
        filePaths = [folderContent for folderContent in addPath(path,
                                                                folderContents)]
        filePermission(filePaths)

        for filePath in _filePaths(filePaths):
            checkPath(filePath)
