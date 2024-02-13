class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if len(words[i])%2==0:
                n = len(words[i])//2
                if words[i][:n] == words[i][n:][::-1]:
                    return words[i]
            else:
                n = (len(words[i])-1)//2
                if words[i][:n] == words[i][n+1:][::-1]:
                    return words[i]
        return ""