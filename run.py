from generator import generator
import sys
def call():
    score=[]
    routine=[]
    batch=2074
    routine_2075=[]
    score,routine=generator(batch)
    x=0
    while 480 not in score :
            score,routine=generator(batch)
    if len(score)==1:
        print("this is right routine for 2074",routine,score)
    else:
        print("this is right routine for 2074",routine[0],score)



    # x=0
    # batch=2079
    # score,routine=generator(batch)
    # while 480 not in score:
    #     if x<10:
    #         print(x)
    #         x=x+1
    #         score,routine=generator(batch)
            
    #     else:
    #         call()
    # if len(score)==1:
    #     print("this is right routine for 2079",routine,score)
    # else:
    #     print("this is right routine for 2079",routine[0],score)
    

    x=0
    batch=2075
    score,routine=generator(batch)
    while 480 not in score :
        if x<10:
            x=x+1
            score,routine=generator(batch)
        else:
            call()
    if len(score)==1:
        print("this is right routine for 2075",routine,score)
    else:
        print("this is right routine for 2075",routine[0],score)
    


    x=0
    batch=2076
    score,routine=generator(batch)
    while 480 not in score:
        if x<100:
            x=x+1
            score,routine=generator(batch)
        else:
            call()
    if len(score)==1:
        print("this is right routine for 2076",routine,score)
    else:
        print("this is right routine for 2076",routine[0],score)
    



    x=0
    batch=2077
    score,routine=generator(batch)
    while 480 not in score:
        if x<60:
            x=x+1
            score,routine=generator(batch)
            
        else:
            call()
    if len(score)==1:
        print("this is right routine for 2077",routine,score)
    else:
        print("this is right routine for 2077",routine[0],score)



        
    x=0
    batch=2081
    score,routine=generator(batch)
    while 480 not in score:
        if x<120:
            x=x+1
            score,routine=generator(batch)
            
        else:
            call()
    if len(score)==1:
        print("this is right routine for 2081",routine,score)
    else:
        print("this is right routine for 2081",routine[0],score)


    
    x=0
    batch=2080
    score,routine=generator(batch)
    while 480 not in score:
        if x<200:
            x=x+1
            score,routine=generator(batch)
            
        else:
            call()
    if len(score)==1:
        print("this is right routine for 2080",routine,score)
    else:
        print("this is right routine for 2080",routine[0],score)


    batch=2078
    score,routine=generator(batch)
    while 480 not in score:
        if x<200:
            print(x)
            x=x+1
            score,routine=generator(batch)
            
        else:
            call()
    if len(score)==1:
        print("this is right routine for 2078",routine,score)
    else:
        print("this is right routine for 2078",routine[0],score)
    

    

    
    sys.exit()


call()