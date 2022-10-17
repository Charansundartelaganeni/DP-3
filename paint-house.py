
#TC: O(n)
#SC: O(1)

class Solution(object):
    def minCost(self, costs):
        for i in range(len(costs)-1, -1, -1):       #we are traversing from the bottom
            costs[i][0] += min(costs[i+1][1], costs[i+1][2])    #For the first house,  minimum between costs[i+1][1], costs[i+1][2] is the best path
            costs[i][1] += min(costs[i+1][0], costs[i+1][2])    #For the second house,  minimum between costs[i+1][0], costs[i+1][2] is the best path
            costs[i][2] += min(costs[i+1][0], costs[i+1][1])    #For the third house, minimum between costs[i+1][0], costs[i+1][1] is the path
    
        return min(costs[0])    #minimum in the first row is going to give us the best path to choose