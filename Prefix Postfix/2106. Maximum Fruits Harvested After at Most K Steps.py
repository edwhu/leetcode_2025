### Attempt 2 ###
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        score = 0
        prefix = [0] * 210000
        for pos, amt in fruits:
            prefix[pos] = amt
        accum = 0
        for idx in range(len(prefix)):
            accum += prefix[idx]
            prefix[idx] = accum

        
        def rangeSum(left, right):
            # prefix[i] = n[0...i]
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left-1]

        # think about what the valid ranges are.
        for left_steps in range(k+1): # [0...k]
            left = startPos - left_steps
            if left < 0:
                break
            right_steps = k - (2 * left_steps)
            right = min(210000 - 1, startPos + right_steps)
            if right < left:
                continue
            score = max(score, rangeSum(left, right))

        for right_steps in range(k+1):
            right = startPos + right_steps
            if right >= len(prefix):
                break
            left_steps = k - (2 * right_steps)
            left = max(0, startPos - left_steps)
            if right < left:
                continue
            score = max(score, rangeSum(left, right))
        return score
            

### Attempt 1, times out for k=200000. also not correct, doesn't consider going right and then back to startpos###
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        highest_score = 0
        fruit_map = {pos: amount for (pos, amount) in fruits}

        for i in range(k+1):
            score = 0
            pos = startPos

            left_steps = k - i
            for _ in range(left_steps):
                pos -= 1
                if pos in fruit_map:
                    score += fruit_map[pos]
            right_steps = i
            for _ in range(right_steps):
                pos += 1
                if pos in fruit_map:
                    score += fruit_map[pos]
            highest_score = max(score, highest_score)
        
        return highest_score