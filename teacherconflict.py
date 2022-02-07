from teachermatrix import teacher_matrix
from teacher_code import LecturerCode
from copy import deepcopy

def lec_checkconflict(routine1,routine2):
    routine1=deepcopy(routine1)
    teacher_routine1 = teacher_matrix(routine1,2075)
    routine2=deepcopy(routine2)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(2075)
    #print(teacher_routine1,'this is teacher routine for 2075')
    teacher_routine2 = teacher_matrix(routine2,2076)
    codeLst2, lecCodeLst2, lectId2, lab_lst2, lab_lecturer2, lab_room2, lab_room_lst2, mylist1, mylist2, mylist3, lab_len = LecturerCode(2076)
    
    # for checking conflict
    for id in lectId2:
        if id in lectId:
            for i in range(6):
                for j in range(8):
                    index1 = lectId.index(id)
                    index2 = lectId2.index(id)
                    teacher_routine2[index2][i][j] += teacher_routine1[index1][i][j]

    #print(teacher_routine2)

    # for i in range(len(teacher_routine2)):
    #     print(lecCodeLst2[i])
    #     for j in range(len(teacher_routine2[i])):
    #         print(teacher_routine2[i][j])
            

    score=0
    for u in range(len(teacher_routine2)):
        for i in range(6):
            for j in range(8):
                a=teacher_routine2[u][i][j]
                if a==0:
                    pass
                elif a==1:
                    pass
                else:
                    b=a-1
                    score=score-(10*b)
    return score


            
   