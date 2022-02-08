import random
import itertools

# to change nested list into a one dimensional list
def oneDArray(x):
    return list(itertools.chain(*x))


children = []
overal_routine = [0 for i in range(6)]


for i in range(6):     #this loop is for the generation of population
    routine = []
    lst = []
    lst2 = []
    #print('Population',i)
    mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],
                [25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
    mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
    mylist3 = [[5], [22], [33]]  # Single Period Class

    sec_period_choice = [0, 1]
    random.shuffle(mylist1)
    random.shuffle(mylist2)
    random.shuffle(mylist3)

    for u in range(6):   # this loop is for generation of chromosome
        x = (random.choice(mylist1))
        index = mylist1.index(x)
        mylist1.pop(index)
        lst.append(x)

        e = random.choice(sec_period_choice)  # Second Period Choice
        if e == 0:
            x = (random.choice(mylist1))
            index = mylist1.index(x)
            mylist1.pop(index)
            lst.append(x)
        elif e==1:
            if (len(mylist3)!=0):
                x = random.choice(mylist3)
                index = mylist3.index(x)
                mylist3.pop(index)
                lst.append(x)
            else:
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)

        lst.append([44])  # appending break i.e. 44 --> break


        count = 0
        for q in lst:
            if len(q) == 2:
                count += 2
            else:
                count += 1

        if count == 5:
            if len(mylist2) != 0:
                x = (random.choice(mylist2))
                index = mylist2.index(x)
                mylist2.pop(index)
                lst.append(x)
            
            else:
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
                if (len(mylist3)!=0):
                    x = (random.choice(mylist3))
                    index = mylist3.index(x)
                    mylist3.pop(index)
                    lst.append(x)
        
        elif count == 4:
            for i in range(2):
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
        #print(lst)
        routine.append(lst)     
        lst = []
    #print(routine)     # generates whole population




    matrix = []
    matrix1 = []
    matrix = oneDArray(routine)   # generates onedimensional of routine
    #print(matrix)
    matrix1 = oneDArray(matrix)   # generates onedimensional of population
    #print(matrix1)
    #print(len(matrix1))

    arr = [[0 for i in range(8)] for j in range(6)]
    count = 0
    for i in range(6):
        for j in range(8):
            arr[i][j] = matrix1[count]
            count += 1


    #print(lst)
    lst3 = arr

    codeLst = [5, 11, 17, 22, 28, 32, 33] 
    lecCodeLst = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB']

    chk = []

    def calcFitness(chk):
        lecCount = [0 for i in range(7)]
        a = 0
        b = 0
        j = 0
        while(j <= 6):
            if(a>7):
                break
            elif(chk[a] <= codeLst[j]):
                lecCount[j] += 1
                #print(lecCount)
                j=0
                a=a+1
            elif chk[a] >= 34:
                b += 1
                a += 1
                j=0
                pass
            
            else: 
                j += 1
                pass

        #print(lecCount)

        score=0
        for j in range(7):
            if(lecCount[j]<=2):
                #print(lecCount[j])
                score+= (lecCount[j])*10  # no-conflict = 10
                #print(score)
            else:
                conflict = 0
                #print(lecCount[j])
                conflict=(lecCount[j]-2)
                score+=(conflict*(-10))+(2*10)   # conflict = -10
                #print(score)

        #print(b)

        score+=(b*10)
        #print(score)
        
        return score

    overal_score = 0 
    
    for i in range(6): 
        chk=lst3[i]
        #print(chk)
        score = calcFitness(chk) 
        #print(score)
        overal_score += score  

    #print(overal_score)
    overal_routine[i] = matrix1
    print(overal_routine[i])
    print(overal_score)



        





    