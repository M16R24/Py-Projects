print("_____________________________")
print("Random Number Guessing Game")
print("---------------------------------------------")
print("guess the number between 0 and 9")
count = 0

def rndNo():
    import random
    return random.randint(0, 10)

temp = rndNo()

def guess(n, temp):
    if n != temp:
        return False
    else:
        return True


while count < 3:
    count = count + 1
    ZZ = int(input('Enter guess no: '))
    t = guess(ZZ, temp)
    if t is False:
         print("Guess Again, chances left: ", 3 - (count))
         continue
    else:
        print('Correct Guess:  ', temp)
        break
    
    

