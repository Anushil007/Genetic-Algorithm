from initial_population import *


codeLst = [5, 11, 17, 22, 28, 32, 33] 
lecCodeLst = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB']

chk = []

def calcFitness(chk):

    lecCount = [0 for i in range(7)]
    a = 0
    b = 0
    j = 0
    while(j <= 6):
        if(a>7):
            break
        elif(chk[a] <= codeLst[j]):
            lecCount[j] += 1
            #print(lecCount)
            j=0
            a=a+1
        elif chk[a] >= 34:
            b += 1
            a += 1
            j=0
            pass
        
        else: 
            j += 1
            pass

    #print(lecCount)

    score=0
    for j in range(7):
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

    #print(b)

    score+=(b*10)
    #print(score)
    
    return score