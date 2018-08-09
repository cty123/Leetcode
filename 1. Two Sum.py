class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i_index, i_val in enumerate(nums):
            for j_index, j_val in enumerate(nums):
                if i_index != j_index:
                    if i_val + j_val == target:
                        return i_index, j_index


s = Solution()
i, j = s.twoSum([3, 2, 4], 6)
print('[%d,%d]' % (i, j))