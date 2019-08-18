#!/usr/bin/env python3
sticks = 21
print("There are 21 nticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")
print("*"*50)
while True:
    print('Sticks left:',sticks)
    take = int(input('Take sticks (1-4):'))
    if take <= 0 or take >= 5:
        print('You take wrong sticks ,try again !')
        continue
    if sticks == 1:
        print('YOU lOOSE !')
        break
    sticks -= 5
    print("The computer took ",(5-take))
    print("*"*50)
