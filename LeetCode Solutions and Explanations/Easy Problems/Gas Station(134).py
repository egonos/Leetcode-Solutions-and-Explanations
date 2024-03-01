#Brute Force Solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            current = i
            tank = 0
            count = 0
            while tank >=0:
                
                tank += (gas[i] - cost[i])

                if i == len(gas) - 1:
                    i = 0

                else:
                    i+=1

                count+=1

                if count == len(gas):
                    return i
            
            i = current

        return -1

# Efficient Solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) - sum(cost) < 0: return -1

        tank = 0
        start_idx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start_idx = i+1

        return start_idx