'''def search(a,b):
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
            break'''

'''nums =[9,0,1,8,0,0,5,6]
def remove_zero();
    expt_value = []
    zeros = []
   for vals in nums:
       if (vals != 0):
           expt_value.append(vals)
        else:
            zeros.append(vals)
    expt_value.extend(zeros)
emove_zero'''


nums1 = [1,3,5,99]
nums2 = [2,4,66]

total_values = []
def assending(nums1,nums2):
    for i in range(len(nums1)):
        if(len(nums1)-1 != i):
            if (nums1[i] < nums2[i]):
                total_values.append(nums1[i])
                total_values.append(nums2[i])
        else:
            total_values.append(nums1[i])

    print (total_values)
                
assending(nums1,nums2)

               
           
           


