from collections import defaultdict
from typing import List, Optional

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for i, j in prerequisites:
            g[i].append(j)

        state: List[Optional[bool]] = [None] * numCourses  # None = unvisited

        def dfs(node: int) -> bool:
            if state[node] == True:   # already processed
                return True
            if state[node] == False:  # cycle detected
                return False

            state[node] = False  # mark as visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            state[node] = True   # mark as visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
