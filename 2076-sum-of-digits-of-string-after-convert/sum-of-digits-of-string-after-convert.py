class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def replace_letters(text):
            alphabet = {chr(i): i - 96 for i in range(97, 123)}
            replaced_text = ' '.join(str(alphabet[char]) for char in text.lower() if char in alphabet)
            return replaced_text
        s = replace_letters(s)
        total = 0
        for i in s:
            if i != ' ':
                total += int(i)
        k -= 1
        while k > 0:
            s = str(total)
            total = 0
            for i in s:
                total += int(i)
            k -= 1
        return total