from typing import List
from bisect import bisect_right, bisect_left


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        total_ones = s.count("1")

        # Build runs: (character, start_index, end_index)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j

        # For every valid 0+1+0 pattern, store:
        # center one-run start/end, and lengths of adjacent zero-runs.
        starts = []
        ends = []
        left_zeros = []
        right_zeros = []
        full_gain = []

        for i in range(1, len(runs) - 1):
            ch, one_start, one_end = runs[i]

            if ch != "1":
                continue

            _, left_start, left_end = runs[i - 1]
            _, right_start, right_end = runs[i + 1]

            # Runs alternate, so neighbors here are necessarily zero-runs.
            left_len = left_end - left_start + 1
            right_len = right_end - right_start + 1

            starts.append(one_start)
            ends.append(one_end)
            left_zeros.append(left_len)
            right_zeros.append(right_len)
            full_gain.append(left_len + right_len)

        m = len(starts)

        # Segment tree: maximum full_gain over a range of candidate one-runs.
        size = 1
        while size < m:
            size <<= 1

        seg = [0] * (2 * size)

        for i, value in enumerate(full_gain):
            seg[size + i] = value

        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[i * 2], seg[i * 2 + 1])

        def range_max(left: int, right: int) -> int:
            """Maximum full_gain in inclusive range [left, right]."""
            if left > right:
                return 0

            left += size
            right += size
            result = 0

            while left <= right:
                if left & 1:
                    result = max(result, seg[left])
                    left += 1
                if not (right & 1):
                    result = max(result, seg[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        answer = []

        for left, right in queries:
            # A center one-run is usable only if it has a zero on both
            # sides inside the query: one_start > left and one_end < right.
            lo = bisect_right(starts, left)
            hi = bisect_left(ends, right) - 1

            if lo > hi:
                answer.append(total_ones)
                continue

            # The first valid candidate may have its left zero-run clipped.
            left_gain = min(left_zeros[lo], starts[lo] - left)

            # The last valid candidate may have its right zero-run clipped.
            right_gain = min(right_zeros[hi], right - ends[hi])

            if lo == hi:
                # Same pattern is clipped on both sides.
                best_gain = left_gain + right_gain
            else:
                # First candidate: only left side can be clipped.
                best_gain = left_gain + right_zeros[lo]

                # Last candidate: only right side can be clipped.
                best_gain = max(best_gain, left_zeros[hi] + right_gain)

                # All candidates strictly between are fully inside the query.
                best_gain = max(best_gain, range_max(lo + 1, hi - 1))

            answer.append(total_ones + best_gain)

        return answer