# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat = []
        self.flatten(nestedList)
        self.nextPtr = 0

    def flatten(self, nestedList):
        for elem in nestedList:
            if elem.isInteger():
                self.flat.append(elem.getInteger())
            else:
                self.flatten(elem.getList())
    
    def next(self) -> int:
        res = self.flat[self.nextPtr]
        self.nextPtr += 1
        return res
    
    def hasNext(self) -> bool:
         return self.nextPtr < len(self.flat)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())