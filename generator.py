from initial_population import PopulationGeneration, overal_routine, oneDArray
from fitness import calcFitness
from roulette_selection import selection
from crossover import partial_crossover
import pickle
from teacherconflict import lec_checkconflict
from lab_conflict import lab_checkconflict
#from routine_info import saveroutine
#from teachermatrix import teacher_matrix
  
def generator(batch):

    
    
    score_lst = []

    routine_lst = []

    # semester_routine = float(input("Enter the batch number:"))

    for i in range(6):
        if batch== 2075:
            mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],[25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
            mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
            lab_len = len(mylist2[0])
            mylist3 = [[5], [22], [33]]  # Single Period Class

        elif batch== 2076:
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
            score = calcFitness(chk,batch) 
            #print(score)
            overal_score += score 
        scoreconflict=0
        if batch != 2075:
            with open('file4.txt','rb') as f:
                routine_2075=pickle.load(f) 
            scoreconflict=lec_checkconflict(routine_2075,lst3)
            overal_score=overal_score+scoreconflict 
            scoreconflict1 = lab_checkconflict(routine_2075, lst3)
            overal_score=overal_score+scoreconflict1 

        #print(overal_score)
        overal_routine[i] = matrix1
       
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
    while 480 not in score_lst and count<100:
        if 1:
            routine1_lst = []
            score1_lst = []
            a=routine_lst[0].copy()
            b=routine_lst[1].copy()
            routine1_lst, score1_lst = partial_crossover(a,b, lab_len,batch)
            c=0
            while(len(routine1_lst) == 0 and len(score1_lst)==0) and c<100:
                c=c+1
                a=routine_lst[0].copy()
                b=routine_lst[1].copy()
                routine1_lst, score1_lst = partial_crossover(a,b, lab_len,batch)  
            if len(score1_lst)==0:
                score_lst,routine_lst=generator(batch)
                print('this is inside if')
                return score_lst,routine_lst
            elif len(score1_lst)==1:
                score_lst[0]=score1_lst[0]
                routine_lst[0]= routine1_lst[0]
            else:
                for j in range(2):
                    routine_lst[j] = routine1_lst[j]
                    score_lst[j]= score1_lst[j]
            routine_lst, score_lst = selection(score_lst, routine_lst)
            count=count+1
            #print(count)
            #print(score_lst,routine_lst,'this is score list and routine list')
    return(score_lst,routine_lst)

# for i in range(50):
score=[]
routine=[]
batch=2075
routine_2075=[]
score,routine=generator(batch)
while 480 not in score:
    score,routine=generator(batch)
print("this is right routine for 2075",routine[0])
routine_2075=routine[0]
with open('file4.txt','wb') as f:
    pickle.dump(routine[0],f)
with open('file4.txt','rb') as f:
    routine_2075=pickle.load(f)

batch=2076
score,routine=generator(batch)
while 480 not in score:
    score,routine=generator(batch)
print("this is right routine for 2076",routine[0],score)
    # print(i)






