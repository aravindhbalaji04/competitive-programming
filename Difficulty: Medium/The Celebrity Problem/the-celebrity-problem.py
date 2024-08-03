class Solution:
    def celebrity(self, mat):
        for i in range(n):
            if mat[i].count(1)==0:
                for j in range(n):
                    if mat[j][i]==0:
                        if i!=j:
                            return -1
                return i
        return -1

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends