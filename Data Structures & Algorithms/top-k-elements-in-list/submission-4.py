from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1

        sorted_list = sorted(freq_dict.items(), key=lambda x:x[1], reverse=True)

        return [num for num, _ in sorted_list[:k]]