"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


Hi everyone! For this problem, I needed some time to understand the logic behind the solution so I'll do my best to explain it.

We are trying to find the starting position -if any- which gives us a chance to visit all the other stations. For the placeholder we will use starting_position. It's initial value is 0 meaning we will try each station one by one.

To see the possibility for traveling through all the stations, we will define a base condition:

if sum(gas) - sum(cost) < 0: return -1.
Now, after make sure that a solution exists, we will loop through the arrays.temp_gas is the gas balance when we start at station i. When it falls below zero it means we have no gas left so we can't traverse all the stations. Here is the fancy part:

if temp_gas < 0:
        temp_gas = 0
        starting_position = i + 1
This part confused me a lot. The first thing came to my mind is how it is possible to increasing starting index by negative number counts allows us to find the solution? Well, from my understanding, we are already sure that a solution exists and when we start at previous indicies we can not maintain a positive balance. When we find an index which keeps the balance positive till the end should be the solution. I hope this explanation is clear for you...

Time complexity: O(n) {looping}
Space complexity: O(1) {the placeholder}
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) - sum(cost) < 0: return -1

        temp_gas = 0
        starting_position = 0
        for i in range(len(gas)):
            temp_gas += gas[i] - cost[i]
            if temp_gas < 0:
                temp_gas = 0
                starting_position = i + 1

        return starting_position