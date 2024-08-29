class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums = list(map(str, nums))
        print(snums)
        snums.sort(key=lambda x: x*10, reverse = True)
        if snums[0] == "0":
            return "0"
        return ''.join(snums)