#The infamous game: TIC-TAC-TOE
#
#Thought it was a fun project
#so I gave it a go
#
#A 2D array makes it easy to check
#for vertical/ horizontal/ diagonal
#similarity.
#
#Has exception handling for most if
#not all errors that could come up.
#
#------------------------------------

from math import floor

arr = [ #0#1#2
        [0,0,0] #0
       ,[0,0,0] #1
       ,[0,0,0] #2
      ]

dic = '-XO'

player = 1

def vertCheck(): #Check vertical similarity
    for i in range(3):
        if [arr[0][i], arr[1][i], arr[2][i]] in [[1,1,1],[2,2,2]]:
            return 1;
    
    return 0;

def horiCheck(): #Check horizontal similarity
    for x in arr:
        if [x[0],x[1],x[2]] in [[1,1,1],[2,2,2]]:
            return 1;
    
    return 0;

def diagCheck(): #Check diagonal similarity
    if [arr[0][0],arr[1][1],arr[2][2]] in [[1,1,1],[2,2,2]]:
        return 1;
    elif [arr[0][2],arr[1][1],arr[2][0]] in [[1,1,1],[2,2,2]]:
        return 1;
    
    return 0;

def drawCheck(): #Check for draw
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0: return 0;

    return 1;

def Turn():      #Player input
    inp = input(
f'''
Player {player}'s turn... [{dic[player]}]\n

Enter the number of the slot
you want to place your token in:
'''
)
    while True:
        try:
            inp=int(inp.strip())
        except ValueError:
            print('Input has to be a number.')
            inp = input('Enter a new number: ')
            continue

        if inp < 0 or inp > 8:
            print('Number has to be from (0-8).')
            inp = input('Enter a new number: ')
            continue
        
        if arr[floor(inp/3)][inp%3] == 0:
            arr[floor(inp/3)][inp%3] = player
            break;
        else:
            print('This slot is already occupied.')
            inp = input('Enter a new number: ')
    
    return 0;

def Render():    #Render the game
    rendArr = [
        dic[arr[0][0]],dic[arr[0][1]],dic[arr[0][2]],
        dic[arr[1][0]],dic[arr[1][1]],dic[arr[1][2]],
        dic[arr[2][0]],dic[arr[2][1]],dic[arr[2][2]]
        ]

    for x in range(len(rendArr)):
        if rendArr[x] == '-':
            rendArr[x] = x
    
    print(
f'''
[{rendArr[0]}] [{rendArr[1]}] [{rendArr[2]}]

[{rendArr[3]}] [{rendArr[4]}] [{rendArr[5]}]

[{rendArr[6]}] [{rendArr[7]}] [{rendArr[8]}]

''')
    
    return 0;

def Reset():
    global arr
    global player
    print('\n'*20)
    arr = [[0,0,0],[0,0,0],[0,0,0]]
    player = 1

while True:     #match loop
    try:
        Reset()
        draw = 0
        while True: #main game loop
            Render()
            Turn()
            if vertCheck(): break
            if horiCheck(): break
            if diagCheck(): break
            if drawCheck(): draw=1;break
            player = 2 if player == 1 else 1

        Render()
        print('The game is a draw' if draw else f'Player {player} wins!')

        input('press enter to restart the game...')
    except KeyboardInterrupt:
        break
