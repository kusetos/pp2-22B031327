### 1
def sqr(N):
    for i in range(1, N+1):
        i = i ** 2
        yield i
N = 10
ka = sqr(N)
for i in range(1, N+1):
    print(next(ka), end=(' '))

print('\n')
### 2

def evenNum(n):
    for i in range(0, n+2):
        if i % 2 == 0:
            yield i

n = 50 # n = int(input())

even = evenNum(n)
for i in range(0, n//2+1):
    print(next(even), end=' ')

### 3
print('\n')

def div3and4(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
num = div3and4(n)
for i in range(0, n//12+1):
    print(next(num), end=" ")

### 4
print('\n')

def squares(a, b):
    p = 0
    for i in range(a, b+1):
        p = i ** 2
        yield p
a, b = 10, 15
s = squares(a, b)
for i in range(0, b-a+1):
    print(next(s), end=(' '))

### 5
print('\n')

toZero = (i for i in range(n, -1, -1))
for i in range(0, n):
    print(next(toZero), end=(' '))
