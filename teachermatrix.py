from teacher_code import LecturerCode, allLecturerCode
from copy import deepcopy 



def teacher_matrix(routine,batch):
    routine1=[]
    routine1=deepcopy(routine)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
    teacher_routine = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lectId))]


    # for theory and tutorial class
    for u in range(len(codeLst)):
        for i in range(6):
            for j in range(8):
                if routine1[i][j] <= codeLst[u]:
                    teacher_routine[u][i][j] = 1
                    routine1[i][j] = 105
                else:
                    pass


    # for lab class
    for id in range(len(lectId)):
        for u in range(len(lab_lst)):
            for i in range(6):
                for j in range(8):
                    if routine1[i][j] <= lab_lst[u]:
                        for k in lab_lecturer[u]:
                            if k in lectId:
                                index = lectId.index(k)
                                teacher_routine[index] [i][j] = 1
                        routine1[i][j] = 105        
                    else:
                        pass  

    return teacher_routine
    # for u in range(len(teacher_routine)):
    #     name  =  lecCodeLst[u]
    #     print(name)
    #     for j in range(6):
    #         print(teacher_routine[u][j])





# routine = [
#     [40, 41, 42, 100, 6, 7, 3, 4],
#     [34, 35, 36, 100, 25, 26, 20, 21], 
#     [14, 15, 27, 28, 100, 8, 9, 5], 
#     [1, 2, 18, 19, 100, 37, 38, 39],
#     [12, 13, 23, 24, 100, 31, 32, 33], 
#     [10, 11, 29, 30, 100, 16, 17, 22]
#   ]
# teacher_matrix(routine, 2075)

# print("I am from Second Year.")


# routine2 = [[30, 31, 3, 4, 100, 26, 27, 24], 
# [9, 10, 5, 6, 100, 37, 38, 34], 
# [39, 40, 19, 20, 100, 1, 2, 25],
#  [35, 36, 12, 13, 100, 17, 18, 21], 
#  [41, 42, 14, 15, 100, 22, 23, 16],
#   [7, 8, 32, 33, 100, 28, 29, 11]]
# teacher_matrix(routine2, 2076)