"""
Intuition
We have to find the nodes which are not reachable. To do that, we can store the nodes in a storage unit then loop over the edges. Whenever we detect an incoming edge for the given node, we remove it because it means the node in consideration is reachable.

Approach
set() variables are handy when it comes to adding and removing the unique elements. Using list() gives time exceeding error.

Time complexity: O(n+e) -> number of edges
Space complexity: O(n)
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        nodes = set(range(n))
        for outgoing,incoming in edges:
            if incoming in nodes: nodes.remove(incoming)

        return nodes