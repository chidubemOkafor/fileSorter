from pathlib import Path
import os
import shutil

def getDirectory(p):
    downloads_path = str(Path.home() / p)
    return downloads_path

def getFilesInDirectory():
    files = os.scandir(getDirectory("Downloads"))
    return files

def moveFile():
    images = [".jpg",".jpeg",".webp",".gif",".png",".svg",".webp",".avif"]
    videos = [".mp4"]
    microsoftInst = [".msi"]
    compresses = [".7z", ".rar",".zip"]
    application = [".exe"]
    isoFiles = [".iso"]
    documents = [".pdf"]

    files = getFilesInDirectory()
    for file in files:
        _,extention =  os.path.splitext(file)
        if extention in images:
            shutil.move(file, getDirectory("Downloads") + "/images")

        elif extention in videos:
            shutil.move(file, getDirectory("Downloads") + "/videos")

        elif extention in microsoftInst:
            shutil.move(file, getDirectory("Downloads") + "/microsoftinstaller")

        elif extention in compresses:
            shutil.move(file, getDirectory("Downloads") + "/compressed")

        elif extention in isoFiles:
            move = shutil.move(file, getDirectory("Downloads") + "/iso")

        elif extention in application:
            move = shutil.move(file, getDirectory("Downloads") + "/executable")

        elif extention in documents:
            move = shutil.move(file, getDirectory("Downloads") + "/documents")

moveFile()