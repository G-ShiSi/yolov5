import random
list=[]
n=4
while True:
    num=random.randint(1, 32)
    if num!=6 and num!=16 and num!=18 and num!=30 and num!=2 and num!=19and num!=21 and num not in list:
        list.append(num)
        n-=1
    if n==0:
        break
print(list)