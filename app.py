import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Deadlock Detector", page_icon="🔒", layout="wide")

st.title("🔒 Deadlock Detection System")
st.markdown("### Using Resource Allocation Graphs (RAG)")
st.write("This system simulates OS processes requesting resources. It uses a **Depth-First Search (DFS)** algorithm to detect circular waits (deadlocks).")

# Initialize session state for the graph
if 'edges' not in st.session_state:
    # Default scenario: P1 holds R1, P2 holds R2. P1 wants R2, P2 wants R1. (Deadlock!)
    st.session_state.edges = [
        ("P1", "R1"), ("R1", "P1"), 
        ("P2", "R2"), ("R2", "P2"), 
        ("P1", "R2"), ("P2", "R1")
    ]

# --- Sidebar Controls ---
st.sidebar.header("🛠️ Graph Controls")
edge_type = st.sidebar.selectbox("Action", ["Process Requests Resource", "Resource Assigned to Process"])
proc = st.sidebar.selectbox("Process", ["P1", "P2", "P3", "P4"])
res = st.sidebar.selectbox("Resource", ["R1", "R2", "R3", "R4"])

if st.sidebar.button("➕ Add Connection"):
    new_edge = (proc, res) if edge_type == "Process Requests Resource" else (res, proc)
    if new_edge not in st.session_state.edges:
        st.session_state.edges.append(new_edge)
        st.rerun()

if st.sidebar.button("🗑️ Clear Graph"):
    st.session_state.edges = []
    st.rerun()

if st.sidebar.button("🔄 Load Default Deadlock"):
    st.session_state.edges = [
        ("P1", "R1"), ("R1", "P1"), 
        ("P2", "R2"), ("R2", "P2"), 
        ("P1", "R2"), ("P2", "R1")
    ]
    st.rerun()

# --- Graph Logic ---
G = nx.DiGraph()
G.add_edges_from(st.session_state.edges)

# Detect Deadlock (Cycle Detection using DFS)
deadlock_detected = False
cycle_edges = []

if G.number_of_nodes() > 0:
    try:
        cycle_edges = nx.find_cycle(G)
        deadlock_detected = True
    except nx.NetworkXNoCycle:
        deadlock_detected = False

# --- UI Display ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Resource Allocation Graph")
    if G.number_of_nodes() > 0:
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Draw nodes (Blue for Process, Orange for Resource)
        color_map = ['skyblue' if node.startswith("P") else 'orange' for node in G]
        pos = nx.spring_layout(G, seed=42)
        
        nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=2500, 
                font_size=14, font_weight="bold", arrowsize=25, ax=ax,
                edge_color='gray', width=2)
        
        # Highlight the deadlock cycle in Red
        if deadlock_detected:
            nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='red', width=3, ax=ax)
            
        st.pyplot(fig)
    else:
        st.info("Graph is empty. Add connections from the sidebar.")

with col2:
    st.subheader("🚦 System Status")
    if deadlock_detected:
        st.error("🔴 **DEADLOCK DETECTED!**")
        st.write("The OS has found a circular wait. System is frozen.")
        
        # List the processes involved
        involved = list(set([node for edge in cycle_edges for node in edge if node.startswith("P")]))
        st.markdown(f"**Processes involved:** `{', '.join(involved)}`")
        st.markdown("**Resolution:** The OS must terminate one of these processes to break the cycle.")
    else:
        st.success("🟢 **System is SAFE**")
        st.write("No circular waits detected. All processes can complete successfully.")