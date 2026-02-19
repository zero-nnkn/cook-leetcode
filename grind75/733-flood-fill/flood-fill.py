from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_color = image[sr][sc]
        if source_color == color:
            return image

        rows, cols = len(image), len(image[0])
        candidates = deque([(sr, sc)])
        
        while candidates:
            ri, ci = candidates.popleft()

            image[ri][ci] = color

            for (adjacent_ri, adjacent_ci) in (
                (ri -1, ci),
                (ri + 1, ci),
                (ri, ci -1),
                (ri, ci + 1),
            ):
                if adjacent_ri >= 0 and adjacent_ri < rows and adjacent_ci >= 0 and adjacent_ci < cols and image[adjacent_ri][adjacent_ci] == source_color:
                    candidates.append((adjacent_ri, adjacent_ci))

        return image

        