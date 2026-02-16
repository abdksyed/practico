# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]


from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        # region Solution 1
        # T -> O(n²*k)
        # S -> O(n*k)
        # def check_anagram(s: str, t: str) -> bool:
        #     from collections import Counter
        #     if len(s) != len(t): return False
        #     return Counter(s) == Counter(t)

        # seen = set()
        # results = []
        # for i in range(len(strs)):
        #     if strs[i] in seen:
        #         continue
        #     current_anagrams = [strs[i]]
        #     for j in range(i+1, len(strs)):
        #         if check_anagram(strs[i], strs[j]):
        #             seen.add(strs[j])
        #             current_anagrams.append(strs[j])
        #     results.append(current_anagrams)
        # return results
        # end region

        # region Solutin 2
        # T -> O(n * klogk)
        # S -> O(n*k)
        # from collections import defaultdict
        # hash_map = defaultdict(list)
        # for s in strs:
        #     hash_map["".join(sorted(s))].append(s)
        # return list(hash_map.values())
        # endregion

        # T -> O(n * k)
        # S -> O(n * k)
        hash_map = defaultdict(list)
        for s in strs:
            key = [0]*26
            for i in s:
                key[ord(i)-ord('a')] += 1
            hash_map[tuple(key)].append(s)
        return list(hash_map.values())




