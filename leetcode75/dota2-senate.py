class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        index_r, index_d = [], []
        for idx, s in enumerate(senate):
            if s == "R":
                index_r.append(idx)
            else:
                index_d.append(idx)

        while index_r and index_d:
            ridx = index_r.pop(0)
            didx = index_d.pop(0)
            if ridx < didx:
                index_r.append(ridx + n)
            else:
                index_d.append(didx + n)
        
        return "Radiant" if index_r else "Dire"
        
