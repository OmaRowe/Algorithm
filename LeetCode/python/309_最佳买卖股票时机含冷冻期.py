class Solution:
    """
    动态规划：一共三种状态
    1、当前持有一直股票 ， 有股票且没有卖
    2、当前不持有股票且处在冷冻期
    3、当前不持有股票且不处在冷冻期，即没有股票或者有股票卖了
    """
    def maxProfit(self, prices):

        n = len(prices)

        if n == 0:
            return 0

        f = [[0] * 3 for i in range(n)]
        f[0][0] = -prices[0]

        for i in range(1, n):
            # 关键点i表示今天结束的状态，也就是买入卖出操作执行结束
            # 前一天有股票, 今天不属于冷冻期
            # 当前最大收益的状态时卖出或者保持不变
            f[i][0] = max(f[i-1][0], f[i-1][2] - prices[i])
            # 当前一天不持有股票且处在冷冻期
            f[i][1] = f[i-1][0] + prices[i]
            # 注意冷冻期是指
            # 当前不持有股票且不再冷冻期，有以下几种情况
            # 前一天有股票，且没有卖
            # 股票已经卖完了
            f[i][2] = max(f[i-1][1], f[i-1][2])

        return max(f[n-1][1], f[n-1][2])
