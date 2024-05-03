worker1 = []
worker2 = []
worker3 = []
x1 = worker1.append(input("Enter the name of the first worker:"))
for i in range(3):
     worker1.append(int(input("Enter three salaries:")))
x2 = worker2.append(input("Enter the name of the second worker:"))
for i in range(3):
    worker2.append(int(input("Enter three salaries:")))
x3 = worker3.append(input("Enter the name of the third worker:"))
for i in range(3):
   worker3.append(int(input("Enter three salaries:")))

worker1.pop(0)
worker2.pop(0)
worker3.pop(0)



worker1_x = worker1.sort()
worker2_x = worker2.sort()
worker3_x = worker3.sort()

print(worker1_x )
print(worker2_x )
print(worker3_x )






#def average(worker1):
 #  return "the average of worker1: ", sum(worker1)/len(worker1)
#def average2(worker2):
 #  return "the average of worker1: ", sum(worker2) / len(worker2)
#def average3(worker3):
   #return "the average of worker1: ", sum(worker3) / len(worker3)

#worker1.append(x1)
#worker2.append(x2)
#worker3.append(x3)


#average(worker1)
#average(worker2)
#average(worker3)


