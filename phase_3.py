import numpy as np

class BankersAlgorithm:
    def __init__(self, total_resources, max_demand, allocation):
        self.total_resources = total_resources
        self.max_demand = max_demand
        self.allocation = allocation
        self.need = max_demand - allocation  #need
        self.available = total_resources - np.sum(allocation, axis=0) #available
        
    def print_need(self):
        print(self.need)
    def print_available(self):
        print(self.available)
    def is_safe(self):
        work = self.available.copy()
        finish = [False] * len(self.allocation)
        safe_sequence = []

        while len(safe_sequence) < len(self.allocation):
            progress = False
            for i in range(len(self.allocation)):
                if not finish[i] and all(self.need[i] <= work):
                    work += self.allocation[i]
                    finish[i] = True
                    safe_sequence.append(i)
                    progress = True
            if not progress:
                break
        if len(safe_sequence) == len(self.allocation):
            return True, safe_sequence
        else:
            return False, []
    def request_resources(self, process_number, request):
        if all(request <= self.need[process_number]) and all(request <= self.available):
            self.available -= request
            self.allocation[process_number] += request
            self.need[process_number] -= request
            is_safe, safe_sequence = self.is_safe()
            if is_safe:
                return True, safe_sequence
            else:
                self.available += request
                self.allocation[process_number] -= request
                self.need[process_number] += request
        return False, []
 
# Example setup for the Banker's Algorithm
total_resources = np.array([2, 3, 2])
max_demand = np.array([[1, 1, 2], [2, 1, 0], [0, 1, 1], [0, 3, 0]]) #max
allocation = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 0], [0, 1, 0]]) #allocation

bankers = BankersAlgorithm(total_resources, max_demand, allocation)

# Request resources for process 1
request = np.array([1, 0, 2])
process_number = 1

bankers.print_need()
bankers.print_available()


granted, safe_sequence = bankers.request_resources(process_number, request)
if granted:
    print("Request granted")
    print("Safe sequence:", [f"P{p+1}" for p in safe_sequence])
else:
    print("Request denied")