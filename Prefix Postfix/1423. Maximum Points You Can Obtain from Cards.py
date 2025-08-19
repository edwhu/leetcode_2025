######### Attempt 1, compute middle segment. #########
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        idea is for K, try all options.
        Let's say for K=4, these are the possible draws.
        LLLL
        LLLR
        LLRR
        LRRR
        RRRR
        We can represent each option as a range, and we can query the sum of a range in O(1).
        So runtime will be O(cardPoints) + O(k+1) = O(cardPoints)
        """
        accum = 0
        prefix = [0]
        for n in cardPoints:
            accum += n
            prefix.append(accum)
        # p[i] = n[0...i-1], query range by doing prefix[right+1] - prefix[left]
        def rangeSum(left, right):
            # print(left, right, len(prefix))
            return prefix[right+1] - prefix[left]
        # now enumerate all possible options
        score = 0
        for i in range(k+1):
            left = k-i
            right = (len(cardPoints) - 1) - i
            candidate = accum - rangeSum(left, right)
            # print(left, right, candidate)
            score = max(score, candidate)
        return score
######### Attempt 2, compute left and right segments. #########
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        idea is for K, try all options.
        Let's say for K=4, these are the possible draws.
        LLLL
        LLLR
        LLRR
        LRRR
        RRRR
        We can represent each option as a range, and we can query the sum of a range in O(1).
        So runtime will be O(cardPoints) + O(k+1) = O(cardPoints)
        """
        accum = 0
        prefix = [0]
        for n in cardPoints:
            accum += n
            prefix.append(accum)
        # p[i] = n[0...i-1], query range by doing prefix[right+1] - prefix[left]
        def rangeSum(left, right):
            # print(left, right, len(prefix))
            return prefix[right+1] - prefix[left]
        # now enumerate all possible options
        score = 0
        for i in range(k+1):
            pass
        return score
