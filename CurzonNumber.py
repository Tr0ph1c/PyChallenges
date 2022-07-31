#Task from Edabit
#
#TASK REQUIREMENTS:
#
#Find if a number is a Curzon Number or not.
#
#A Curzon number is defined as such:
#Consider the number N..
#If 1 + 2 to the power of N is divisible by 1 + 2 multiplied by N
#then N is a curzon number
#
# e.g.: 1, 2, 5, 6, 9, 14, 18, 21, 26, 29...
#
#----- My solution -----

def IsCurzon(num):                                  
    if (1 + 2 ** num) % (1 + 2 * num) == 0:  #pretty easy solution
	    return True                             
    return False

def GetInput():                              #function to get input
    try:                                     #and make sure its a num
        inp = int(input())
    except ValueError:
        print("please enter a number")
        inp = GetInput()
    return inp

if __name__ == "__main__":
    Inp = GetInput()
    print(IsCurzon(Inp))
