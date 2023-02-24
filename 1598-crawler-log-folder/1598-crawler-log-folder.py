class Solution:
    def minOperations(self, logs: List[str]) -> int:
        min_operation = 0
        for operation in logs:
            if operation == './':
                continue
            elif operation == '../' :
                if min_operation:
                    min_operation -= 1
                else:
                    continue
            else:
                min_operation += 1
                
        return min_operation
        