class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        already_satisfied = 0
        
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0

        best_solution = 0
        current = 0
        
        for i, customer in enumerate(customers):
            current += customer

            if i >= X:
                current -= customers[i-X]
            best_solution = max(best_solution, current)

        return already_satisfied + best_solution