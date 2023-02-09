import math
### 1
class Upper:
    def __inti__(self):
        self.word = ""
    def getString(self):
        self.word = "алалалаллалалала"
    def printStr(self):
       print(self.word.upper())
word = Upper()
word.getString()
word.printStr()

### 2

class Shape:
    def area(self):
        print(0)
class Square(Shape):
        def __init__(self, length):
            super().__init__()
            self.length = length
        def area(self):
            print(self.length**2)

shape = Shape()
square = Square(25)    #int(input())
shape.area()
square.area()

### 3

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
a = Rectangle(15, 22)   #int(input()), int(input())
a.area()

### 4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, point):

        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        # return sqrxy
first = Point(3, 4)
second = Point(5, 6)
first.show()
second.show()
first.move(0, 8)          #(int(input()), int(input()))
print(first.dist(second))
first.show()

### 5

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, balance):
        self.balance += balance
    def withdraw(self, balance):
        if(balance >= self.balance):
            print("воняешь слабостью")
        elif (balance < self.balance):
            self.balance -= balance
            print(f"теперь {self.owner} беден на", balance, "tg")
    def show(self):
        print(self.owner, self.balance)
isa = Account("Isssatay", 500)
isa.deposit(50)
isa.show()
isa.withdraw(3000)
isa.show()
anu = Account("aNuar", 2000)
anu.deposit(500)
anu.show()
anu.withdraw(700)

### 6

class Prime:
    def filter(self, list):
        primes = []
        self.list = list
        for x in self.list:
            p = 0
            for i in range(1, x):
                if x % i == 0:
                    p += 1
            if p == 1:
                primes.append(x)
        return primes

nums = Prime()
print(nums.filter([1, 3, 5, 6, 7, 10, 113]))
