import sys

class Solution:
    def threeSumClosest(self, nums, target) -> int:
        n = len(nums)
        arr = sorted(nums)
        min_df = sys.maxsize
        three_sum = 0

        for i in range(n-2):
            if arr[i] + arr[i+1] + arr[i+2] > target:
                if abs(arr[i] + arr[i+1] + arr[i+2] - target) < min_df:
                    return arr[i] + arr[i+1] + arr[i+2]
                else:
                    return three_sum
                
            if arr[i] + arr[n-1] + arr[n-2] < target:
                if abs(arr[i] + arr[n-1] + arr[n-2] - target) < min_df:
                    three_sum = arr[i] + arr[n-1] + arr[n-2] 
                    min_df = abs(three_sum - target)
                continue

            l, r = i+1, n-1

            while l < r:
                if arr[i] + arr[l] + arr[r] == target:
                    return arr[i] + arr[l] + arr[r]
                elif arr[i] + arr[l] + arr[r] > target:
                    if abs(arr[i] + arr[l] + arr[r] - target) < min_df:
                        three_sum = arr[i] + arr[l] + arr[r]
                        min_df = abs(three_sum - target)
                    r -= 1
                else:
                    if abs(arr[i] + arr[l] + arr[r] - target) < min_df:
                        three_sum = arr[i] + arr[l] + arr[r]
                        min_df = abs(three_sum - target)
                    l += 1

        return three_sum   

s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
