"""
Intuition
Hi everyone! This problem was hard to understand but fairly easy to code it. To be honest, after looking the graphs in here, I was able to understand it. All we have to do is creating a queue for each party and compare them like explained in question. senator is at a smaller position gets to ban the other senator, and the senator who gets to ban is added back to the queue with their position updated to be at the end of the round. The smaller indexed senate after the operation is added to the end of the queue (of course its index is incread by the number of senates). Repeat this process until one of the queue's are empty and return the other one.

We have 2 loops so our time complexity would be O(n) and due to queue's we have space complexity of O(n) also.
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rq = deque([])
        dq = deque([])
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R': rq.append(i)
            else: dq.append(i)


        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            if r>d: dq.append(r + n)
            else: rq.append(d + n)

        if not rq: return "Dire"
        else: return "Radiant"