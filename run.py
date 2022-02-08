from generator import generator
def call():
    score=[]
    routine=[]
    batch=2075
    routine_2075=[]
    score,routine=generator(batch)
    x=0
    while 480 not in score :
        if x<25:
            x=x+1
            score,routine=generator(batch)
        else:
            call()
    print("this is right routine for 2075",routine[0])

    x=0
    batch=2076
    score,routine=generator(batch)
    while 480 not in score :
        if x<25:
            x=x+1
            score,routine=generator(batch)
        else:
            call()
    print("this is right routine for 2076",routine[0],score)


    x=0
    batch=2074
    score,routine=generator(batch)
    while 480 not in score:
        if x<25:
            x=x+1
            score,routine=generator(batch)
        else:
            call()
    print("this is right routine for 2074",routine[0])




    x=0
    batch=2077
    score,routine=generator(batch)
    while 480 not in score:
        if x<25:
            x=x+1
            score,routine=generator(batch)
            
        else:
            call()
    print("this is right routine for 2077",routine[0])
    exit


call()