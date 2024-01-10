class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K) :
        prefix_sum_remainders = {0: -1}
        max_length = 0
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            remainder = curr_sum % K
            if remainder in prefix_sum_remainders:
                max_length = max(max_length, i - prefix_sum_remainders[remainder])
            else:
                prefix_sum_remainders[remainder] = i
        return max_length

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends