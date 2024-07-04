import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("Rolling dice...")
print("Die 1: "+str(dice1))
print("Die 2: "+str(dice2))
Total = dice1+dice2
print("Total value: "+str(Total))
if Total>=7:
    print("You won")
else:
    print("You lost")
