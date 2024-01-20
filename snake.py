# Trying to implement the Snake game on python
#
#
#
#
#
#

import time
import msvcrt

WIDTH = 16
HEIGHT = 16

posX = 0
posY = 0
dire = 0 # 0, 1, 2, 3 -> up, right, down, left

foodPos = 0

score = 0

def Initialize():
    global posX
    global posY
    global dire
    global foodPos
    global score
    
    posX = round(WIDTH/2)
    posY = round(HEIGHT/2)
    dire = 3
    foodPos = round(WIDTH*HEIGHT/2)
    score = 0

def Render():
    print('\n'*5)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == posX and y == posY:
                print('S ', end='')
            elif y*WIDTH+x == foodPos:
                print('F ', end='')
            else:
                print('# ', end='')
        print()

def WaitInput():
    global dire
    timeout = 0
    
    while timeout < 100:
        timeout += 0.01
        if msvcrt.kbhit():
            #inputs inverted coz rendering inverted
            key = msvcrt.getch()
            if key == b'w':
                dire = 2
            elif key == b'd':
                dire = 1
            elif key == b's':
                dire = 0
            elif key == b'a':
                dire = 3

def Process():
    print('processing')

def Next():
    global posX
    global posY

    if dire == 0:
        posY += 1
    elif dire == 1:
        posX += 1
    elif dire == 2:
        posY -= 1
    elif dire == 3:
        posX -= 1

def main():
    Initialize()
    
    while (True):
        Render()
        WaitInput()
        Next()
        #Process game state

if __name__ == "__main__":
    main()
