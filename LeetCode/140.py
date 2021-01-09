class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        results = []

        if (len(s) == 0):
            results.append("");
            return results

        for word in wordDict:
            if not s.startswith(word):
                continue
            
            if len(word) == len(s):
                results.append(word)

            else:
                sub = s[len(word):]
                substring = self.helper(sub, wordDict, memo)

                for substr in substring:
                    results.append(word + " " + substr)

        memo[s] = results
        print(memo)
        return results