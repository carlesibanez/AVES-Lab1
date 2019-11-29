import matplotlib.image as mpimg
import sys

result = []


def up(i,j, max_i, max_j):
    result.append(matrix[i][j])
    if i == 0 and j != max_j:
        down(i, j+1, max_i, max_j)
    elif j == max_j and i != max_i:
        down(i+1, j, max_i, max_j)
    elif j != max_j:
        up(i-1, j+1, max_i, max_j)


def down(i, j, max_i, max_j):
    result.append(matrix[i][j])
    if j == 0 and i != max_i:
        up(i+1, j , max_i, max_j)
    elif i == max_i and j!= max_j:
        up(i, j+1, max_i, max_j)
    elif i != max_i:
        down(i+1, j-1, max_i, max_j)


if len(sys.argv) == 1:
    matrix = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]]
else:
    try:
        matrix = mpimg.imread(sys.argv[1])
    except FileNotFoundError:
        print('File does not exist. Try again')
        sys.exit(0)

max_i = len(matrix)-1
max_j = len(matrix[0])-1
sys.setrecursionlimit(1000000)
i, j = 0, 0
up(i,j, max_i, max_j)
print(result)