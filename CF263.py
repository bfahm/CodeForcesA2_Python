import time
print("Beautiful Matrix <3 v.Final", "\nEnter A Matrix from the left to the right, down to the next line.", "\nonly one '1' is allowed, else an error will occur")
def rowfinder (array):
    for q in range (0,len(ListList)):
        for w in range (0,len(ListList[q])):
            if ListList[q][w]=='1':
                return q+1
    return "no 1s"
def columnfinder (array):
    for q in range (0,len(ListList)):
        for w in range (0,len(ListList[q])):
            if ListList[q][w]=='1':
                return w+1
    return "no 1s"
def mover(array):
    moves = 0
    row = rowfinder(ListList)
    while row < 3:
        ListList[row - 1], ListList[row] = ListList[row], ListList[row - 1]
        nicemoves(ListList)
        print("")
        time.sleep(2)
        row = rowfinder(ListList)
        moves += 1
    while row > 3:
        ListList[row - 1], ListList[row - 2] = ListList[row - 2], ListList[row - 1]
        nicemoves(ListList)
        print("")
        time.sleep(2)
        row = rowfinder(ListList)
        moves += 1

    column = columnfinder(ListList)
    while column < 3:
        ListList[2][column - 1], ListList[2][column] = ListList[2][column], ListList[2][column - 1]
        nicemoves(ListList)
        print("")
        time.sleep(2)
        column = columnfinder(ListList)
        moves += 1
    while column > 3:
        ListList[2][column - 1], ListList[2][column - 2] = ListList[2][column - 2], ListList[2][column - 1]
        nicemoves(ListList)
        print ("")
        time.sleep(2)
        column = columnfinder(ListList)
        moves += 1
    #print (ListList)
    print("number of moves= " ,moves)
def nicemoves(array):
    for y in range(0, 5):
        print(' '.join(ListList[y]))


#ListList=[['1','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0']]
ListList=[[input() for j in range(5)] for i in range(5)]
print ("your list is")
nicemoves(ListList)
print ("lets get is balanced")
mover(ListList)
