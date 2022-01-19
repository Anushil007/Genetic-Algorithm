
import random
def generateinitialpop():
    routine = []
    lst = []
    mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],
                [25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
    mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
    mylist3 = [[5], [22], [33]]  #

    sec_period_choice = [0, 1]
    random.shuffle(mylist1)
    random.shuffle(mylist2)
    random.shuffle(mylist3)

    for u in range(6):
        x = (random.choice(mylist1))
        lst.append(x)
        # routine.append(x)
        index = mylist1.index(x)
        mylist1.pop(index)

        e = random.choice(sec_period_choice)  # Second Period Choice
        if e == 0:
            x = (random.choice(mylist1))
            lst.append(x)
            # routine.append(x)
            index = mylist1.index(x)
            mylist1.pop(index)
        else:
            x = random.choice(mylist3)
            lst.append(x)
            routine.append(x)
            index = mylist3.index(x)
            mylist3.pop(index)

        lst.append([44])
        # routine.append([44])

        count = 0
        for q in lst:
            if len(q) == 2:
                count += 2
            else:
                count += 1

        #   print(count)

        if count == 5:
            if len(mylist2) != 0:
                x = (random.choice(mylist2))
                lst.append(x)
                # routine.append(x)
                index = mylist2.index(x)
                mylist2.pop(index)
            else:
                x = (random.choice(mylist1))
                lst.append(x)
                # routine.append(x)
                index = mylist1.index(x)
                mylist1.pop(index)
                x = (random.choice(mylist3))
                lst.append(x)
                #  routine.append(x)
                index = mylist3.index(x)
                mylist3.pop(index)
        elif count == 4:
            for i in range(2):
                x = (random.choice(mylist1))
                lst.append(x)
                # routine.append(x)
                index = mylist1.index(x)
                mylist1.pop(index)
            else:
                pass
        routine.append(lst)
        # print(lst)
        lst = []
    return routine