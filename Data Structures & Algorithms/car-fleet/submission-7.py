class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for i, e in enumerate(pairs):
            p, s = e
            diff = target - p
            req_time = diff / s
            stack.append(req_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)