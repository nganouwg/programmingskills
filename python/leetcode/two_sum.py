'''

Tag: Easy Array / Hash table

Ultimate Goal: Can you come up with an algorithm that is less than O(n2) time complexity?

-------------------------------------------------------------------------------------------

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

'''



def run(nums, target):

    '''
    for i, n in enumerate(nums):
        print(f"Index: {i}, Value: {n}")
        pass
    '''

    i = 0
    j = 0
    found = False
    arrlen = len(nums)

    while(i < arrlen):
        j = i+1
        while(j < arrlen):
            twosum = nums[i] + nums[j]
            if twosum == target:
                found = True
                break
            j += 1
        if found:
            break
        i += 1

    if found:
        two_sum = [i, j]
        print(two_sum)
    else:
        print("Two sum not found")
