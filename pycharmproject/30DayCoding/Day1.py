# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

def running_sum(l1):
    c1=len(l1)
    l2=[]
    print(c1)
    #print(l1[1])
    total = 0
    for i in range(len(l1)):
        total += l1[i]
        l2.append(total)

    print(l2)


l1=[1,2,3,4]
l12=[1,1,1,1,1]
l13=[3,1,2,10,1]

running_sum(l12)