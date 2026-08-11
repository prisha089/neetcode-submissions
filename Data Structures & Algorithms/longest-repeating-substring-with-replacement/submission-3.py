class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        start = 0
        max_length = 0
        max_count = 0

        for i in range(len(s)):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
            max_count = max(max_count, counts[char])
            window_length = i - start + 1

            if window_length - max_count > k:
                counts[s[start]] -= 1
                start += 1

            max_length = max(max_length, i - start + 1)

        return max_length