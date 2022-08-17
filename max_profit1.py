class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        P, P_pay = 0, - prices[0]
        for i in range(1, len(prices)):
            P, P_pay = max(P, prices[i] + P_pay - fee), max(P_pay, P - prices[i])
        return P