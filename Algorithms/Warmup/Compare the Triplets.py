# Compares the values of two arrays

def compareTriplets(a, b):
    pointa = 0
    pointb = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            pointa += 1
        elif a[i] < b[i]:
            pointb += 1
    print(pointa, pointb)

compareTriplets([1, 5, 6], [9, 4, 3])