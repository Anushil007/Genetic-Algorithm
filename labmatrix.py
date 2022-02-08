from teacher_code import LecturerCode
from copy import deepcopy


def lab_matrix(routine, batch):
    routine1=deepcopy(routine)
    #print(routine1)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer,lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
    for i in range(6):
        for j in range(8):
            if routine1[i][j] <= (lab_lst[0] - len(lab_lecturer[0])):
                routine1[i][j] = 105
            else:
                pass

    # print(routine)


    lab_routine = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lab_room_lst))]
    # print(lab_routine)


    for u in range(len(lab_lst)):
        for i in range(6):
            for j in range(8):
                if routine1[i][j] <= lab_lst[u]:
                    for k in range(len(lab_room[u])):
                        index = lab_room_lst.index(lab_room[u][k])
                        # print(index)
                        # print(lab_room[u][k])
                        # print(lab_room_lst[index])
                        if lab_room[u][k] == lab_room_lst[index]:
                            #if routine_2075[i][j] <= lab_lst_2075[u]:
                            lab_routine[index][i][j] += 1
                        else:
                            pass
                    routine1[i][j] = 105
                else:
                    pass
    return lab_routine 

