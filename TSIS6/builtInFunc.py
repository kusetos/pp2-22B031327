
### 1
def multiply(nums):
    mul = 1;
    for i in nums:
        mul *= i
    return mul
print(multiply([1, 2, 3, 4, 5, 6]))
### 2
def UpperLower(String):
    upper = 0
    lower = 0
    for i in String:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    print(f"upper = {upper}, lower = {lower}")
UpperLower("ASKDlkajsd")
### 3
def polindrome(String):

    if String[::-1] == String:
        print(True)
    else:
        print(False)
polindrome("asddsa")
### 4
import time
import math
def rootTimer():
    num = 25100
    milisek = 500
    time.sleep(500/1000)
    print(math.sqrt(num))
rootTimer()
### 5
def trueTuple(tuple):
    print(all(tuple))
trueTuple((1, 1, 0))
