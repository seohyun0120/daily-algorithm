class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        
        for price in prices:
            min_price = min(min_price, price)
            answer = max(answer, price - min_price)

        return answer            