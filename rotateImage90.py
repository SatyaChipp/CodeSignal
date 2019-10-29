"""
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
Example
For
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be
rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""

##1
def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

##2
list(zip(*reversed(a)))
##3
lambda a: zip(*a[::-1])

##4
def rotateImage(a):
    a = a[::-1]
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
