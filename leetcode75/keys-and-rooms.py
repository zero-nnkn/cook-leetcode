class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        is_visited = [False] * len(rooms)
        while stack:
            picked_room = stack.pop(-1)
            is_visited[picked_room] = True
            for key in rooms[picked_room]:
                if key not in stack and not is_visited[key]:
                    stack.append(key)
        return all(is_visited)
            
