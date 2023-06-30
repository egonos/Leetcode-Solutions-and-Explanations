A Solution with Explanation
egemenugur
1
1
Jun 23, 2023
Python3
Array
Greedy
Intuition
Hi everyone! For this problem, the following algoritm works:

Assign 1 candy for each child.
Do a forward pass. Increase the candy count of a child at index i if his/her ranking is greater than the child located at index i-1.
Do a backward pass. Increase the candy count of a child at index i if his/her ranking is greater than the child located at index i+1.
Here is the tricky part. Since we start with a list of ones, we don't have to define more conditions to the algorithm:

for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        candies[i] = candies[i-1] + 1
However in the back pass, since the list is not that simple anymore we have to define a new condition which is:

and candies[i]<=candies[i+1]
What happens when we don't do that? I've tried it. Let's look at one of the test cases:

ratings = [1,3,4,5,2]

candies = [1,1,1,1,1]

After forward loop:

candies = [1,2,3,4,1]

Backward loop without addition:

candies = [1,2,3,2,1]

Since 5 is greater than 2 we update the candy at index 3 from 4 to 2 which violates the question statement.

The time complexity is O(n) {from looping} and the space complexity is also O(n) {because of the candies array}

I hope this explanation is helpful.

class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        candies = [1]*n

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1] and candies[i]<=candies[i+1]:
                candies[i] = candies[i+1] +1


        return sum(candies)