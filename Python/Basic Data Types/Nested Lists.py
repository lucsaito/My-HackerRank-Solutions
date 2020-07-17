"""
## The main idea I came up with was to recreate the records list without the students
with the minimum grade. Now just create a list comprehension with the students with
the minimum grades(that now are the 2th minimum grade) and then just sort the values.

EX:
records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
records = [i for i in records if i[1] != min([sub[-1] for sub in records])]
records = [i for i in records if i[1] == min([sub[-1] for sub in records])]
records.sort()
for i in records:
    print(i[0])
"""
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    records = [i for i in records if i[1] != min([sub[-1] for sub in records])]
    records = [i for i in records if i[1] == min([sub[-1] for sub in records])]
    records.sort()
    for i in records:
        print(i[0])
