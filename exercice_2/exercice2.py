from collections import deque
from exercice_2 import Graph

def manual_test(graph):
    """Enables a user to enter the edges manually"""
    while True:
        edge = input("Enter an Edge (Format: A -> B) or 'done' to end: ")
        if edge.lower() == "done":
            break
        if "->" in edge:
            u, v = map(str.strip, edge.split("->"))
            graph.add_edge(u,v)
        else:
            print("Invalid format. Use 'A -> B'.")

def main():
    """Main Menu Exercise 2"""
    graph = Graph()

    while True:
        print("\n\n* MAIN MENU EXERCISE 2 *")
        print("1. Load a graph from a file")
        print("2. Enter a graph manually")
        print("3. Do a BFS")
        print("4. Do a DFS")
        print("5. Verify if two places are connected")
        print("6. Exit")

        choice = input("Enter your choice (1-6) : ")

        if choice == "1":
            filename = input("Enter the file name of the batch of tests (eg: test_cases.txt) : ")
            graph.load_from_file(filename)
            print("Graph load with success")
        elif choice == "2":
            manual_test(graph)
        elif choice == "3":
            start = input("Enter the starting point for BFS : ")
            if start in graph.graph:
                print("BFS pathway : ", graph.bfs(start))
            else:
                print("This node is not in the graph.")

        elif choice == "4":
            start = input("Enter the starting point for DFS : ")
            if start in graph.graph:
                print("DFS pathway : ", graph.dfs(start))
            else:
                print("This node is not existing in the graph.")

        elif choice == "5":
            start = input("Place to start : ")
            end = input("Plaec to end : ")
            if start in graph.graph and end in graph.graph:
                path = graph.is_connected(start, end)
                print(f"Path found : {path}" if path else "No path found.")
        
            else:
                print("One of these nodes are not existing in the graph.")
        
        elif choice == "6":
            print("Exciting...\n\n")
            break
        else:
            print("Invalid choice. Please enter a valid choice between 1 and 6.")

if __name__ == "__main__":
    main()