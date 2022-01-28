
codeLst = [5, 11, 17, 22, 28, 32, 33] 
lecCodeLst = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB']

lab_lst = [36, 39, 42]
lab_lecturer = [[5,11,22],[22,11,28],[5,11,17]]

routine = [
            [34, 35, 36, 100, 16, 17, 10, 11], 
            [40, 41, 42, 100, 18, 19, 23, 24], 
            [29, 30, 3, 4, 100, 27, 28, 22], 
            [37, 38, 39, 100, 31, 32, 25, 26], 
            [8, 9, 20, 21, 100, 12, 13, 5], 
            [1, 2, 14, 15, 100, 6, 7, 33]
        ]

routine1 = []
routine1 = routine
teacher_routine = []

# for theory and tutorial class

for u in range(len(codeLst)):
    teacher_mat = [[1 for j in range(8)] for i in range(6)]
    for i in range(6):
        for j in range(8):
            if routine1[i][j] <= codeLst[u]:
                teacher_mat[i][j] = 0
                routine1[i][j] = 105
            else:
                pass
    teacher_routine.append(teacher_mat)

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
                        teacher_routine1[index] [i][j] = 0
                        routine1[i][j] = 105
            else:
                pass                   

for i in range(len(teacher_routine1)):
    print(lecCodeLst[i])
    for j in range(len(teacher_routine[i])):
        print(teacher_routine1[i][j])

