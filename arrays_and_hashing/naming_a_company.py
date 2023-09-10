# Link: https://leetcode.com/problems/naming-a-company/

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# (Hashset)
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        prefixDict = defaultdict(set)
        ans = 0

        for name in ideas:
            prefixDict[name[0]].add(name[1:])
        
        for prefix1 in prefixDict:
            for prefix2 in prefixDict:
                if prefix1 == prefix2:
                    continue
                
                shared = len(prefixDict[prefix1].intersection(prefixDict[prefix2]))
                uniq1, uniq2 = len(prefixDict[prefix1])-shared, len(prefixDict[prefix2])-shared
                ans += uniq1 * uniq2

        return ans