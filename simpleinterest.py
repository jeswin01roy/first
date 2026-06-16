print("\t\tcalculating simple interest")
p=int(input("enter the principle amount:"))
i=float(input("enter the rate of interest in year:"))
t=int(input("enter the time period in years:"))
amt=(p*i*t)/100
print("the amount of interst recieve in a year:",amt)
print("the amount of interst recieve in a month:",(amt/(12*t)))
