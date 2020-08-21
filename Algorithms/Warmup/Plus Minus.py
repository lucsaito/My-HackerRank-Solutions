# Returns the ratio of positive, negative and zeros in an array

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    print(pos/n)
    print(neg/n)
    print(zer/n)