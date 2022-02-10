def LecturerCode(batch):
    if batch == 2075:
        codeLst = [5, 11, 17, 22, 28, 32, 33] 
        lecCodeLst = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB']
        lectId = [1, 2, 3, 4, 5, 6, 7]
        lab_lst = [36, 39, 42]
        lab_lecturer = [[1,2,4], [4,2,5], [1,2,3]]
       # lab_lecturer = [[1], [4], [1]]
        #lab_lecturer = [[5,11,22],[22,11,28],[5,11,17]]
        lab_room = [['Computer','Computer'],['Computer','Computer'],['Computer','Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics''Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],[25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
        mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
        lab_len = len(mylist2[0])
        mylist3 = [[5], [22], [33]]  # Single Period Class
        

    elif batch == 2076:
        codeLst = [6,10,15,20,24,28,32,33,34]
        lecCodeLst = ['AS','BK','SKS','BB','DK','SKR','DMG','PPB','RG','DG','RN','PG']
        lectId = [8,9,10,1,15,14,4,13,16,11,30,19]
        lab_lst = [36,38,40,42]
     #   lab_lecturer = [[11,10,8,30],[8,14,1,19],[11,10,8,30],[1,19,15,16]]
        lab_lecturer = [[11,10,8,30],[8,14,1,19],[11,10,8,30],[1,19,15,16]]

        #lab_lecturer = [[6,15],[6,20,28],[6,15],[20,24,34]]
        lab_lec = [['DG+SKS','AS+RN'], ['AS+SKR','BB+PG'], ['DG+SKS','AS+RN'], ['BB+PG','DK+RG']]
        lab_room = [['Computer','Computer'],['Instrumentation','Computer'],['Computer','Computer'],['Computer','Electrical']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[16,17],[18,19],[21,22],[23,24],[25,26],[27,28],[29,30]] #Double class
        mylist2 = [[35,36],[37,38],[39,40],[41,42]] #labs
        lab_len = len(mylist2[0])
        mylist3 = [[15],[20],[31],[32],[33],[34]] #single period

    elif batch == 2074:
        codeLst = [6,12,18,23,26,32,33]
        lecCodeLst = ['SS','SP','PG','PS','RP','AK','Supervisor', 'BB', 'KB']
        lectId = [     18,  2,   19,  20,  21,  22,   29,           1,   31]
        lab_lst = [36, 39, 42]
        lab_lecturer = [[29],[20,18,19,31], [18,1,22,31]]
        lab_lec = [['Supervisor'], ['PS+SS','PG+KB'], ['SS+BB','AK+KB']]
        lab_room = [['Project', 'Project'], ['Computer','Computer'], ['Computer', 'Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[24,25],[27,28],[29,30],[31,32]]
        mylist2 = [[37,38,39],[40,41,42],[34,35,36]]
        lab_len = len(mylist2[0])
        mylist3 = [[33],[23],[26]]

    elif batch == 2077:
        codeLst = [5, 12, 16, 19, 23, 25, 27, 28, 29, 30]
        lecCodeLst = ['CD','MLP','BRM','DG','RPD','NRB', 'BK', 'TEST','PL', 'RP', 'SN']
        lectId = [     23,   24,   25,  11,   26,   27,    9,    28,   17,  32,    33]
        lab_lst = [33,36,39,42]
        lab_lecturer = [[17,32], [17,32], [26,27,24,33], [26,27,25,]]
        lab_lec = [[]]
        lab_room = [['Drawing','Workshop'],['Drawing','Workshop'],['Chemistry','Thermodynamics'],['Chemistry','Electronics']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1 =[[1, 2], [3, 4], [6,7], [8,9], [10,11], [13, 14], [15, 16], [17, 18], [20, 21], [22, 23], [24, 25], [26, 27]]
        mylist2 =[[31,32,33], [34,35,36], [37,38,39], [40,41,42]]
        lab_len = len(mylist2[0])
        mylist3= [[5],[12],[19], [28], [29], [30]]

    
    #for elec 1st year
    elif batch == 2078:
        codeLst = [4, 11, 15, 18, 22, 24, 27, 28, 29, 30]
        lecCodeLst = ['CD','MLP','BRM','DG','RPD','NRB', 'BK', 'TEST','RS', 'RP','PL','SN', 'NK']
        lectId = [     23,  24,   25,   11,  26,    27,   9,     28,   12,   32,  17,  33,   34]
        lab_lst = [33,36,39,42]
        lab_lecturer = [[12,17,32], [12,17,32], [26,27,24,33], [26,27,25,34]]
        lab_lec = [['RS+PL','RP'],['RS+PL','RP'],['RPD+NRB','MLP+SN'],['RPD+NRB','BRM+NK']]
        lab_room = [['Drawing','Workshop'],['Drawing','Workshop'],['Chemistry','Thermodynamics'],['Chemistry','Electronics']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1 =[[1, 2], [3, 4], [5,6], [7,8], [9,10], [12,13], [14,15], [16, 17], [19,20], [21, 22], [23, 24], [25, 26]]
        mylist2 =[[31,32,33], [34,35,36], [37,38,39], [40,41,42]]
        lab_len = len(mylist2[0])
        mylist3= [[11],[18],[27], [28], [29], [30]]  


    
        
    #for elec 2nd year 
    elif batch == 2079:
        codeLst=[6,11,17,20,26,28,33]
        lecCodeLst=['TN','DG','AS','BK','DK','PPB','SKR', 'RG', 'GT', 'SKS', 'RN', 'BRM']
        lectId=[     35,  11,   8,  9,   15,   13,  14,    16,    36,   10,   30,    25]
        lab_lst =[36,39,42]
        lab_lecturer=[[15,16,36,14],[11,10,30,8],[11,10,25,8]]
        lab_lec =[['DK+RG','GT+SKR'],['DG+SKS','RN+AS'],['DG+SKS','BRM'+'AS']]
        lab_room=[['Electrical','Instrumentation'],['Computer','Computer'],['Computer','Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1=[[1,2],[3,4],[5,6],[7,8],[9,10],[12,13],[14,15],[16,17],[18,19],[21,22],[23,24],[25,26],[27,28],[29,30],[31,32]]
        mylist2=[[34,35,36],[37,38,39],[40,41,42]]
        lab_len = len(mylist2[0])
        mylist3=[[11],[20],[33]]

    # for elec 3rd year
    elif batch == 2080:
        codeLst=[6,11,16,22,26,30,32,33]
        lecCodeLst=['RUG','SKS','GCJ','RG','SD','NS','AD','YB','SL','IMS','RN','TN','GT']
        lectId= [    37,    10,   44,   16,  45,  47,  46,  7,   48,  49,  30,   35,  36]
        lab_lst =[36,39,42]
        lab_lecturer=[[37,48,47,46],[49,30,10],[35,36,16,49]]
        lab_lec =[['RuG+SL','NS+AD'],['IMS+RN','SKS'],['TN+GT','RG+IMS']]
        lab_room=[['Electrical','Hydropower'],['Computer','Electrical'],['Computer','Electrical']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project', 'Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1=[[1,2],[3,4],[5,6],[7,8],[9,10],[12,13],[14,15],[17,18],[19,20],[21,22],[23,24],[25,26],[27,28],[29,30],[31,32]]
        mylist2=[[34,35,36],[37,38,39],[40,41,42]]
        lab_len = len(mylist2[0])
        mylist3=[[11],[16],[33]]



    # for elec 4th year
    elif batch==2081:
        codeLst = [6,12,18,24]
        lecCodeLst = ['AJS','RUG','TN','DK','APS','PV','YB','RP','SDH','AB','TBM','Supervisor1']
        lectId = [     38,   37,   35,  15,  39,   40,   7,  21,   41,  42,  43,    50]
        lab_lst = [27,30,33,36, 39, 42]
        lab_lecturer = [[39,40,7],[50], [21], [39,41,40,7], [37,42,35,43], [37,42,35,43]]
        lab_lec = [['APS','PV+YB'], ['Supervisor1'],['RP'],['APS+SDH','PV+YB'],['RUG+AB','TN+TBM'],['RUG+AB','TN+TBM']]
        lab_room = [['Class1', 'Class2'], ['Project','Project'],['Class1'],['Class1', 'Class2'],['Hydropower', 'Switchgear'],['Hydropower', 'Switchgear']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[23,24]]
        mylist2 = [[25,26,27],[28,29,30],[31,32,33],[34,35,36],[37,38,39],[40,41,42]]
        lab_len = len(mylist2[0])
        mylist3 = []



    return codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len


def allLecturerCode():
    lec_name = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB', 'AS','BK','SKS', 'DG', 'RS', 'PPB', 'SKR','DK','RG', 'PL', 'SS','PG','PS','RP','AK','CD','MLP','BRM','RPD','NRB', 'TEST', 'Supervisor','RN', 'KB','RP', 'SN', 'NK', 'TN', 'GT', 'RUG', 'AJS', 'APS', 'PV', 'SDH', 'AB', 'TBM', 'GCJ', 'SD', 'AD', 'NS','SL', 'IMS','Supervisor1']
    lec_Id =  [  1,    2,    3,     4,     5,     6,    7,    8,   9,   10,   11,   12,    13,    14,  15,  16,   17,   18,  19,  20,  21,  22,  23,  24,    25,   26,   27,    28,       29,        30,   31,  32,  33,   34,    35,   36,   37,    38,    39,   40,    41,    42,  43,     44,    45,   46,  47,  48,    49 ,   50]

    return lec_name, lec_Id