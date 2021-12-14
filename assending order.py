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
