class Solution:
    def addOne(self,head):
        str1 = ''
        while head != None:
            str1 += str(head.data)
            head = head.next
        num1 = int(str1)
        num1 = num1 + 1
        str1 = str(num1)
        sol = []
        for i in range(len(str1)):
            sol.append(int(str1[i]))
        dum = Node(0)
        ans = dum
        for i in sol:
            ans.next = Node(i)
            ans = ans.next
        return(dum.next)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        for i in arr:
            list1.insert(i)

        resHead = Solution().addOne(list1.head)
        PrintList(resHead)
        print()

# } Driver Code Ends