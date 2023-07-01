
class SlidingWindow:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # sliding window
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            curr = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_profit = max(max_profit, curr)
            else:
                l = r
            r += 1

        return max_profit

        # hacky solution
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit