# 1
def ounces(num):
    return 28.3495231 * num
print(ounces(15))
# 2
def Fahrenheit(F):
    return (5 / 9) * (F - 32)
print (Fahrenheit(120))
# 3
def solve(numheads, numlegs):
    chiken = numheads * 2
    rabbit = (numlegs - chiken) / 2
    chiken = numheads - rabbit
    print(f"{rabbit} rabbits, and {chiken} chikens" )
solve(35, 94)
# 4
def filter_prime(num):
    num = list(map(int, num.split()))
    primes = []
    for x in num:
        c = 0
        for i in range(1, x):
            if x % i == 0:
                c += 1
        if c == 1:
            primes.append(x)
    return primes
print(filter_prime("1 3 5 8 7 6 5 4 32 2 1"))
# 5
from itertools import permutations #inported tool
def permuta(string):
    word = [''.join(p) for p in permutations(string)]
    print(word)
permuta("пенсл")
# 6
def reversSentence(string):
    words = list(map(str, string.split()))
    words.reverse()
    print(*words, sep=' ')
reversSentence(")))) sovoskin like I")
reversSentence("казнить , нельзя помиловать")
# 7
def has_33(num):
    for i in num:
        if num[i] == 3 and num[i+1] == 3:
            return True
        else:
            return False

print(has_33([1, 3, 3, 4, 6, 9]))
print(has_33([1, 2, 3, 4, 5, 6, 3]))
# 8
def spy_game(num):
    if num.count(0) > 1 and num.count(7) > 0:
        if num.index(0) < num.index(0, num.index(0)+1, len(num)) and num.index(7, -1) > num.index(0, num.index(0)+1, len(num)):
            return True
        else:
            return False
    else:
        return False

print(spy_game([0, 0, 7]))
# 9
def volume_sphere(r):
    return (4/3)*3.14*r**3
print(volume_sphere(5))
# 10
def uniqList(num):
    newList = num.copy()
    return newList
print(uniqList([1, 2, 3, 4,50]))
# 11
def palindrom(word):
    word = str(word)
    tmp = word[::-1]
    if tmp == word:
        #print('palindrom')
        return True
    else:
        #print('not palindrom')
        return False

print(palindrom("kayak"))
print(palindrom("bambaleyla"))
# 12
def histogram(num):
    for x in num:
        print(x * '*')
histogram([1, 0, 5])
