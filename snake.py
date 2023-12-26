# Trying to implement the Snake game on python
#
#
#
#
#
#

import time

WIDTH = 16
HEIGHT = 16

posX = 0
posY = 0

foodPos = 10

score = 0

def Initialize():
    global posX
    global posY
    global foodPos
    global score
    
    posX = round(WIDTH/2)
    posY = round(HEIGHT/2)
    foodPos = round(WIDTH*HEIGHT/2)
    score = 0

def Render():
    print('\n'*5)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == posX and y == posY:
                print('Q ', end='')
            elif y*WIDTH+x == foodPos:
                print('F ', end='')
            else:
                print('# ', end='')
        print()

def Process():
    print('processing')

def main():
    Initialize()
    
    while (True):
        Render()
        #Get Input
        #Process game state
        time.sleep(0.5)

if __name__ == "__main__":
    main()
