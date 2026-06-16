print (" \t\t prime or not ")
num=int(input("enter the number you want to test:"))
ctr=0
for i in range(1,(num+1)):
    if(num % i == 0):
        ctr=ctr+1

if(ctr>2):
    print("the number is not prime")
else:
    print("the number is prime")
