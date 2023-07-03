"""
Intuition
Hi everyone! For this problem, I've again used Brute Force approach and again it exceeded the time limit :D. Then I had to switch my strategy to stacking

Here is my Brute Force Solution:
"""

class StockSpanner:

    def __init__(self):

        
        self.prices = []
        

    def next(self, price: int) -> int:
        if not self.prices: self.prices.append(price); return 1

        if price < self.prices[-1]: self.prices.append(price); return 1

        pointer  = -1
        while pointer > -len(self.prices)-1 and self.prices[pointer] <= price:
            pointer -= 1
            
        self.prices.append(price)

        return abs(pointer)
"""
For each input, we basically search the value obeying the criteria question provides in the global prices list and then we add the current value to the end. The time complexity for this problem is O(n) {from looping} and the space complexity is also O(n) {from self.prices}

The stack solution on the other hand, follows a more complex yet effective logic. The default value of the span is one. We add (current_price,span) in each addition. Also during the addition, we remove all the values smaller than the current value and add the span counts to the tuple of the current value:

(100,1)
(80,1)
(60,1)
|
(70)

vanishes (60,1) then
(100,1)
(80,1)
(70,2)
however it couldn't exceed 80 so we end the spand addition part at this point. Finally we return the span count.

The corresponding code is this:
"""

class StockSpanner:

    def __init__(self):

        
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0]<= price:
            prc,spn = self.stack.pop()
            span+=spn

        self.stack.append((price,span))

        return self.stack[-1][1]
    
"""
The time complexity is O(1) and space complexity is O(n) which is more effective.
"""
