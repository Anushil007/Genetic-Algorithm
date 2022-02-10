import random
import itertools

# to change nested list into a one dimensional list

def oneDArray(x):
    return list(itertools.chain(*x))


children = []
overal_routine = [0 for i in range(6)]



def PopulationGeneration(mylist1, mylist2, mylist3):     #this loop is for the generation of population
    routine = []
    lst = []
    lst_1D = []
    
    lab_len=mylist2[0]
    lab_len=(len(lab_len))
    sec_period_choice = [1, 2]
    random.shuffle(mylist1)
    random.shuffle(mylist2)
    random.shuffle(mylist3)
    
    for u in range(6):   # this loop is for generation of chromosome
    #if len(mylist1) != 0 and len(mylist2) != 0:
        lab = 0
        length = 0
        e = random.choice(sec_period_choice)
        lunch = random.choice([4,5])

        if e == 1:
            if len(mylist1) != 0:
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
            elif len(mylist2) != 0:
                x = (random.choice(mylist2))
                index = mylist2.index(x)
                mylist2.pop(index)
                lab = 1
                lst.append(x)   
            elif len(mylist3) != 0:
                x = (random.choice(mylist3))
                index = mylist3.index(x)
                mylist3.pop(index)
                lst.append(x) 
            else:
                pass
        elif e == 2:
            if len(mylist2) != 0:
                x = (random.choice(mylist2))
                index = mylist2.index(x)
                mylist2.pop(index)
                lab = 1
                lst.append(x)
            elif len(mylist1) != 0:
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
            elif len(mylist3) != 0:
                x = (random.choice(mylist3))
                index = mylist3.index(x)
                mylist3.pop(index)
                lst.append(x) 
            else:
                pass
        #print(lst)
        count = 0
        lst_1D = oneDArray(lst)
        length = len(lst_1D)
        #print(length)
        if length == 2:
            if len(mylist1) != 0:
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x)
            elif len(mylist3) != 0:
                x = (random.choice(mylist3))
                index = mylist3.index(x)
                mylist3.pop(index)
                lst.append(x) 
            else:
                pass
        elif length == 3:
            pass

        lst.append([100])
        lst_1D = oneDArray(lst)
        length=len(lst_1D)
        if length==5 and lab_len==3:
            if len(mylist2) != 0:
                x = (random.choice(mylist2))
                index = mylist2.index(x)
                mylist2.pop(index)
                lst.append(x)
                lab=1
        lst_1D = oneDArray(lst)
        length=len(lst_1D)

        #print(len(lst))
        


        if (length!=8):
            if len(mylist2) != 0 and lab==0:
                x = (random.choice(mylist2))
                index = mylist2.index(x)
                mylist2.pop(index)
                lab = 1
                lst.append(x) 
            
            elif len(mylist1) != 0:
                x = (random.choice(mylist1))
                index = mylist1.index(x)
                mylist1.pop(index)
                lst.append(x) 
            elif len(mylist3) != 0:
                x = (random.choice(mylist3))
                index = mylist3.index(x)
                mylist3.pop(index)
                lst.append(x) 
            else:
                pass
            # elif e == 2:
            #     if len(mylist2) != 0 and lab==0 :
            #         x = (random.choice(mylist2))
            #         index = mylist2.index(x)
            #         mylist2.pop(index)
            #         lab = 1
            #         lst.append(x)
            #     elif len(mylist1) != 0:
            #         x = (random.choice(mylist1))
            #         index = mylist1.index(x)
            #         mylist1.pop(index)
            #         lst.append(x)
            #     elif len(mylist3) != 0:
            #         x = (random.choice(mylist3))
            #         index = mylist3.index(x)
            #         mylist3.pop(index)
            #         lst.append(x) 
            #     else:
            #         pass

            #print(lst)
            lst_1D = oneDArray(lst)
            length = len(lst_1D)
            #print(length)
            if length == 7:
                if len(mylist3) != 0:
                    x = (random.choice(mylist3))
                    index = mylist3.index(x)
                    mylist3.pop(index)
                    lst.append(x) 
            elif length == 6:
                if len(mylist2) != 0 and lab==0:
                    x = (random.choice(mylist2))
                    index = mylist2.index(x)
                    mylist2.pop(index)
                    lst.append(x) 
                    #print(length)
                elif len(mylist1) != 0:
                    x = (random.choice(mylist1))
                    index = mylist1.index(x)
                    mylist1.pop(index)
                    lst.append(x) 
                elif len(mylist2) != 0:
                    x = (random.choice(mylist2))
                    index = mylist2.index(x)
                    mylist2.pop(index)
                    lst.append(x) 
                    #print(length)
                # else:
                #     pass
            lst_1D = oneDArray(lst)
            length=len(lst_1D)
            if length!=8:
                if len(mylist3) != 0:
                    x = (random.choice(mylist3))
                    index = mylist3.index(x)
                    mylist3.pop(index)
                    lst.append(x) 
                if len(mylist3) != 0:
                    x = (random.choice(mylist3))
                    index = mylist3.index(x)
                    mylist3.pop(index)
                    lst.append(x) 
                if len(mylist3) != 0:
                    x = (random.choice(mylist3))
                    index = mylist3.index(x)
                    mylist3.pop(index)
                    lst.append(x)
            
        lst_initial=lst[:]
        random.shuffle(lst)
        random.shuffle(lst)
        lst_check=oneDArray(lst)
        for i in range(10):
            if (lst_check[3]==100 or lst_check[4]==100):
                routine.append(lst)
                x=100
                break
            else:
                random.shuffle(lst)
                lst_check=oneDArray(lst) 
        if x!=100:
            routine.append(lst_initial)
                    
                    


        #print((lst))
        # routine.append(lst)
        lst = []
    return routine
