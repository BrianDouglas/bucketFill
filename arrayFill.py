
###Here be where we define functions! YARRRRR###

def create2dArray(numColumns, numRows):
    a = [[0]*numColumns for i in range(numRows)]
    return a

def print2dArray(a):
    #print("\n")
    for i in range(len(a)):
        #print(i)
        print(a[i])
    print("\n")

def diag2dArray(a):
    for i in range(len(a)):
        if i >= len(a[0]):
            break
        a[i][i] = 1
    #print(a[i])
    return a

def fillBucket(canvas, X, Y, oldVal, newVal):
    #print(str(X)+","+str(Y))
    if (X<0 or X >= len(canvas) or Y<0 or Y >= len(canvas[0]) or canvas[X][Y] == newVal or canvas[X][Y] != oldVal):
        return
    
    canvas[X][Y] = newVal
    fillBucket(canvas,X+1,Y,oldVal,newVal)
    fillBucket(canvas,X,Y+1,oldVal,newVal)
    fillBucket(canvas,X-1,Y,oldVal,newVal)
    fillBucket(canvas,X,Y-1,oldVal,newVal)

###End function defs###
