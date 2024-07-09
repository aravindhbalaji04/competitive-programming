class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle = 0
        wait = 0
        for customer in customers:
            idle = max(customer[0], idle) + customer[1]
            wait += idle - customer[0]
        return wait / len(customers)