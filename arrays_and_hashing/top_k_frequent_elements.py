# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Time Complexity: O(N + K log N)
# Space Complexity: O(N)
# (Max Heap)
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        heap = [(v, k) for k, v in frequencies.items()]
        
        heapq.heapify(heap)

        return [x[1] for x in heapq.nlargest(k, heap)]

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Bucket Sort)
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in frequencies.items():
            buckets[freq].append(num)

        res = []

        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    if k > 0:
                        res.append(num)
                        k -= 1
                    else:
                        return res

        return res

# Time Complexity: O(N) average case, O(N^2) worst case
# Space Complexity: O(N)
# (Quickselect/Hoare's Selection Algorithm)
from collections import Counter
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(l, r):
            # pick random pivot
            pivotIdx = random.randint(l, r)
            pivotFreq = count[elements[pivotIdx]]

            # swap pivot to the end
            elements[pivotIdx], elements[r] = elements[r], elements[pivotIdx]

            # move all less frequent elements to the left
            tmpIdx = l
            
            for i in range(l, r):
                if count[elements[i]] < pivotFreq:
                    # move to left
                    elements[i], elements[tmpIdx] = elements[tmpIdx], elements[i]
                    tmpIdx += 1

            # move pivot to its proper location
            elements[r], elements[tmpIdx] = elements[tmpIdx], elements[r]

            return tmpIdx

        def quickselect(l, r, k):
            if l == r:
                return

            # find pivot position for a random pivot index
            pivot = partition(l, r)

            # if pivot is in its final sorted position
            if pivot == k:
                return
            
            # go left
            if k < pivot:
                quickselect(l, pivot-1, k)
            # go right
            else:
                quickselect(pivot+1, r, k)

        count = Counter(nums)
        elements = list(count.keys())

        quickselect(0, len(elements)-1, len(elements)-k)

        return elements[len(elements)-k:]