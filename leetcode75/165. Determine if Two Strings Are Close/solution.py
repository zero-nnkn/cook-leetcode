from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        occurences1 = defaultdict(int)
        occurences2 = defaultdict(int)

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            occurences1[word1[i]] += 1
            occurences2[word2[i]] += 1
        
        return (sorted(list(occurences1.keys())) == sorted(list(occurences2.keys()))) and (sorted(list(occurences1.values())) == sorted(list(occurences2.values())))
        