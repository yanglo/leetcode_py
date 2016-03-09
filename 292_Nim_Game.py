#coding=utf-8
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = (n % 4 != 0)
        return  res


if __name__ == '__main__':
    test = Solution()
    # print test.canWinNim(4)
    # print test.canWinNim(3)
    print test.canWinNim(11)
    print test.canWinNim(157343)