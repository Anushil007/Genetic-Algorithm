# initial population
import numpy
import gen_pop
routine=[]
for i in range(6):   
      routine=gen_pop.generateinitialpop()
      print("This is population ",i, "\n",routine)