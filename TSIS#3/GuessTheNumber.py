import random
def numGusser():
    x = random.randint(0, 20)
    print("Hello! Input nikname:")
    name = input()
    print(f'well, {name}, im thinking of number between 1-20 \nTake a guess:')

    while 1 > 0:
        num = int(input())
        if num > x:
            print(f"{num} is too HUGE")
        elif num < x:
            print(f"{num} is too LITTLE")
        elif num == x:
            print("SUUIIIIII")
            break
numGusser()
