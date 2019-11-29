from itertools import groupby
import sys

def runLengthEncode (plainText):
    res = []

    for k,i in groupby(plainText):
        run = list(i)
        if(len(run) > 2):
            res.append("{}{}".format(len(run), k))
        else:
            res.extend(run)

    return "".join(res)


if len(sys.argv) < 2:
    input_code = 'wwwwaaadexxxxxx'
else:
    input_code = sys.argv[1]

print(runLengthEncode(input_code))