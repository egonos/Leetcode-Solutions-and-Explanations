"""
Intuition
Generating a dictionary for the paranthesis is valuable because it allows us to check the order efficiently.

Approach
First we append the open paranthesis. During this process if we encounter a closing paaranthesis we need to make sure that paranthesis in consideration is the complementary of the last paranthesis. If it is then we remove that paranthesis from our list. Otherwise we immediately return False.

Complexity
Time complexity: O(n)

Space complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        control_dict = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        control = list()
    
   

        
        for b in s:
            if b in control_dict:
                control.append(b)

            else:
                if control and b == control_dict[control[-1]]:
                    control.pop()
                  

                else: 
                    return False

        
        return len(control) == 0
        