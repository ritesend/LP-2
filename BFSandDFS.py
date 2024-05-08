#import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

def bfs(graph,start):
    visited = set()
    queue=deque([start])
    visited.add(start)

    while queue:
        node=queue.popleft()
        print(node,end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def main():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node=input(f"Enter node {i+1}: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node]=neighbors

    start_node = input("Enter the start node: ")

    print('DFS = ',end=' ')
    dfs(graph,start_node)

    print('\nBFS = ',end=' ')
    bfs(graph,start_node)

main()

Enter the number of nodes: 8
Enter node 1: A
Enter neighbors of A separated by space: B C
Enter node 2: B
Enter neighbors of B separated by space: D E
Enter node 3: C
Enter neighbors of C separated by space: F G
Enter node 4: D
Enter neighbors of D separated by space: 
Enter node 5: E
Enter neighbors of E separated by space: 
Enter node 6: F
Enter neighbors of F separated by space: 
Enter node 7: G
Enter neighbors of G separated by space: H
Enter node 8: H
Enter neighbors of H separated by space: 
Enter the start node: A
DFS =  A B D E C F G H BFS =  A B C D E F G H
