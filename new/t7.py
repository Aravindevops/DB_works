def list(l):
    even=0
    odd=0
    fifty=0
    for i in l:
        if i%2==0:
            even+=1
        else:
            odd+=1
    
        if i>50:
            fifty+=1
    print(f"even:{even},odd:{odd},fifty:{fifty}")


l=[23,56,12,78,98,89,31,67]
list(l)