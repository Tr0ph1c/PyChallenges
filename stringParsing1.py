#Task from hackerRank
#
#TASK REQUIREMENTS:
#
#You are given a string S.
#
#Your task is to find the
#indices of the start and
#end of string K in S.
#
#----- My solution -----

def FindIndicies(string, substring):
    currentind = 0
    stringlen = len(string)
    substringlen = len(substring)
    
    while currentind < stringlen:
        ind = string.find(substring, currentind, stringlen)
        if currentind == 0 and ind == -1:
            print("(-1, -1)")      #Prints "(-1, -1)" if there are
            break                  #no instances of K in S.
        if ind == -1:
            break
        print("({0}, {1})".format(ind, ind+substringlen-1))
        currentind = ind + 1       #Keep looping and using string.find()
                                   #to find the index of the start, adding
                                   #the length of the substring to it -1 to
                                   #find the end index until it finds no more.
if __name__ == "__main__":
    string = input("String S: ")
    substring = input("Substring K: ")
    FindIndicies(string,substring)
