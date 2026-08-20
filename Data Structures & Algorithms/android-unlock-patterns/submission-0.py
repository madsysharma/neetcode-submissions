class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[4][6] = skip[6][4] = 5
        skip[7][9] = skip[9][7] = 8
        skip[1][7] = skip[7][1] = 4
        skip[2][8] = skip[8][2] = 5
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5

        def dfs(curr, length, visited):
            if length == 0:
                return 1
            visited.add(curr)
            count = 0
            for next_node in range(1, 10):
                if next_node not in visited:
                    s = skip[curr][next_node]
                    if s == 0 or s in visited:
                        count += dfs(next_node, length - 1, visited)
            visited.remove(curr)
            return count

        res = 0
        for length in range(m, n + 1):
            res += dfs(1, length - 1, set()) * 4
            res += dfs(2, length - 1, set()) * 4
            res += dfs(5, length - 1, set())
        return res