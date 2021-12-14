def search(a,b):
    for d in b:
        if a==d:
            m=True
            break
        else:
            m=False
    return m

nums=[1,4,5,7,9,6,2]
target=int(input("Enter the number:"))
for i in nums:
    if i<target:
        pair=int(target)-int(i)
        in2=search(pair,nums)
        if in2==True:
            print ([nums.index(i),nums.index(pair)])
            print ("the first number= %d the second number %d"%(i,pair))
            break
