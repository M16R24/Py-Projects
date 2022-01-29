class GuessNumber:
    
    def __init__(self):
        n = input('Enter guess value: ')
        self.n = n
        
    def random(self): # func to generate random number
        import random
        rndN = int(random.randint(0, 10))
        return rndN
        
    def guess(self, random): # func to check the guess value
        z = 2
        while z > 0:
            if self.n != random:
                print('remaining guesses', z)
                GuessNumber()
            z = z - 1
        
        if z == 0:
            print('guess value', random)
