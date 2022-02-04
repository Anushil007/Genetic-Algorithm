import numpy as np
import itertools
import random
from fitness import calcFitness
import sys
from copy import deepcopy




def oneDArray(x):
    return list(itertools.chain(*x))


# for crossover                                              

def partial_crossover(lst1, lst2, lab_len):
    lst1_1 = deepcopy(lst1)
    lst2_2=deepcopy(lst2)
    x=0
    # print(lst1,"dhssssssssssssssss")
    # print(lst2,"sdhhhhhhhhhhhhhhhhhhhhhhh")
    i = j = 0
    lst1off=[]
    lst2off=[]
    offspring = []
    routine_two_offspring = []   # two store two offspring after calculating fitness
    score_offspring_lst = []    #two store two offspring fitness value

    # lst1=[[20, 21, 29, 30, 100, 37, 38, 39], [40, 41, 42, 100, 23, 24, 16, 17], [10, 11, 1, 2, 100, 34, 35, 36], [25, 26, 18, 19, 100, 31, 32, 5], [6, 7, 3, 4, 100, 27, 28, 22], [14, 15, 12, 13, 100, 8, 9, 33]]
    # lst2=[[37, 38, 39, 100, 16, 17, 25, 26], [27, 28, 12, 13, 100, 34, 35, 36], [40, 41, 42, 100, 14, 15, 20, 21], [10, 11, 1, 2, 100, 8, 9, 33], [29, 30, 6, 7, 100, 3, 4, 5], [18, 19, 23, 24, 100, 31, 32, 22]]
    x=random.randint(0,5)
    #print(x)

    lst1off.append(lst2_2[x])
    lst2_2.pop(x)

    lst2off.append(lst1_1[x])
    lst1_1.pop(x)


    for i in range(5):
        lst1off.append(lst1_1[0])
        lst1_1.pop(0)

    for i in range(5):
        lst2off.append(lst2_2[0])
        lst2_2.pop(0)
    offspring.append(lst1off)
    offspring.append(lst2off)

    #print(lst1off)
    #print(lst2off)
    #print(offspring)


    # Finding out errors indicated by '*'
    for i in range(2):
        routine = []
        routine = offspring[i]
        #routine=[[22, 23, 17, 18, 100, 28, 29, 34], [28, 29, 28, 29, 100, 35, 36, 34], [9, 10, 30, 31, 100, 37, 38, 25], [41, 42, 19, 20, 100, 12, 13, 11], [14, 15, 7, 8, 100, 39, 40, 24], [17, 18, 1, 2, 100, 22, 23, 21]]
        routinecheck=[]
        routinecheck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                        29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 100, 100, 100, 100, 100, 100]

        for i in range(6):
            for j in range(8):
                if routine[i][j] in routinecheck:
                    index = routinecheck.index(routine[i][j])
                    routinecheck.pop(index)
                else:
                    routine[i][j] = '*'
        #print(routine,"this is routine ")
        #print(routinecheck,"this is routine check")
        not_present = routinecheck[:]
        arr = [[0 for q in range(10)] for p in range(6)]
        for i in range(6):
            for j in range(8):
                arr[i][j] = routine[i][j]
        present = arr[:]





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

        elif lab_len == 2:
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

        mis_prac_smp=mis_prac[:]
        mis_lec_smp=mis_lec[:]
        mis_tut_smp=mis_tut[:]
    



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

        # print(mis_prac_smp,"mis prac")
        # print(mis_lec_smp,"mis prac")
        # print(mis_tut_smp,"mis prac")
        # print(not_present,"not present")
        # print(present,"present")

        if lab_len == 2:
            for i in range(6):
                for j in range(8):

                    if len(mis_prac_smp) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                        present[i][j] = 'prac'
                        mis_prac_smp.pop(0)
                        present[i][j + 1] = 'prac'
                        mis_prac_smp.pop(0)
                        

                    elif len(mis_lec_smp) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                        present[i][j] = 'Lec'
                        mis_lec_smp.pop(0)
                        present[i][j + 1] = 'Lec'
                        mis_lec_smp.pop(0)
                        
                    elif len(mis_tut_smp) != 0 and present[i][j] == '*':
                        present[i][j] = 'Tut'
                        mis_tut_smp.pop(0)
        
        #print(present,"this is present")
        present1 = present
        present1 = np.array(present1)
        present1.flatten()
        if '*' in present1:
            #print("this is return")
            return [],[]

        # Replacing missing class
        # if len(mis_prac)!=0:
        #         if 'prac'  not in  present1:
        #             print(lst1)
        #             print(lst2)
        #             print("cvsddddddddddddddddddddddddddddddddddddddddddddd")
        #             return [],[]
     
        if lab_len == 3:
            for i in range(6):
                #print(i)
                for j in range(8):
                    #print(j)
                    if present[i][j] == 'prac' and present[i][j + 1] == 'prac' and present[i][j + 2] == 'prac':
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

                    if present[i][j] == 'prac' and present[i][j + 1] == 'prac':
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
        routine_offspring = []
        for i in range(6):
            routine_offspring.append(present[i][:8])

        #print(routine_offspring) 
        routine_two_offspring.append(routine_offspring)
        
        chk = []
        overal_score = 0
        #print(routine_offspring)
        for i in range(6): 
            chk=routine_offspring[i]
            #print(chk)
            score = calcFitness(chk) 
            #print(score)
            overal_score += score  
        if overal_score==480:
            score_offspring_lst.append(overal_score)
            return routine_offspring,score_offspring_lst
        score_offspring_lst.append(overal_score)

    return routine_two_offspring, score_offspring_lst
    



