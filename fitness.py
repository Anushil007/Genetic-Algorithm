from initial_population import *
from teacher_code import LecturerCode
#from routine_info import saveroutine
chk=[]

def calcFitness(chk,batch):
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer=LecturerCode(batch)



    lecCount = [0 for i in range(len(lectId))]
    a = 0
    b = 0
    j = 0
    while(j <= (len(lectId)-1)):
        if(a>7):
            break
        elif(chk[a] <= codeLst[j]):
            lecCount[j] += 1
            #print(lecCount)
            j=0
            a=a+1
        elif chk[a] >=(codeLst[-1]+1):
            b += 1
            a += 1
            j=0
            pass
        
        else: 
            j += 1
            pass

    #print(lecCount)

    score=0
    for j in range(len(lecCount)):
        if(lecCount[j]<=2):
            #print(lecCount[j])
            score+= (lecCount[j])*10  # no-conflict = 10
            #print(score)
        else:
            conflict = 0
            #print(lecCount[j])
            conflict=(lecCount[j]-2)
            score+=(conflict*(-10))+(2*10)   # conflict = -10
            #print(score)

    #print("this is fitness")

    score+=(b*10)
    
    return score
     
