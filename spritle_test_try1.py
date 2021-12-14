nums = [1,2,3]
def target_indices(nums,target):
    try:
        target = int(target)
        if (int(sum(nums)) > int(target) or sum(nums)==target):
            for vals in nums:
                if (vals < target):
                    for vals1 in nums:
                        if(nums.index(vals) == nums.index(vals1)):
                            continue
                        else:
                            sum1 = vals+vals1
                            if (sum1 == target):
                                print ([nums.index(vals),nums.index(vals1)])
                else:
                    continue
        else:
            print ("sorry.target value exceeds the sum of nums")
            return target_indices(nums,input("enter the target = "))
    except:
        print ("oops.you entered a non integer value. \n please try again ")
        return target_indices(nums,input("enter the target = "))
target_indices(nums,input("enter the target = "))






    
