def LecturerCode(batch):
    if batch == 2075:
        codeLst = [5, 11, 17, 22, 28, 32, 33] 
        lecCodeLst = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB']
        lectId = [1, 2, 3, 4, 5, 6, 7]
        lab_lst = [36, 39, 42]
        lab_lecturer = [[5,11,22],[22,11,28],[5,11,17]]
        lab_room = [['Computer','Computer'],['Computer','Computer'],['Computer','Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics']
        mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],[25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
        mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
        lab_len = len(mylist2[0])
        mylist3 = [[5], [22], [33]]  # Single Period Class
        

    elif batch == 2076:
        codeLst = [6,10,15,20,24,28,32,33,34]
        lecCodeLst = ['AS','BK','SKS','BB','DK','SKR','DMG','PPB','RG']
        lectId = [8,9,10,1,15,14,4,13,16]
        lab_lst = [36,38,40,42]
        lab_lecturer = [[6,15],[6,20,28],[6,15],[20,24,34]]
        lab_lec = [['DG+SKS','AS+RN'],['AS+SKR','BB+PG'],
        ['DG+SKS','AS+RN'],['BB+PG','DK+RG']]
        lab_room = [['Computer','Computer'],['Instrumentation','Computer'],['Computer','Computer'],['Computer','Electrical']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics']
        mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[12,13],[14,15],[17,18],[19,20],[22,23],[26,27],[28,29],[30,31],[32,33]] #Double class
        mylist2 = [[35,36],[37,38],[39,40],[41,42]] #labs
        lab_len = len(mylist2[0])
        mylist3 = [[11],[16],[21],[24],[25],[34]] #single period

    elif batch == 2074:
        codeLst = [6,12,18,23,26,32]
        lecCodeLst = ['SS','SP','PG','PS','RP','AK']
        lectId = [18, 2, 19, 20, 21, 22]
        lab_lst = [35, 39, 42]
        lab_lecturer = [[65,66],[23,6,18], [6,32]]
        lab_lec = [['Project'], ['PS+SS','PG+KB'], ['SS+BB','AK+KB']]
        lab_room = [['Project', 'Project'], ['Computer','Computer'], ['Computer', 'Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics']
        mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[24,25],[27,28],[29,30],[31,32]]
        mylist2 = [[37,38,39],[40,41,42],[33,34,35]]
        lab_len = len(mylist2[0])
        mylist3 = [[36],[23],[26]]

    elif batch == 2077:
        codeLst = [5, 12, 16, 19, 23, 25, 27, 28, 29, 30]
        lecCodeLst = ['CD','MLP','BRM','DG','RPD','NRB', 'BK', 'TEST','RS', 'PL']
        lectId = [23, 24, 25, 11, 26, 27, 9, 28,12,17]
        lab_lst = [33,36,39,42]
        lab_lecturer = [[30], [30], [23,25,12], [23,25,26]]
        lab_lec = [[]]
        lab_room = []
        lab_room_lst = []
        mylist1 =[[1, 2], [3, 4], [6,7], [8,9], [10,11], [13, 14], [15, 16], [17, 18], [20, 21], [22, 23], [24, 25], [26, 27]]
        mylist2 =[[31,32,33], [34,35,36], [37,38,39], [40,41,42]]
        lab_len = len(mylist2[0])
        mylist3= [[5],[12],[19], [28], [29], [30]]

    return codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len


def allLecturerCode():
    lec_name = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB', 'AS','BK','SKS', 'DG', 'RS', 'PPB', 'SKR','DK','RG', 'PL', 'SS','PG','PS','RP','AK','CD','MLP','BRM','RPD','NRB', 'TEST','RS']
    lec_Id =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

    return lec_name, lec_Id

