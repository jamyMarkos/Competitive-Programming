class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(idx, txn_status):

            if idx > len(prices)-1:
                return 0

            if (idx, txn_status) in memo:
                return memo[(idx, txn_status)]
            
            if txn_status:
                bought = dp(idx+1, False) - prices[idx]
                waited = dp(idx+1, True) 
                memo[(idx, txn_status)] = max(bought, waited)
            else:
                sell_it = dp(idx+1, True) + prices[idx] - fee
                waited = dp(idx+1, False)
                memo[(idx, txn_status)] = max(sell_it, waited)

            return memo[(idx, txn_status)]

        return dp(0, True)