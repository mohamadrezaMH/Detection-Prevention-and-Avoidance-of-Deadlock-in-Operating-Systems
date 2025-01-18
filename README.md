# Deadlock Occurrence, Detection, and Resolution in Operating Systems

This project demonstrates how deadlocks occur, how to detect them using graph-based methods, and how to resolve them using the Banker's Algorithm. The project is divided into three phases, each focusing on a specific aspect of deadlock management.

---

## Phase 1: Simulating a Deadlock Scenario

### Resource Class
The `Resource` class represents a system resource and provides methods to allocate and release resource units safely.  

**Key Features:**  
- **Initialization:** Each resource has a `name`, `total_units` (total available), and `allocated_units` (initially set to 0).  
- **Allocation:** The `allocate` method ensures resources are only allocated if sufficient units are available.  
- **Release:** The `release` method frees up allocated units, maintaining the integrity of resource usage.  

### Deadlock Simulation
The simulation creates processes and resources to model a deadlock scenario.  

**Key Components:**  
1. **Process Class:** Represents system processes, with methods to request and release resources.  
2. **Deadlock Scenario:**  
   - Resources `R1` and `R2` are created with one unit each.  
   - Processes `P1`, `P2`, and `P3` attempt to allocate resources in a manner that leads to a deadlock:  
     - `P1` holds `R1` and waits for `R2`.  
     - `P2` holds `R2` and waits for `R1`.  
     - `P3` waits for both `R1` and `R2`.  

**Output:** A clear demonstration of how deadlocks occur in a resource-constrained environment.

---

## Phase 2: Graph-Based Deadlock Detection

In this phase, a graph structure is implemented to represent processes, resources, and their interactions. Two approaches are provided:

### Approach 1: Without Libraries  
A custom `Graph` class is used to simulate the resource allocation graph and detect deadlocks using Depth-First Search (DFS).  

**Features:**  
- **Nodes:** Represent processes and resources.  
- **Edges:**  
  - Allocation edges (`P → R`): A process holds a resource.  
  - Request edges (`R → P`): A process requests a resource.  
- **Deadlock Detection:** Cycles in the graph indicate deadlocks.  

**Example:**  
1. Add nodes for processes (`P1, P2, P3`) and resources (`R1, R2`).  
2. Add edges to simulate resource allocation and requests.  
3. Detect deadlocks using the `detect_deadlock` method.  

### Approach 2: Using `networkx` and `matplotlib`  
This approach visualizes the graph and identifies deadlocks more efficiently using the `networkx` library.  

**Visualization:**  
- **Nodes:**  
  - Processes (gray rectangles).  
  - Resources (blue circles).  
- **Edges:**  
  - Requests (red dashed lines).  
  - Allocations (green solid lines).  
- **Graph Drawing:** Displayed using `matplotlib` with labeled edges and nodes.  

**Example:**  
1. Create a directed graph (`DiGraph`).  
2. Add nodes and edges for processes and resources.  
3. Visualize the graph and detect deadlocks using `networkx`'s cycle detection.

---

## Phase 3: Implementing the Banker's Algorithm

The Banker's Algorithm is used to prevent deadlocks by ensuring the system remains in a safe state during resource allocation.  

### BankersAlgorithm Class
**Attributes:**  
- `total_resources`: Total available resources.  
- `max_demand`: Maximum resource demand per process.  
- `allocation`: Current resource allocation per process.  
- `need`: Remaining resource needs.  
- `available`: Currently available resources.  

**Key Methods:**  
1. **is_safe:**  
   - Determines if the system is in a safe state by simulating process completion.  
   - Returns `True` and a safe sequence if found, otherwise `False`.  

2. **request_resources:**  
   - Checks if a process's resource request can be safely granted.  
   - Allocates resources if the system remains in a safe state, otherwise rolls back changes.  

**Example Usage:**  
1. Initialize `BankersAlgorithm` with system resource data.  
2. Request resources for a process and check if the request is granted.  
3. Output the safe sequence if the system remains safe.

---

## Dependencies
To run this project, ensure the following libraries are installed:  
```bash
pip install networkx matplotlib
```

---

## Examples and Test Cases

### Phase 1: Deadlock Simulation  
Input:  
- Processes: `P1, P2, P3`.  
- Resources: `R1, R2`.  

Output:  
- `P1` and `P2` hold resources and block `P3`. Deadlock occurs.  

### Phase 2: Deadlock Detection  
Input:  
- Graph edges representing requests and allocations.  

Output:  
- Deadlock detected. Graph visualization displayed.  

### Phase 3: Banker's Algorithm  
Input:  
- Resource allocation and maximum demands.  

Output:  
- Safe sequence found or request denied with explanation.
