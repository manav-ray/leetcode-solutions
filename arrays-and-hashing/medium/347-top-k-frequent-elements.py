class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        freqSort = {}
        
        for key in freq:
            currVal = freq[key]
            
            if currVal in freqSort:
                freqSort[currVal].append(key)
            else:
                freqSort[currVal] = [key]
        
        keylist = sorted(freqSort.keys(), reverse=True)
        
        res = []
        
        for key in keylist:
            currKeyList = freqSort[key]
            
            for j in currKeyList:
                if len(res) == k:
                    break
                
                res.append(j)
            
            if len(res) == k:
                break
        
        return res