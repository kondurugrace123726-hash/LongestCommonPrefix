from typing import List
"""
Problem: Longest Common Prefix

Write a function to find the longest common prefix string
among an array of strings.

If there is no common prefix, return an empty string "".

Approach:
- Start with the first string as prefix.
- Compare it with every other string.
- Shrink the prefix until it matches the start of each string.

Time Complexity: O(n * m)
n = number of strings
m = length of shortest string
Space Complexity: O(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
