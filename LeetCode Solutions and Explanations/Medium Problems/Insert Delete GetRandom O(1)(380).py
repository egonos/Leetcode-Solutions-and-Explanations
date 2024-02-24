# My first solution (not working due to not providing complete randomness) :

class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.randomizedSet:
            self.randomizedSet.add(val)
            return True

        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            return True

        else:
            return False

    def getRandom(self) -> int:
        if self.randomizedSet:
            randomNumber = self.randomizedSet.pop()
            self.randomizedSet.add(randomNumber)
            return randomNumber

# My solution after understanding the logic:

class RandomizedSet:

    def __init__(self):
        self.randomList = []
        self.indexDict = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.indexDict:
            self.indexDict[val] = len(self.randomList)
            self.randomList.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.indexDict:
            lastValue = self.randomList[-1]
            self.randomList[self.indexDict[val]],self.randomList[-1] = self.randomList[-1], self.randomList[self.indexDict[val]] #replacement
            self.randomList.pop()
            self.indexDict[lastValue] = self.indexDict[val]
            self.indexDict.pop(val)
            return True

        else:
            return False

    def getRandom(self) -> int:
        if self.randomList:
            randomNumber = random.choice(self.randomList)
          
            return randomNumber

        else:
            return None
        