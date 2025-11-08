class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(index: int) -> List[str]:
            if index == len(s):
                return [""]  # base case: empty sentence at end of string
            if index in memo:
                return memo[index]

            sentences = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in word_set:
                    for rest in dfs(end):
                        # avoid unnecessary trailing space
                        sentence = word + (" " + rest if rest else "")
                        sentences.append(sentence)

            memo[index] = sentences
            return sentences

        return dfs(0)
