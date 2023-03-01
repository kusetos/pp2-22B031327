import re
# /d = nums
# /D = not nums
# [a-zA-z0-9]+@"[a-zA-Z]+\.(com|edu|kz)
#  начало      после@  после точки
# ^word - start of str
# word$ - end of str
# \s - contain space
# \w - any letter a-z, A-Z, 0-9, _
# \w{3} - 3 последовательных числа
#

#
### 1
pat1 = re.compile(r"ab*")
print(pat1.search("ASDAKDKkakldaldadababab"))
### 2
pat2 = re.compile(r"ab{2,3}")
print(pat2.search("ASaDAKDKkabbbakldaldbabab"))

### 3
pat3 = re.compile(r"[a-z]+\_")
print(pat3.findall("asdkaj___aklsd_.ad"))

### 4
pat4 = re.compile(r"[A-Z]{1}[a-z]+")
print(pat4.findall("ASK LDka d sLAS DJka skakd ladASDLdald"))
### 5
pat5 = re.compile(r"a.+b\Z")
print(pat5.findall("akalsdmajfndsjknfsb"))
### 6
pat6 = re.compile(r"[ .,]")
print(pat6.sub(';', "ad. . ak...oda;k dk jna ."))
### 7
def fromSnake(txt):
    camel = ''
    s = re.split("_", txt)
    s[1] = s[1].capitalize()
    camel += s[0]
    camel += s[1]
    print(camel)
fromSnake("its_camel")
### 8
text = "DldkadAasdadaaASHAHAHASS"
pat8 = re.findall("[A-Z][^A-Z]*", text)
print(pat8)

### 9
def spaceIn(txt):
    l = re.findall("[A-Z][^A-Z]*", txt)
    #print(l)
    sen = ""
    for i in l:
        sen += " " + i
    print(sen)
spaceIn("aAdaljdnAjandAnnddnAAA")
### 10
def fromCamel(txt):
    txt = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
    snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', txt).lower()
    print(snake)
fromCamel("itsSnake")

"""pattern =  "[a-zA-z0-9]+@[a-zA-Z]+\.(com|edu|kz)"
user = input()
if(re.search(pattern, user)):
    print("good")
else:
    print("no")
"""
