'''
def dfs(state):
    # Termination condition.
    if meets_termination_condition(state):
        process_solution(state)
        return
    # Explore each possible decision that can be made at the current state.
    for decision in possible_decisions(state):
        make_decision(state, decision)
        dfs(state)
        undo_decision(state, decision)  # Backtrack.
'''

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def dfs(idx, subset):
            nonlocal total
            xor = 0
            for n in subset:
                xor ^= n
            total += xor

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
        
        dfs(0, [])
        return total