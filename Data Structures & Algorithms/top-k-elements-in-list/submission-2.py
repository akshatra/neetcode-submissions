from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1

        # Sort (number, count) tuples descending by count (item[1])
        sorted_pairs = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

        # Extract the top k numbers
        return [num for num, count in sorted_pairs[:k]]