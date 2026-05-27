class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cur_profit = 0

        buy = prices[0]

        for p in prices:
            if buy > p:
                buy = p
            
            cur_profit = max(cur_profit, p - buy)
        
        return cur_profit
        