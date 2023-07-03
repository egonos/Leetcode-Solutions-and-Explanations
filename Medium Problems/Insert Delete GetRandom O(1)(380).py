"""
Intuition
Hi everybody! The biggest challenge for this problem is to stay at O(1) complexity. It is hard to do when working with list objects because in general, any operation involving search through the list results in ~O(n) complexity. Therefore I've decided to use aset object. Since sets only store the unique values, all we have to do is checking the length before and after the insterting operation and return whether they are equal or not. Since we don't want them to be equal I defined

return before != after
Removing operation is fairly simple because it also requires O(1) complexity. However, when the intended value is not in the set Key Error raises. To handle that I've used an try-except pair. Instead of raising error the algoritm immediately returns False. Otherwise it removes the element from the list then returns True

Picking a random element is a bit trickier. First I've used this:
"""
def getRandom(self) -> int:
    return random.choice(list(self.s))

"""
Unfortunetely random.choice does not work for sets and set -> list conversion takes O(n) time complexity. Therefore, I used pop(). This method can be used to pick and remove a random element from a set [1]. Since we don't want to remove the variable, before the end I added the popped value back to the set. I hope my explanation was clear and you will find helpful.
"""

class RandomizedSet:

    def __init__(self):

        self.s = set()
        

    def insert(self, val: int) -> bool:
        before = len(self.s)
        self.s.add(val)
        after = len(self.s)
        return before != after

    def remove(self, val: int) -> bool:
        try:

            self.s.remove(val)
            return True

        except: 
            return False
        

    def getRandom(self) -> int:
        try:

            ret = self.s.pop()
            self.s.add(ret)
            return random.choice(list(self.s))

        except: 
            return 