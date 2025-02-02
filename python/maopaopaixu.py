from random import randint
number = []
for counter in range(1,20):
    number.append(randint(0,100)) 
for counter in range(1,len(number)):
    i = 0
    number1 = 0
    while True:
        if number[i]>number[i+1]:
            number1=number[i]
            number[i]=number[i+1]
            number[i+1]=number1
        i = i+1
        if i+1==len(number):
            break
print(number)            

