class Solution:
    def kthElement(self, k, arr1, arr2):
        arr3 = arr1 + arr2
        arr3 = sorted(arr3)
        res = arr3[k-1]
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends