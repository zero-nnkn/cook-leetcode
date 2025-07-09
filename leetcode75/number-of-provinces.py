class Solution:
    def dfs(self, start_city: int, isConnected: List[List[int]], is_visited: List[bool]):
        stack = [start_city]
        while stack:
            cur_city = stack.pop(-1)
            is_visited[cur_city] = True
            for city, is_connect in enumerate(isConnected[cur_city]):
                if is_connect and not is_visited[city]:
                    stack.append(city)
        return is_visited

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_province = 0
        is_visited = [False] * len(isConnected)
        for idx, isv in enumerate(is_visited):
            if not isv:
                is_visited = self.dfs(idx, isConnected, is_visited)
                num_province += 1
        return num_province
        
