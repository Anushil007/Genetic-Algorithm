from labmatrix import lab_matrix
from teacher_code import LecturerCode
from copy import deepcopy

def lab_checkconflict(routine1,routine2):
    routine1=deepcopy(routine1)
    lab_routine1 = lab_matrix(routine1,2075)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer,lab_room, lab_room_lst = LecturerCode(2075)
    
    routine2=deepcopy(routine2)
    lab_routine2 = lab_matrix(routine2,2076)

    # print('This is lab routine of 2075')
    # print(lab_routine1)
    # print('This is lab routine of 2076')
    # print(lab_routine2)

    #for checking conflict
    for u in range(len(lab_room_lst)):
        for i in range(6):
            for j in range(8):
                lab_routine2[u][i][j] += lab_routine1[u][i][j]
    print(lab_routine2)


    score=0
    for u in range(len(lab_routine2)):
        for i in range(6):
            for j in range(8):
                a=lab_routine2[u][i][j]
                if a >= 3:
                    b=a-1
                    score=score-(10*b)
    return score

