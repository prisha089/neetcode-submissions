class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        top_k_pairs = sorted(count.items(), key = lambda pair:pair[1], reverse = True) [:k]

        result = []
        for pair in top_k_pairs: 
            result.append(pair[0])

        return result
            
