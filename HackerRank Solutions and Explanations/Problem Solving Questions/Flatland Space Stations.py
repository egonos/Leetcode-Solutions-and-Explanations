"""
Explanation

This question requires a different approach. For example, the first two solutions I provide `flatlandSpaceStations` and `flatlandSpaceStations2` are not efficient enough and both of them fail at Test Case 15 due to time limit constraints. The last solution is not fully mine but I'll do my best to explain it.

* First we sort c because it improves the lookup efficiency.
* The initial value of `max_distance` is max(0, the location of the first space station (*it refers to the distance between first city and first space station*) and last city's distance to the last space station)
* Loop over space stations and update the maximum distance based on the value `(c[i+1] - c[i]) // 2)` since the distance to a space station of a given city is lower for either c[i+1] or c[i].

"""

def flatlandSpaceStations(n, c):
    pointer = 0
    distances = []
    for i in range(n):
        if i == c[pointer]:
            distances.append(0)
            if pointer == len(c)-1: pass
            else: pointer += 1
            
        else:
            distances.append(min([abs(j-i) for j in c]))
            
    return max(distances)



def flatlandSpaceStations2(n, c):
    c.sort()
    candidates = list(range(n))
    for i in c:
        candidates.remove(i)
    distances = []
    for i in candidates:
        distances.append(min([abs(i-j) for j in c]))
    return max(distances)



def flatlandSpaceStations3(n, c):
    c.sort()
    max_distance = max(c[0], n-1-c[-1])
    for i in range(len(c)-1):   
        max_distance = max(max_distance, (c[i+1]-c[i])//2)
    return max_distance