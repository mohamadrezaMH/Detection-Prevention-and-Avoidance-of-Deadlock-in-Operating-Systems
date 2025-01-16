class Resource:
    def __init__(self, name, total_units):
        self.name = name
        self.total_units = total_units
        self.allocated_units = 0

    def allocate(self, units):
        if self.total_units - self.allocated_units >= units:
            self.allocated_units += units
            return True
        return False

    def release(self, units):
        if self.allocated_units >= units:
            self.allocated_units -= units
            return True
        return False

# Simulating a deadlock scenario
class Process:
    def __init__(self, name):
        self.name = name
        self.allocated_resources = []

    def request_resource(self, resource, units):
        if resource.allocate(units):
            self.allocated_resources.append((resource, units))
            print(f"{self.name} allocated {units} units of {resource.name}")
        else:
            print(f"{self.name} failed to allocate {units} units of {resource.name}")

    def release_resources(self):
        for resource, units in self.allocated_resources:
            resource.release(units)
            print(f"{self.name} released {units} units of {resource.name}")
        self.allocated_resources = []

# Create resources
R1 = Resource("R1", 1)
R2 = Resource("R2", 1)

# Create processes
P1 = Process("P1")
P2 = Process("P2")
P3 = Process("P3")

# Simulate deadlock
P1.request_resource(R1, 1)
P2.request_resource(R2, 1)
P3.request_resource(R1, 1)
P1.release_resources()
P3.request_resource(R1, 1)