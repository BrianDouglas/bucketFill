from arrayFill import *

canvas = create2dArray(int(input("Specify number of Columns: ")), int(input("Specify number of Rows: ")))
print2dArray(canvas)

canvas = diag2dArray(canvas)

print2dArray(canvas)

fillBucket(canvas,int(input("Specify Y coord: ")),int(input("Specify X coord: ")),0,2)

print2dArray(canvas)