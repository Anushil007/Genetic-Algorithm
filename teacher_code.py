def LecturerCode(batch):
    if batch == 2075:
        codeLst = [5, 11, 17, 22, 28, 32, 33] 
        lecCodeLst = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB']
        lectId = [1, 2, 3, 4, 5, 6, 7]
        lab_lst = [36, 39, 42]
        lab_lecturer = [[5,11,22],[22,11,28],[5,11,17]]

    elif batch == 2076:
        codeLst = [6,10,15,20,24,28,32,33,34]
        lecCodeLst = ['AS','BK','SKS','BB','DK','SKR','DMG','PPB','RG']
        lectId = [8,9,10,1,15,14,4,13,16]
        lab_lst = [36,38,40,42]
        lab_lecturer = [[6,15],[6,20,28],[6,15],[20,24,34]]
        lab_lec = [['DG+SKS','AS+RN'],['AS+SKR','BB+PG'],
        ['DG+SKS','AS+RN'],['BB+PG','DK+RG']]

    return codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer
