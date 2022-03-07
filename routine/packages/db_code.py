
def input_lst(lst):
    newlist = []
    for word in lst:
        word = word.split(",")
        newlist.extend(word)  # <----
    
    return newlist


def code_db_calc(c):
    x = 0
    codeLst1 = []
    codeLst = []
    lecCodeLst = []
    lectId = []

    for code in c:
        #print(code.Lecturer_Id)
        lectId.append(code.Lecturer_Id)
        #print(code.Lecturer_Code)
        lecCodeLst.append(code.Lecturer_Code)
        #print(code.Lecturer_Period)
        #print(codeLst)
        codeLst1.append(code.Lecturer_Period)
        if (code.Lecturer_Period)!= 0:
            x = x + code.Lecturer_Period
            codeLst.append(x)
        else:
            codeLst.append(0)

    #print(codeLst1)
    # print(codeLst)
    # print(lecCodeLst)
    # print(lectId)

    


    
    lab_room1 = []
    lab_lecturer1 = []
    for code in c:
        if code.Lab_Class != '':
            lab_room1.append(code.Lab_Class)
        if code.Lab_Lec_Period != None:
            lab_lecturer1.append(code.Lab_Lec_Period)
    

    lab_room = []
    lab_lecturer = []
    lab_lst = []
    mylist1 = []
    mylist3 = []
    mylist2 = []
    if codeLst != []:
        maxm = max(codeLst)
        for i in range(len(lab_room1)):
            lst1 = []
            lst2 = []
            lst1.append(lab_room1[i])
            lab_room.append(input_lst(input_lst(lst1)))
            lst2.append(lab_lecturer1[i])
            x = input_lst(lst2)
            lab_lecturer.append(list(map(int, x)))

            lab_lst.append(maxm+3)
            maxm = maxm + 3
        
        
        period = 0
        for i in range(len(codeLst)):
            #print(period)
            m = codeLst[i]
            #print(m)
            if m != 0:
                value = codeLst1[i]
                #print(value)
                y = value % 2
                if y == 1:
                    #print(period)
                    while(period < m):
                        if ((m-period) > 1):
                            period_lec_list = []
                            period += 1
                            period_lec_list.append(period)
                            period += 1
                            period_lec_list.append(period)
                            mylist1.append(period_lec_list)
                        else:
                            period += 1
                            period_tut_list = []
                            period_tut_list.append(period)
                            mylist3.append(period_tut_list)
                else:
                    #print(period)
                    while(period < m):
                        if ((m-period) > 1):
                            period_lec_list = []
                            period += 1
                            period_lec_list.append(period)
                            period += 1
                            period_lec_list.append(period)
                            mylist1.append(period_lec_list)


                period = m
            else:
                pass
        
        for i in range(len(lab_lst)):
            m = lab_lst[i]
            while(period < m):
                if ((m-period) > 1):
                    period_lab_list = []
                    period += 1
                    period_lab_list.append(period)
                    period += 1
                    period_lab_list.append(period)
                    period += 1
                    period_lab_list.append(period)
                    mylist2.append(period_lab_list)
        #print(mylist2)
            


    return codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2,mylist3

    # for j in range(len(lab_lst)):
    #     m = lab_lst[j]

    #     while(period < m):
    #         if ((m-period) > 1):
    #             period_lab_list = []
    #             period += 1
    #             period_lec_list.append(period)
    #             period += 1
    #             period_lec_list.append(period)
    #             mylist1.append(period_lec_list)
