import matplotlib.image as mpimg
import sys

result = []


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


# Get the dimensions of the matrix/image
max_i = len(matrix)-1
max_j = len(matrix[0])-1
# Initialize indices
i, j = 0, 0
#Flags for the flow of the serpentine
has_ended = False
up_down = True

while not has_ended:
    result.append(matrix[i][j])
    if up_down:
        if i == 0 and j != max_j:
            up_down = False
            j = j + 1
        elif j == max_j and i != max_i:
            up_down = False
            i = i + 1
        elif j != max_j:
            up_down = True
            i = i - 1
            j = j + 1
        else:
            has_ended = True
    else:
        if j == 0 and i != max_i:
            up_down = True
            i = i + 1
        elif i == max_i and j != max_j:
            up_down = True
            j = j + 1
        elif i != max_i:
            up_down = False
            i = i + 1
            j = j - 1
        else:
            has_ended = True

print(result)