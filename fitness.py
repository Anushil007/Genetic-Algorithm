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
routine_offspring=[[1, 2, 5, 100, 3, 4, 16, 17], [10, 11, 23, 24, 100, 34, 35, 36], [37, 38, 39, 100, 29, 30, 27, 28], [14, 15, 18, 19, 100, 6, 7, 22], [20, 21, 25, 26, 100, 8, 9, 33], [40, 41, 42, 100, 12, 13, 31, 32]]


overal_score=0
for i in range(6): 
            chk=routine_offspring[i]
            #print(chk)
            score = calcFitness(chk) 
            overal_score += score  
print(overal_score)