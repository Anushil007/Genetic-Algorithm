def sandeep(lst):
    lst2=lst.copy()
    lst2.pop(0)
    return lst2

lst=[1,2,3,4]
while len(lst)!=0:
    lst2=sandeep(lst)
    lst=lst2
    print(lst)
