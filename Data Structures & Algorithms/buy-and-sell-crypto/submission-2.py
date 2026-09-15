class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_profit = 0 

        for price in prices: 
            if price < lowest_price: 
                lowest_price = price 
            if best_profit < price-lowest_price: 
                best_profit = price-lowest_price 

        return best_profit 
        