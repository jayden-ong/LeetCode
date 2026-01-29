class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Get closest multiple of 10
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount 
        
        smaller_multiple = (purchaseAmount // 10) * 10
        larger_multiple = ((purchaseAmount // 10) + 1) * 10
        if abs(smaller_multiple - purchaseAmount) < abs(larger_multiple - purchaseAmount):
            return 100 - smaller_multiple
        
        return 100 - larger_multiple
