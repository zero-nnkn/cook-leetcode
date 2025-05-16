class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        min_num, max_num = min(arr), max(arr)
        count = [0] * (max_num - min_num + 1)
        for num in arr:
            count[num - min_num] += 1
        
        count2idx = {}
        for idx, c in enumerate(count):
            if c in count2idx:
                return False
            elif c > 0:
                count2idx[c] = idx
        return True
