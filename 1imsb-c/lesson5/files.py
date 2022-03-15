from pathlib import Path
import os, shutil, zipfile

# pythonFolderPath = Path(r"/Users/collinvandervorst/Desktop/python_files/python.txt")

# print("Bestaat de folder/file?", pythonFolderPath.exists())
# print("Is het een folder?", pythonFolderPath.is_dir())
# print("Is het een file?", pythonFolderPath.is_file())
# print("Is het parent folder?", pythonFolderPath.parent)
# print("Welke extension?", pythonFolderPath.suffix)
# print("Welke bestandsnaam?", pythonFolderPath.stem)
# print("Full file naam", pythonFolderPath.name)


# path = r"c://yassine-is-ne-coole/desktop/test.text"
# print(path)

# file = Path(__file__)
# print(file.name)

# writing
# file = open("log.txt", "a") # w = write, a = append, r = read
# file.write("Collin was hier om 11:43\n")
# file.close()

# reading
# file = open("log.txt", "r")
# fullText = file.read() # volledige text terug .ReadToEnd()
# firstFiveChars = file.read()
# print(firstFiveChars)

# otherText = file.read()
# print(otherText)

# lines = file.readlines()
# print(lines[0])

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

# # Ask for path
# pathString = input("Give me a filename")
# pathObject = Path(pathString)

# # Ask if file exists
# if pathObject.exists() and pathObject.is_file :
#     # Ask which line you have remove
#     lineNumber = int(input("While line to you want remove?")) # fe: 3

#     # read the file 
#     file = open(pathString, "r")
#     allLines = file.readlines()
#     file.close()

#     # remove line 
#     allLines.pop(lineNumber - 1) # del allLines[lineNumber - 1]

#     # output to file
#     file = open(pathString, "w")
#     for line in allLines:
#         file.write(line)
#     file.close()
# else:
#     print("hij bestaat niet")

if Path("logs").exists() == False:
    os.mkdir("logs")

# shutil.copy(Path("log.txt"), Path("logs/copy_log.txt"))
# shutil.move("log.txt", "logs/moved_log.txt")
# shutil.rmtree("logs")

# newzip = zipfile.ZipFile("logs.zip", "w")
# newzip.write("logs/log.txt")
# newzip.close()

newzip = zipfile.ZipFile("logs.zip")
newzip.extractall()
newzip.close()