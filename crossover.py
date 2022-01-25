import numpy as np
import itertools
import random

def oneDArray(x):
    return list(itertools.chain(*x))


# for crossover                                              import itertools


lst1off=[]
lst2off=[]
lst1=[[20, 21, 29, 30, 100, 37, 38, 39], [40, 41, 42, 100, 23, 24, 16, 17], [10, 11, 1, 2, 100, 34, 35, 36], [25, 26, 18, 19, 100, 31, 32, 5], [6, 7, 3, 4, 100, 27, 28, 22], [14, 15, 12, 13, 100, 8, 9, 33]]
lst2=[[37, 38, 39, 100, 16, 17, 25, 26], [27, 28, 12, 13, 100, 34, 35, 36], [40, 41, 42, 100, 14, 15, 20, 21], [10, 11, 1, 2, 100, 8, 9, 33], [29, 30, 6, 7, 100, 3, 4, 5], [18, 19, 23, 24, 100, 31, 32, 22]]
x=random.randint(0,5)
#print(x)

lst1off.append(lst2[x])
lst2.pop(x)

lst2off.append(lst1[x])
lst1.pop(x)

for i in range(5):
    lst1off.append(lst1[0])
    lst1.pop(0)

for i in range(5):
    lst2off.append(lst2[0])
    lst2.pop(0)

print(lst1off)
print(lst2off)


# Finding out errors indicated by '*'


lst1off = []
lst2off = []
routine = [[18, 19, 23, 24, 100, 31, 32, 22], [20, 21, 29, 30, 100, 37, 38, 39], [40, 41, 42, 100, 23, 24, 16, 17],
           [10, 11, 1, 2, 100, 34, 35, 36], [25, 26, 18, 19, 100, 31, 32, 5], [18, 19, 23, 24, 100, 27, 28, 22]]
routinecheck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 100, 100, 100, 100, 100, 100]

for i in range(6):
    for j in range(8):
        if routine[i][j] in routinecheck:
            index = routinecheck.index(routine[i][j])
            routinecheck.pop(index)
        else:
            routine[i][j] = '*'
print(routine)
print(routinecheck)
not_present = routinecheck[:]
arr = [[0 for q in range(10)] for p in range(6)]
for i in range(6):
    for j in range(8):
        arr[i][j] = routine[i][j]
present = arr[:]


# Enter how long lab is

lab_len = int(input("Enter the no of periods in lab:"))


# lists converted to 1D


if lab_len == 3:
    mylist1 = np.array(
        [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24], [25, 26],
         [27, 28], [29, 30], [31, 32]])  # Double Class
    mylist1 = mylist1.flatten()
    # print(mylist1)
    mylist2 = np.array([[34, 35, 36], [37, 38, 39], [40, 41, 42]])  # Lab
    mylist2 = mylist2.flatten()
    # print(mylist2)

    mylist3 = np.array([[5], [22], [33]])
    mylist3 = mylist3.flatten()
    # print(mylist3)

if lab_len == 2:
    mylist1 = np.array(
        [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [12, 13], [14, 15], [17, 18], [19, 20], [22, 23], [26, 27], [28, 29],
         [30, 31], [32, 33]])  # Double class
    mylist1 = mylist1.flatten()
    # print(mylist1)
    mylist2 = np.array([[35, 36], [37, 38], [39, 40], [41, 42]])  # labs
    mylist2 = mylist2.flatten()
    # print(mylist2)
    mylist3 = np.array([[11], [16], [21], [24], [25], [34]])  # single class
    mylist3 = mylist3.flatten()
    # print(mylist3)


# Finding the missing class type

mis_prac = []
mis_lec = []
mis_tut = []
for i in range(len(not_present)):
    if not_present[i] in mylist1:
        mis_lec.append(not_present[i])
    if not_present[i] in mylist2:
        mis_prac.append(not_present[i])
    if not_present[i] in mylist3:
        mis_tut.append(not_present[i])


# Renaming * to req class types

if lab_len == 3:
    for i in range(6):
        for j in range(8):

            if len(mis_prac) != 0 and present[i][j] == '*' and present[i][j + 1] == '*' and present[i][j + 2] == '*':
                present[i][j] = 'prac'
                present[i][j + 1] = 'prac'
                present[i][j + 2] = 'prac'
            elif len(mis_lec) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                present[i][j] = 'Lec'
                present[i][j + 1] = 'Lec'
            elif len(mis_tut) != 0 and present[i][j] == '*':
                present[i][j] = 'Tut'

if lab_len == 2:
    for i in range(6):
        for j in range(8):

            if len(mis_prac) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                present[i][j] = 'prac'
                present[i][j + 1] = 'prac'
            elif len(mis_lec) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                present[i][j] = 'Lec'
                present[i][j + 1] = 'Lec'
            elif len(mis_tut) != 0 and present[i][j] == '*':
                present[i][j] = 'Tut'


# Replacing missing class


if lab_len == 3:
    for i in range(6):
        for j in range(8):

            if present[i][j] == 'L' and present[i][j + 1] == 'L' and present[i][j + 2] == 'L':
                present[i][j] = mis_prac[0]
                mis_prac.pop(0)
                present[i][j + 1] = mis_prac[0]
                mis_prac.pop(0)
                present[i][j + 2] = mis_prac[0]
                mis_prac.pop(0)
            elif present[i][j] == 'Lec' and present[i][j + 1] == 'Lec':
                present[i][j] = mis_lec[0]
                mis_lec.pop(0)
                present[i][j + 1] = mis_lec[0]
                mis_lec.pop(0)
            elif present[i][j] == 'Tut':
                present[i][j] = mis_tut[0]
                mis_tut.pop(0)

if lab_len == 2:
    for i in range(6):
        for j in range(8):

            if present[i][j] == 'L' and present[i][j + 1] == 'L':
                present[i][j] = mis_prac[0]
                mis_prac.pop(0)
                present[i][j + 1] = mis_prac[0]
                mis_prac.pop(0)
            elif present[i][j] == 'Lec' and present[i][j + 1] == 'Lec':
                present[i][j] = mis_lec[0]
                mis_lec.pop(0)
                present[i][j + 1] = mis_lec[0]
                mis_lec.pop(0)
            elif present[i][j] == 'Tut':
                present[i][j] = mis_tut[0]
                mis_tut.pop(0)

# Printing Output

for i in range(6):
    print(present[i][:8])
