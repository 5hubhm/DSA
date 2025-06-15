from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = Counter(nums)
        print(h_map)  

        sorted_h_map = dict(sorted(h_map.items(), key=lambda x: x[1], reverse=True))
        print(h_map)  

        res = []
        for num in sorted_h_map:
            if k>0:
                res.append(num)   
            k-=1 
        
        return res