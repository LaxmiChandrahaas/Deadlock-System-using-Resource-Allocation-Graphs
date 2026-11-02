# 🔒 Deadlock Detection System using Resource Allocation Graphs (RAG)

## 📖 Overview
This project is a comprehensive Operating Systems simulator designed to detect Deadlocks in real-time. It visually models processes and resources using a **Resource Allocation Graph (RAG)** and implements a **Depth-First Search (DFS)** algorithm to identify circular waits (deadlocks). 

The project features two distinct components:
1. **Core CLI Engine** (`cli_test.py`): A command-line version to demonstrate the raw algorithm logic.
2. **Interactive Web UI** (`app.py`): A visual dashboard built with Streamlit to dynamically add processes/resources and visualize the graph.

## ✨ Features
*   **Real-time Cycle Detection:** Uses NetworkX and DFS to instantly scan for circular dependencies.
*   **Dynamic Visualization:** Processes are rendered as blue nodes, and resources as orange nodes.
*   **Deadlock Alert System:** Highlights the exact blocked path in **Red** and triggers a system frozen warning.
*   **Safe State Check:** Automatically detects and confirms when the system is in a safe state (Green).
*   **Dual Interface:** Includes both a terminal-based logic tester and a modern web-based GUI.

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Web Framework:** Streamlit
*   **Graph Theory & Algorithms:** NetworkX
*   **Data Visualization:** Matplotlib

