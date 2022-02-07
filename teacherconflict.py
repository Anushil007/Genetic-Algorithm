from teachermatrix import teacher_matrix
from teacher_code import LecturerCode
from copy import deepcopy
import pickle




def lec_checkconflict(routine1, batch):
    # main(allLecturerMatrix)
    routine1=deepcopy(routine1)
    teacher_routine1 = teacher_matrix(routine1,2075)
    # routine2=deepcopy(routine2)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
    #print(teacher_routine1,'this is teacher routine for 2075')
    # teacher_routine2 = teacher_matrix(routine2,2076)
    # codeLst2, lecCodeLst2, lectId2, lab_lst2, lab_lecturer2, lab_room2, lab_room_lst2, mylist1, mylist2, mylist3, lab_len = LecturerCode(2076)
    
    with open('file3.txt','rb') as f:
        allLecturerMatrix=pickle.load(f) 
    
    print(allLecturerMatrix)

    # for u in range(len(teacher_routine1)):
    #     id =  lectId[u]
    #     print(id)
    #     allLecturerMatrix[id-1] = teacher_routine1[u]

    # for checking conflict
    # for id in lectId2:
    #     if id in lectId:
    #         for i in range(6):
    #             for j in range(8):
    #                 index1 = lectId.index(id)
    #                 index2 = lectId2.index(id)
    #                 teacher_routine2[index2][i][j] += teacher_routine1[index1][i][j]


    for id in lectId:
        print(id)
        for k in range(len(allLecturerMatrix)):
            for i in range(6):
                for j in range(8):
                    # print(id, "This is id.")
                    # print(allLecturerMatrix)
                    index = lectId.index(id)
                    print(index)
                    allLecturerMatrix[id-1][i][j] += teacher_routine1[index][i][j]
            print(allLecturerMatrix)
    
    # main(allLecturerMatrix)



    #print(teacher_routine2)

    # for i in range(len(teacher_routine2)):
    #     print(lecCodeLst2[i])
    #     for j in range(len(teacher_routine2[i])):
    #         print(teacher_routine2[i][j])
            

    score=0
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
    if score == 0:
        with open('file3.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)

    return score


            
routine2 = [[30, 31, 3, 4, 100, 26, 27, 24], [9, 10, 5, 6, 100, 37, 38, 34], [39, 40, 19, 20, 100, 1, 2, 25], [35, 36, 12, 13, 100, 17, 18, 21], [41, 42, 14, 15, 100, 22, 23, 16], [7, 8, 32, 33, 100, 28, 29, 11]]   
score = lec_checkconflict(routine2, 2076)