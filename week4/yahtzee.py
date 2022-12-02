import random
dice = []
class Die:
    SIDES = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    def __init__(self, sides, value = 1):
        self.sides = sides
        self.value = value
    def roll(self):
        self.value = random.randint(1, self.sides)
    def getCurrentFaceValue(self):
        return self.value
    def showDieFace(self):
        return Die.SIDES[self.value]
    def __eq__(self, __o):
        return self.value == __o.value

def rollFive(sides1, sides2, sides3, sides4, sides5):
    global dice
    dice = [Die(sides1), Die(sides2), Die(sides3), Die(sides4), Die(sides5)]
    for die in dice:
        die.roll()
        print(f"{die.showDieFace()} ({die.getCurrentFaceValue()})", end =" ")
       
rollFive(1, 1, 1, 3, 1)

def rollForYahtzee(dice) :
    if all(die == dice[0] for die in dice):
            print("\nYAHTZEE")

rollForYahtzee(dice)
