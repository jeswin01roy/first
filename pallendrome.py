import sys
print("\t\tPallendrome or not")
num=int(input("enter the number you want to test:"))
temp=num    
rev=0
while(temp>0):
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if(num==rev):
    print("the number is pallendrome")
else:
    print("the number is not pallendrome")