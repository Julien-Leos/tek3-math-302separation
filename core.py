import sys
import numpy as np
import copy

class Core:
    friendLinks = []
    matrixDeep = 0
    friend1 = ""
    friend2 = ""

    friends = []
    adjacencyMatrix = []
    adjacencyMatrixShortest = []

    def __init__(self, parsedArgs):
        self.friendLinks = parsedArgs[0]
        if len(parsedArgs) == 2:
            self.matrixDeep = int(parsedArgs[1])
        else:
            self.friend1 = parsedArgs[1]
            self.friend2 = parsedArgs[2]

        self.getUniqueFriends()

    def matrixAlgorithm(self):
        self.createAdjacencyMatrix()
        self.createAdjacencyMatrixShortest()

    def linkAlgorithm(self):
        if self.friend1 == self.friend2:
                print("Degree of separation between " + self.friend1 + " and " + self.friend2 + ": 0")
        try:
            indexFriend1 = self.friends.index(self.friend1)
            indexFriend2 = self.friends.index(self.friend2)
        except ValueError:
            print("Degree of separation between " + self.friend1 + " and " + self.friend2 + ": -1")
            return

        self.createAdjacencyMatrix()
        for i in range(1, 8):
            self.matrixDeep = i
            self.createAdjacencyMatrixShortest()
            if self.adjacencyMatrixShortest[indexFriend1][indexFriend2] != 0:
                print("Degree of separation between " + self.friend1 + " and " + self.friend2 + ": " + str(self.adjacencyMatrixShortest[indexFriend1][indexFriend2]))
                return
        return

    def getUniqueFriends(self):
        tmp = []
        for i in self.friendLinks:
            tmp.append(i[0])
            tmp.append(i[1])

        self.friends = list(dict.fromkeys(tmp))
        self.friends.sort()

    def createAdjacencyMatrix(self):
        for friend in self.friends:
            friendsOfFriend = [0] * len(self.friends)
            for link in self.friendLinks:
                if link[0] == friend:
                    friendsOfFriend[self.friends.index(link[1])] = 1
                if link[1] == friend:
                    friendsOfFriend[self.friends.index(link[0])] = 1
            self.adjacencyMatrix.append(friendsOfFriend)

    def findLinksBetweenFriends(self, meIndex, friendLinkIndex, actualDeep):
        friendIndexesToCheck = []
        if actualDeep > self.matrixDeep:
            return (0)
        friend = self.adjacencyMatrix[friendLinkIndex]
        for (friendOfFriendLinkIndex, friendOfFriendLink) in enumerate(friend):
            if friendOfFriendLink == 1:
                friendOfFriend = self.adjacencyMatrix[friendOfFriendLinkIndex]
                if friendOfFriend[meIndex] == 1:
                    return (actualDeep)
                friendIndexesToCheck.append(friendOfFriendLinkIndex)
        for friendIndexToCheck in friendIndexesToCheck:
            result = self.findLinksBetweenFriends(meIndex, friendIndexToCheck, actualDeep + 1)
            if result != 0:
                return (result)
        return (0)

    def createAdjacencyMatrixShortest(self):
        self.adjacencyMatrixShortest = copy.deepcopy(self.adjacencyMatrix)
        for (meIndex, me) in enumerate(self.adjacencyMatrixShortest):
            for (friendLinkIndex, friendLink) in enumerate(me):
                if friendLink == 0 and meIndex != friendLinkIndex:
                    me[friendLinkIndex] = self.findLinksBetweenFriends(meIndex, friendLinkIndex, 2)

    def displayMatrixAlgorithm(self):
        for friend in self.friends:
            print(friend)
        print('')
        self.displayArray(self.adjacencyMatrix)
        print('')
        self.displayArray(self.adjacencyMatrixShortest)

    def displayLinkAlgorithm(self):
        
        pass

    def displayArray(self, array):
        for row in array:
            for (index, i) in enumerate(row):
                print(str(i) + (' ' if index != len(row) - 1 else ''), end='')
            print('')