from teachermatrix import teacher_matrix
from teacher_code import LecturerCode
from copy import deepcopy
from teacher_code import allLecturerCode
import pickle
import os
from lab_conflict import lab_checkconflict
from labmatrix import lab_matrix

def lec_checkconflict(routine1, batch,overal_score):

    lec_name, lec_Id = allLecturerCode()
    #score_from_lab,allLabMatrix=lab_checkconflict(routine1, batch,overal_score)
    if batch==2079:
        allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lec_Id))]
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()
    with open('file6.txt','rb') as f:
        allLecturerMatrix=pickle.load(f)
    
    # for i in range(len(lec_Id)):
    #     print(lec_name[i])
    #     # index = lec_name.index(lec_name[i])
    #     # print(lec_Id[i])
    #     for j in range(6):
    #         print(allLecturerMatrix[i][j])

    routine=deepcopy(routine1)
    # print(routine)
    teacher_routine1 = teacher_matrix(routine,batch)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)


    # print('After calling teaacher routine')
    # for u in range(len(teacher_routine1)):
    #     name  =  lecCodeLst[u]
    #     print(name)
    #     for j in range(6):
    #         print(teacher_routine1[u][j])

    for id in lectId:
       for i in range(6):
            for j in range(8):
                index = lectId.index(id)
                allLecturerMatrix[id-1][i][j] += teacher_routine1[index][i][j]

    # print('After Addition')

    # for i in range(len(lec_Id)):
    #     print(lec_name[i])
    #     # index = lec_name.index(lec_name[i])
    #     # print(lec_Id[i])
    #     for j in range(6):
    #         print(allLecturerMatrix[i][j])


    

   
    score=0
    b=0
    for u in range(len(allLecturerMatrix)):
     for i in range(6):
            for j in range(8):
                a=allLecturerMatrix[u][i][j]
                if a>1:
                    b=a-1
                    score=score-(10*b)
                    
    # print('Hi I am a score', score)
    


    if batch==2079:
        allLabMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lab_room_lst))]
        with open('file7.txt','wb') as f:
            pickle.dump(allLabMatrix,f)
        f.close()
    with open('file7.txt','rb') as f:
        allLabMatrix=pickle.load(f)
    ##print(allLabMatrix)
    routine1=deepcopy(routine1)
    lab_routine1 = lab_matrix(routine1,batch)
    #print(lab_routine1)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer,lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
  

    for u in range(len(lab_room_lst)):
        for i in range(6):
            for j in range(8):
                allLabMatrix[u][i][j] += lab_routine1[u][i][j]
    #print(allLabMatrix)


    scorelab=0
    b=0
    for u in range(len(allLabMatrix)):
        for i in range(6):
            for j in range(8):
                a=allLabMatrix[u][i][j]
                if a >4:
                    b=a-4
                    scorelab=scorelab-(10*b)

    
    if score==0 and scorelab==0 and overal_score==480:
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()

        with open('file7.txt','wb') as f:
            pickle.dump(allLabMatrix,f)
        f.close()

        lec_name, lec_Id = allLecturerCode()

        if batch==2080:
            #for i in range(len(lec_Id)):
            for i in range(len(lec_Id)):
                print(lec_name[i])
                index = lec_name.index(lec_name[i])
                print(lec_Id[i])
                for j in range(6):
                    print(allLecturerMatrix[i][j])

            print(allLabMatrix)



    return score+scorelab



# from teachermatrix import teacher_matrix
# from teacher_code import LecturerCode
# from copy import deepcopy
# from teacher_code import allLecturerCode
# import pickle
# import os
# from lab_conflict import lab_checkconflict
# from labmatrix import lab_matrix

# def lec_checkconflict(routine1, batch,overal_score):
#    # print(routine1)
#     #score_from_lab,allLabMatrix=lab_checkconflict(routine1, batch,overal_score)
#     if batch==2074:
#         allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(36)]
#         with open('file6.txt','wb') as f:
#             pickle.dump(allLecturerMatrix,f)
#         f.close()
#     with open('file6.txt','rb') as f:
#         allLecturerMatrix=pickle.load(f)
#     routine=deepcopy(routine1)
#     teacher_routine1 = teacher_matrix(routine,batch)
#     codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)

#     for id in lectId:
#        for i in range(6):
#             for j in range(8):
#                 index = lectId.index(id)
#                 allLecturerMatrix[id-1][i][j] += teacher_routine1[index][i][j]

   
#     score=0
#     b=0
#     for u in range(len(allLecturerMatrix)):
#      for i in range(6):
#             for j in range(8):
#                 a=allLecturerMatrix[u][i][j]
#                 if a>1:
#                     b=a-1
#                     score=score-(10*b)
                    

#     lec_name, lec_Id = allLecturerCode()


#     if batch==2074:
#         allLabMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(10)]
#         with open('file7.txt','wb') as f:
#             pickle.dump(allLabMatrix,f)
#         f.close()
#     with open('file7.txt','rb') as f:
#         allLabMatrix=pickle.load(f)
#     ##print(allLabMatrix)
#     routine1=deepcopy(routine1)
#     lab_routine1 = lab_matrix(routine1,batch)
#     #print(lab_routine1)
#     codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer,lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
  

#     for u in range(len(lab_room_lst)):
#         for i in range(6):
#             for j in range(8):
#                 allLabMatrix[u][i][j] += lab_routine1[u][i][j]
#     #print(allLabMatrix)


#     scorelab=0
#     b=0
#     for u in range(len(allLabMatrix)):
#         for i in range(6):
#             for j in range(8):
#                 a=allLabMatrix[u][i][j]
#                 if a >4 :
#                     b=a-2
#                     scorelab=scorelab-(10*b)
#                 # elif u==9:
#                 #     pass
#                 # elif a>1 and u!=0 and u!=9: 
#                 #     b=a-1
#                 #     scorelab=scorelab-(10*b)


                


    
#     if score==0 and scorelab==0 and overal_score==480:
#         with open('file6.txt','wb') as f:
#             pickle.dump(allLecturerMatrix,f)
#         f.close()

#         with open('file7.txt','wb') as f:
#             pickle.dump(allLabMatrix,f)
#         f.close()

#         lec_name, lec_Id = allLecturerCode()

#         if batch==2080:
#             #for i in range(len(lec_Id)):
#             for i in range(36):
#                 print(lec_name[i])
#                 index = lec_name.index(lec_name[i])
#                 print(lec_Id[i])
#                 for j in range(6):
#                     print(allLecturerMatrix[i][j])

#             print(allLabMatrix)



#     return score+scorelab
    
   