def average(x,y,z):
    print(f"Average of 3 numbers is: {(x+y+z)/3}")

average(10,20,30)

def perfect(x):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    if sum==x:
        print(f"{x}:perfect number")
    else:
        print(f"{x}:not perfect")

perfect(10)