from teacher_code import LecturerCode
from copy import deepcopy 
def teacher_matrix(routine,batch):
    teacher_routine=[]
    routine1=[]
    routine1=deepcopy(routine)
    #print(routine1)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst = LecturerCode(batch)
    for u in range(len(codeLst)):
        teacher_mat = [[0 for j in range(8)] for i in range(6)]
        for i in range(6):
            for j in range(8):
                if routine1[i][j] <= codeLst[u]:
                    teacher_mat[i][j] = 1
                    routine1[i][j] = 105
                else:
                    pass
        teacher_routine.append(teacher_mat)
    #print(teacher_routine)

    teacher_routine1 = []
    teacher_routine1 = teacher_routine

    # for lab class

    for u in range(len(lab_lst)):
        for i in range(6):
            for j in range(8):
                if routine1[i][j] <= lab_lst[u]:
                    for k in lab_lecturer[u]:
                        if k in codeLst:
                            index = codeLst.index(k)
                            teacher_routine1[index] [i][j] = 1
                            routine1[i][j] = 105
                else:
                    pass  

    #print(teacher_routine1,"this is after lab")  

    return  teacher_routine1      