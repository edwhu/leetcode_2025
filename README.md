### Aug 19, 2025
Started with Prefix / Postfix problems.

### [303. Range Sum Query](https://leetcode.com/problems/range-sum-query-immutable/)
Comments: Solved it in a few minutes. But noticed I solved it by caching things from right to left, instead of left to right. Works either way, but let me try left to right as well.

Runtime: O(N) to build up the accum array, and O(1) to query for a range.
Storage: O(N) for holding the accum array.

### [1423. Maximum points you can obtain from cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/)

Ishaan: This introduces the concept of a ‘postfix’, which you might be able to intuit what that is after solving #1.

Comments: I took a look and tried to come up with a greedy solution. I also didn't pay attention to the K parameter.  Took a peek at Ishaan's hint which is to try everything. Given a K, you can list out all possible combinations of cards.

For example, K=3, you can do the possible actions:
LLL
LLR
LRR
RRR

And for each of these actions, you can represent it as a range. And since we can query ranges, we can do this efficiently.

There are two ways to represent this using ranges. The way I took, which might not be the most intuitive, is to query the range of the middle segment, which are the cards remaining:

--|--middle----|-------
Then, we can just compute the total points by doing: Accum - sum(middle) where accum is the total points of all cards. 

The more intuitive way would be to compute the sum of the left and right segments, which are the cards taken:

-left--|------|---right---
Then, we can compute the total points by doing: sum(left) + sum(right).
Ok actually this inuitive way is harder to code, so the middle range makes most sense. 


### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

Another prefix+postfix question.
I quickly came up with the solution, which is to construct a prefix and postfix array containing the multiples of everything to the left of element i and vice versa. 

But I ran into indexing problems when constructing the prefix and postfix arrays, my answer was off. I ended up re-implementing it and got it in the second try. Gonna go take a break now. 