#217. Contains Duplicate

#Easy

# Given an integer array nums, 
# return true if any value appears more than once in the array, 
# otherwise return false.

#Example 1:
#Input: nums = [1, 2, 3, 3]
#Output: true

#Example 2:
#Input: nums = [1, 2, 3, 4]
#Output: false

#Solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))  
    
#if length of set is less than length of list, it means there are duplicates in the list

#Solution 2
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
#if any element is already in the set, it means there are duplicates in the list