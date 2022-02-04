    
def generator():

    
    from initial_population import PopulationGeneration, overal_routine, oneDArray
    from fitness import calcFitness
    from roulette_selection import selection
    from crossover import partial_crossover
    from teachermatrix import teacher_matrix

    score_lst = []

    routine_lst = []

    # semester_routine = float(input("Enter the batch number:"))
    semester_routine = 2075

    for i in range(6):
        if semester_routine == 2075:
            mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],[25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
            mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
            lab_len = len(mylist2[0])
            mylist3 = [[5], [22], [33]]  # Single Period Class

        elif semester_routine == 2076:
            mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[12,13],[14,15],[17,18],[19,20],[22,23],[26,27],[28,29],[30,31],[32,33]] #Double class
            mylist2 = [[35,36],[37,38],[39,40],[41,42]] #labs
            lab_len = len(mylist2[0])
            mylist3 = [[11],[16],[21],[24],[25],[34]] #single period
        else:
            pass


        routine = PopulationGeneration(mylist1, mylist2, mylist3)


        # fitness calculation

        matrix = []
        matrix1 = []
        matrix = oneDArray(routine)   # generates onedimensional of routine
        #print(matrix)
        matrix1 = oneDArray(matrix)   # generates onedimensional of population
        #print(matrix1)
        #print(len(matrix1))

        arr = [[0 for q in range(8)] for p in range(6)]
        count = 0
        for p in range(6):
            for q in range(8):
                arr[p][q] = matrix1[count]
                count += 1


        #print(lst)
        lst3 = arr
        routine_lst.append(lst3)
        #print(lst3)

        # if semester_routine != 2075:
        #     teacher_matrix(lst3)


        overal_score = 0 
        chk = []
        for i in range(6): 
            chk=lst3[i]
            #print(chk)
            score = calcFitness(chk) 
            #print(score)
            overal_score += score  

        #print(overal_score)
        overal_routine[i] = matrix1
        #print(overal_routine[i])
        #print(len(matrix1))
        #print(overal_score)
        score_lst.append(overal_score)


    # selection part

    routine_lst, score_lst = selection(score_lst, routine_lst)
    # print(routine_lst)
    # print(score_lst)
    c=[]
    c.append(routine_lst)
    a=routine_lst[0].copy()
    b=routine_lst[1].copy()
    #crossover part
    i = 0
    j = 0
    count=0
    while 480 not in score_lst:
        
        #print(i)
        #print(score_lst[i])
        

        if 1:
            #print(score_lst[i])
            #print(routine_lst[0])
            #print(routine_lst[1])
            routine1_lst = []
            score1_lst = []
            a=routine_lst[0].copy()
            b=routine_lst[1].copy()
            if count>100:
                generator()
                break


            # while 1:
            #     try:
            #         routine1_lst, score1_lst = partial_crossover(routine_lst[0],routine_lst[1], lab_len)
            #         break
            #     except IndexError as error:
            #         print('One')
            #         routine1_lst, score1_lst = partial_crossover(routine_lst[0],routine_lst[1], lab_len)
            #     else:
            #         break

            routine1_lst, score1_lst = partial_crossover(a,b, lab_len)
            #print("this is first")
            #print(routine1_lst)
            #print(score1_lst)

            
            while(len(routine1_lst) == 0 and len(score1_lst)==0):
                #print(c,"this isn c")
                a=routine_lst[0].copy()
                b=routine_lst[1].copy()
                routine1_lst, score1_lst = partial_crossover(a,b, lab_len)   


            if len(score1_lst)==1:
                score_lst[0]=score1_lst[0]
                routine_lst[0]= routine1_lst[0]

            else:
                for j in range(2):
                    routine_lst[j] = routine1_lst[j]
                    score_lst[j]= score1_lst[j]
            #print(routine_lst)
            #print(score_lst)
            routine_lst, score_lst = selection(score_lst, routine_lst)
            print(score_lst,"this is score")
            count=count+1
            print(count)

generator()




