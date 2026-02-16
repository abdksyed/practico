# Given an integer array nums and an integer k,
# return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

class Solution:
    def topK_frequent(self, nums: list[int], k: int) -> list[int]:

        # region Solution 1 Max heap
        # T -> O(n + klogm) (m -> unique elements)
        # S -> O(m)
        # import heapq
        # from collections import Counter
        # freq = Counter(nums)
        # h = [(-value, key) for key, value in freq.items()]
        # heapq.heapify(h) # max heap
        # return [heapq.heappop(h)[1] for _ in range(k)]
        # endregion

        # region Solution 2 Bucket Sort
        # Create an array of size N+1, since there could be max N unique elements
        # N+1 because 0 is not a valid frequency
        # store the each element in the index of its frequency
        # Example: {100: 3, 145: 2, 156: 2} -> [None, None, [145, 156], [100]]
        # T -> O(n+m) = O(n)
        # S -> O(n+m) = O(n)
        # from collections import Counter
        # freq = Counter(nums)
        # results = [None]*(len(nums)+1)
        # for num, count in freq.items():
        #     if results[count] is None: results[count] = []
        #     results[count].append(num)
        # return [item for sublist in results[::-1] if sublist for item in sublist][:k]
        # endregion

        # region Solution 3 Min Heap
        # When we have small k, max heap is not efficient
        # We can use a min heap to get the top k elements when k << m
        # We only need to do smaller, logK, instead of much large, logM operations
        # T -> O(n + mlogk)
        # S -> O(k) (since min heap only stores top k elements, where as max heap stores all unique elements)
        from collections import Counter
        import heapq
        freq = Counter(nums)
        heap = []
        for key, count in freq.items():
            heapq.heappush(heap, (count, key))
            if len(heap) > k:
                # remove the smallest element, since it is no longer in the top k
                heapq.heappop(heap) 
        return [item[1] for item in heap]
        # endregion