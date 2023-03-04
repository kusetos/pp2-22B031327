import os
### 1

path = 'D:\!testPath'
print("List of all directories and files:\n", os.listdir(path))

#os.getcwd()
#os.mkdir("TestDir")

### 2

path2 = afgan = "D:\!testPath\folderAfgan"
print(os.access(path2, os.F_OK), end="\t") #existence/существование
print(os.access(path2, os.R_OK), end="\t") #readability
print(os.access(path2, os.W_OK), end="\t") #writability
print(os.access(path2, os.X_OK), end="\n") #executed/выполнимость

### 3

fortnite = "D:\!testPath\Fortnite.txt"
def chekPath(pathName):
    if os.path.isfile(pathName) == True:
        print("existIn", os.path.dirname(pathName), end="\t")
    else:
        print("NotExist", end="\t")
chekPath(fortnite)
chekPath(path)
chekPath(afgan)
print(' ')

### 4
with open(fortnite, 'r') as fort:
    print(len(fort.readlines()), "lines in text")

### 5
BSfile = "D:\!testPath\BrawlStars.txt"
brawlers = ["Leon", 'Crow', 'Piper', 'Mortis', 'Spike']
with open(BSfile, 'w') as bs:
    bs.write("\n".join(brawlers))

### 6

for i in range(0, 26):
    x = open(chr(i+97)+".txt", 'a')

### 7

with open(BSfile) as bs:
    with open("z.txt", "w") as aFile:
        for ln in bs:
            aFile.write(ln)

### 8
# deleted 10 files
for i in range(97, 122):
    file = chr(i)+".txt"
    if(os.path.exists("D:\Codes\python\pycharm\LABS\Lab6")):
        os.remove(file)
    else:
        print("File doesnt exists!")
