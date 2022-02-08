from teachermatrix import teacher_matrix
from teacher_code import LecturerCode
from copy import deepcopy
from teacher_code import allLecturerCode
import pickle
import os


def lec_checkconflict(routine1, batch,overal_score):
    if batch==2075:
        allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(1, 29)]
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
                if a==0:
                    pass
                elif a==1:
                    pass
                else:
                    b=a-1
                    score=score-(10*b)
                    

    lec_name, lec_Id = allLecturerCode()
    # for i in range(len(allLecturerMatrix)):
    #     print(lec_name[i])
    #     index = lec_name.index(lec_name[i])
    #     print(lec_Id[index])
    #     for j in range(6):
    #         print(allLecturerMatrix[i][j])

    
    if score==0 and overal_score==480:
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()





    return score
    
   

