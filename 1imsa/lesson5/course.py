from pathlib import Path
import shutil, os, zipfile

# pathPythonfolder = Path("/Users/collinvandervorst/Desktop/python_files/text.txt");
# print("Bestaat het? " + str(pathPythonfolder.exists()))
# print("Is het een folder? " + str(pathPythonfolder.is_dir()))
# print("Is het een bestand? " + str(pathPythonfolder.is_file()))
# print("Welke extenstion? " + str(pathPythonfolder.suffix))
# print("Wat is de bestandnaam? " + str(pathPythonfolder.stem))
# print("Wat is de volledige naam? " + str(pathPythonfolder.name))

# currentFolder = Path(__file__)
# print(currentFolder)

# rootPath = Path("/Users/collinvandervorst/Desktop/python_files")
# print(".git" in os.listdir(rootPath))

# allTxtDocuments = rootPath.glob(r"*.txt") # collin checket ut

# print(allTxtDocuments)

# file = open('logs/log.txt', 'a')
# file.write("HALLLLLOOOOO\n")
# file.close()
# @todo LARS WILT WETEN OF JE EEN LIJN KAN VERWIJDEREN


# file = open("log.txt", "r") # a = append, w = overwrite, r = read
# fullText = file.read() # .ReadToEnd() in c#, reads everything
# print(fullText)

# fileLine = file.readline()

# while fileLine:
#     print(fileLine) #check why enter (?)
#     fileLine = file.readline()

# file.close()

# file = open("log.txt", "r")
# fullText = file.readlines()
# print(fullText)
# file.close()

# Test case 1 bestaande file
# O: Give me a filename
# I: /Users/collinvandervorst/School/2021/scripting/exercices/log.txt
# O: While line to you want remove?
# I: 3
# O: Lijn 3 is niet meer

# Test case 1 bestaande file
# O: Give me a filename
# I: /Users/collinvandervorst/School/2021/scripting/exercices/log2.txt
# O: file bestaat niet
# filePath = input("Give me a filename") #/Users/collinvandervorst/School/2021/scripting/exercices/log.txt

# if Path(filePath).exists() == True:
#     removeLine = int(input("While line to you want remove?")) # 3

#     # read file
#     file = open(filePath, "r")
#     allLines = file.readlines()
#     file.close()

#     # remove line from arrary
#     allLines.pop(removeLine - 1)

#     # send output to file
#     file = open(filePath, "w")
#     for line in allLines:
#         file.write(line)

#     file.close()

# else:
#     print("hij bestaat niet")


# if Path("logs").exists() == False:
#     os.mkdir("logs")

# file = open("logs/log.txt", "w")
# file.write("mijn eerste log")
# file.close()

# shutil.copy("logs/log.txt", "logs/copy_log.txt")
# shutil.move("logs/copy_log.txt",Path.cwd())

# zipFolder = zipfile.ZipFile("logs.zip", "w")
# zipFolder.write("logs/log.txt")
# zipFolder.close()

zipfile = zipfile.ZipFile("logs.zip", "r")
print(os.getcwd())
zipfile.extractall("/Users/collinvandervorst/School/2021/scripting/exercices/logs_zip")
zipfile.extractall()
zipfile.close()

