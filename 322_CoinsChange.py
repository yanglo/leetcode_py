#coding=utf-8
import sys

class Solution(object):
    res_map = {}
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.res_map = {}
        coins.sort()
        return self.sub_func(coins, amount)

    def sub_func(self, coins, amount):
        arrlen = len(coins)
        min_value = coins[0]

        if self.res_map.get(amount):
            return self.res_map.get(amount)

        if amount == 0:
            return 0

        if amount < min_value:
            return -1
        min_len = sys.maxint
        for i in range(0, arrlen):
            len_num = self.sub_func(coins, amount-coins[i])
            if min_len > len_num and len_num != -1:
                min_len = len_num

        if min_len == sys.maxint:
            self.res_map[amount] = -1
            return -1
        else:
            self.res_map[amount] = min_len + 1
            return min_len + 1

if __name__ == '__main__':
    test = Solution()
    # print test.coinChange([3], 9)
    # print test.coinChange([1, 2, 4, 5], 9)
    # print test.coinChange([186,419,83,408], 6249)
    print test.coinChange([55,319,101,494,162,58,295,253], 5780)
    print test.coinChange([46,295,485,415,449,379,183,323], 5897)
