# Bad implementation, time complexity is O(m+n) rather than O(log(m+n))
import statistics as stat


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        j = 0
        k = 0
        array = []
        for i in range(len(nums1) + len(nums2)):
            if j == len(nums1):
                array.append(nums2[k])
                k = k + 1
                continue
            if k == len(nums2):
                array.append(nums1[j])
                j = j + 1
                continue
            if nums1[j] < nums2[k]:
                array.append(nums1[j])
                j = j+1
            else:
                array.append(nums2[k])
                k = k+1
        return stat.median(array)


s = Solution()
print(s.findMedianSortedArrays([3, 4], []))
