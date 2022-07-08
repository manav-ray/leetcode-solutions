class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        
        for word in strs:
            sortWord = ''.join(sorted(word))
            if sortWord in anaDict:
                anaDict[sortWord].append(word)
            else:
                anaDict[sortWord] = [word]
        
        res = []
        
        for key in anaDict:
            res.append(anaDict[key])
        
        return res