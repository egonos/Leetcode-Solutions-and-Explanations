#1st Algorithm

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #Initialize a dict
        people_dict = {}
        for i in range(1,n+1):
            people_dict[i] = set()

        #Fill the dict
        for peoples in trust:
            people_dict[peoples[1]].add(peoples[0])

        #Combine the values in a single set
        trusting_people = set()
        for _,j in people_dict.items():
            trusting_people = trusting_people.union(j)

        #Iterate over the dictionary and check the necessary conditions simultaneously
        for i,j in people_dict.items():
            if len(j) == n-1 and i not in trusting_people:
                return i

        return -1
    

#2nd Algorithm
    
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        people_dict = {i: 0 for i in range(1,n+1)} 
        for people in trust:
            people_dict[people[1]] +=1
            people_dict[people[0]] -= 1

        for i,j in people_dict.items():
            if j == n-1:
                return i

        return -1
