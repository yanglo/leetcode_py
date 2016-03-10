#coding=utf-8
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        arr_len = len(x)

        for index in range(3, arr_len):
            if index >= 3 and x[index] >= x[index-2] and x[index-1]<=x[index-3]:
                return True
            if index >= 4 and x[index-1]==x[index-3] and x[index-2] <= (x[index] + x[index-4]):
                return True
            if index >= 5 and x[index-2] > x[index-4] and x[index-1]<=x[index-3] and x[index-1]+x[index-5]>=x[index-3] and x[index]+x[index-4]>=x[index-2]:
                return True

        return False

if __name__ == '__main__':
    test = Solution()
    # print test.isSelfCrossing([1, 2, 3, 4])
    # print test.isSelfCrossing([4, 3, 2, 1])
    print test.isSelfCrossing([3,3,4,2,2])