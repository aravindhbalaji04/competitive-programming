class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarrays = []
        val = 0
        for i in range(len(arr)+1):
            for j in range(i, len(arr)+1):
                try:
                    if len(arr[i:j])%2==1:
                        subarrays.append(arr[i:j])
                except:
                    continue
        print(subarrays)
        for i in range(len(subarrays)):
            val += sum(subarrays[i])
        return val