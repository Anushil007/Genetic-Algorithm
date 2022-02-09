from teachermatrix import teacher_matrix
from teacher_code import LecturerCode
from copy import deepcopy
from teacher_code import allLecturerCode
import pickle
import os
from lab_conflict import lab_checkconflict

def lec_checkconflict(routine1, batch,overal_score):
   # print(routine1)
    print(overal_score)

    #score_from_lab,allLabMatrix=lab_checkconflict(routine1, batch,overal_score)
    if batch==2075:
        allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(28)]
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()
    with open('file6.txt','rb') as f:
        allLecturerMatrix=pickle.load(f)
    routine=deepcopy(routine1)
    teacher_routine1 = teacher_matrix(routine,batch)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)

    for id in lectId:
       for i in range(6):
            for j in range(8):
                index = lectId.index(id)
                allLecturerMatrix[id-1][i][j] += teacher_routine1[index][i][j]

   
    score=0
    b=0
    for u in range(len(allLecturerMatrix)):
     for i in range(6):
            for j in range(8):
                a=allLecturerMatrix[u][i][j]
                if a>1:
                    b=a-1
                    score=score-(10*b)
                    

    lec_name, lec_Id = allLecturerCode()
    
    if score==0 and overal_score==480:
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()

        lec_name, lec_Id = allLecturerCode()

        if batch==2077:
            for i in range(28):
                print(lec_name[i])
                index = lec_name.index(lec_name[i])
                print(lec_Id[i])
                for j in range(6):
                    print(allLecturerMatrix[i][j])

    print(score+overal_score)


    return score
    
   
