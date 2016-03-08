#coding=utf-8
import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        if size < 3:
            return False
        first = sys.maxint
        second = sys.maxint
        for i in range(0, len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False



if __name__ == '__main__':
    test = Solution()
    print test.increasingTriplet([1, 2, 3, 4])
    print test.increasingTriplet([4, 3, 2, 1])
    print test.increasingTriplet([2,1,5,0,3])