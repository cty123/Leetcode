class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums
            
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = len(nums) - 1
                while j >= 0 and nums[j] <= nums[i-1]:
                    j -= 1
                temp = nums[i-1]
                nums[i - 1] = nums[j]
                nums[j] = temp
                start = i
                end = len(nums) - 1
                while start < end:
                    t = nums[start]  
                    nums[start] = nums[end]
                    nums[end] = t
                    start += 1
                    end -= 1
                return
            
        start = 0
        end = len(nums) - 1
        while start < end:
            t = nums[start]  
            nums[start] = nums[end]
            nums[end] = t
            start += 1
            end -= 1
        return