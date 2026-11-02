import networkx as nx
import time

def detect_deadlock(edges, test_name):
    print(f"\n{'='*50}")
    print(f"RUNNING: {test_name}")
    print(f"{'='*50}")
    
    G = nx.DiGraph()
    G.add_edges_from(edges)
    
    print(f"Nodes: {list(G.nodes())}")
    print(f"Edges: {list(G.edges())}")
    
    print("Running Depth-First Search (DFS) Cycle Detection...")
    time.sleep(1) # Small pause for dramatic effect
    
    try:
        cycle = nx.find_cycle(G)
        print("\n[⚠️] DEADLOCK DETECTED! [⚠️]")
        
        # Format the cycle output correctly
        cycle_nodes = [u for u, v in cycle] + [cycle[0][0]]
        path_str = " -> ".join(cycle_nodes)
        
        print(f"🔴 Circular Wait Path: {path_str}")
        print("Status: SYSTEM FROZEN. Resolution required.")
        
    except nx.NetworkXNoCycle:
        print("\n[✅] SYSTEM IS SAFE [✅]")
        print("Status: No circular waits detected. System is stable.")

if __name__ == "__main__":
    print("=========================================")
    print(" DEADLOCK DETECTION - CORE ENGINE (CLI) ")
    print("=========================================")

    # Test Case 1: Deadlock (P1 holds R1, P2 holds R2, they want each other's resources)
    deadlock_edges = [
        ("P1", "R1"), ("R1", "P1"),  
        ("P2", "R2"), ("R2", "P2"),  
        ("P1", "R2"), ("P2", "R1")   
    ]
    detect_deadlock(deadlock_edges, "TEST CASE 1: DEADLOCK SCENARIO")

    # Test Case 2: Safe State (P1 has R1, P3 is just waiting for R1, but there is no cycle)
    safe_edges = [
        ("R1", "P1"), # P1 is assigned R1
        ("R2", "P2"), # P2 is assigned R2
        ("P3", "R1"), # P3 requests R1 (waits for P1 to finish, but P1 isn't waiting for P3)
        ("P4", "R2")  # P4 requests R2 (waits for P2 to finish)
    ]
    detect_deadlock(safe_edges, "TEST CASE 2: SAFE SCENARIO")
    
    print("\n=========================================")
    print(" DEMO COMPLETE. ")
    print("=========================================")