import random
import itertools
import array

def oneDArray(x):
    return list(itertools.chain(*x))


children = []
for i in range(6):
    routine = []
    lst = []
    lst2 = []
    #print('Population',i)
    mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],
                [25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
    mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
    mylist3 = [[5], [22], [33]]  #

    sec_period_choice = [0, 1]
    random.shuffle(mylist1)
    random.shuffle(mylist2)
    random.shuffle(mylist3)

    for u in range(6):
        x = (random.choice(mylist1))
        # routine.append(x)
        index = mylist1.index(x)
        mylist1.pop(index)
        lst.append(x)

        e = random.choice(sec_period_choice)  # Second Period Choice
        if e == 0:
            x = (random.choice(mylist1))
            # routine.append(x)
            index = mylist1.index(x)
            mylist1.pop(index)
            lst.append(x)
        elif e==1:
            if (len(mylist3)!=0):
                x = random.choice(mylist3)
                #routine.append(x)
                index = mylist3.index(x)
                mylist3.pop(index)
                lst.append(x)
            else:
                x = (random.choice(mylist1))
                # routine.append(x)
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)

        lst.append([44])
        # routine.append([44])

        count = 0
        for q in lst:
            if len(q) == 2:
                count += 2
            else:
                count += 1

        #   print(count)

        if count == 5:
            if len(mylist2) != 0:
                x = (random.choice(mylist2))
                # routine.append(x)
                index = mylist2.index(x)
                mylist2.pop(index)
                lst.append(x)
            else:
                x = (random.choice(mylist1))
                # routine.append(x)
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
                if (len(mylist3)!=0):
                    x = (random.choice(mylist3))
                    #  routine.append(x)
                    index = mylist3.index(x)
                    mylist3.pop(index)
                    lst.append(x)
        elif count == 4:
            for i in range(2):
                x = (random.choice(mylist1))
                # routine.append(x)
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
        #print(lst)
        routine.append(lst)
        lst = []
    #print(routine)
matrix = []
matrix1 = []
matrix = oneDArray(routine)
#print(matrix)
matrix1 = oneDArray(matrix)
#print(matrix1)
#print(len(matrix1))

def show(arr):
    print(arr)
    for i in range(len(arr)):
        if arr[i] <= 5:
            arr[i] = 'BB DBMS'
        # elif arr[i]<=:
        #     arr[i]='DBMS BB,SP'
        elif arr[i]<=11:
            arr[i]='OS SP'
        
        elif arr[i]<=17:
            arr[i]='ES ML'
        
        elif arr[i]<=22:
            arr[i]='OOAD DMG'
        
        elif arr[i]<=28:
            arr[i]='AI SLS'
        
        elif arr[i]<=32:
            arr[i]='EC JJ'

        elif arr[i]<=33:
            arr[i]='EC T YB'

        elif arr[i]<=36:
            arr[i]='DBMS LAB SP,BB/OOAD DMG'
        elif arr[i]<=39:
            arr[i]='AI SLS/OS SP'
        elif arr[i]<=42:
            arr[i]='ES ML/DBMS BB,SP'
        elif arr[i]==44:
            arr[i]='Break'
        
    print(arr)
show(matrix1)

arr = [[0 for i in range(8)] for j in range(6)]
count = 0
for i in range(6):
    for j in range(8):
        arr[i][j] = matrix1[count]
        count += 1


#lst3 = []
#print(lst)
lst3 = arr
#print(lst3[0])
for i in range(len(lst3)):
    
    #print(lst3[i])
    pass


# mat = []
# for i in range(routine):
#     for j in range(routine[i]):
#         print(j)

#hard constraint

# noconflict=10
# conflict=-10
# def calcFitness():
#     # for i in range(len(lst)):
#     #     for j in range(lst[i]):
#     for i in range(6):
#         chk=print(lst3[i])
#         for j in range(8):
#             lst.append(chk[j])
            
# calcFitness()
    