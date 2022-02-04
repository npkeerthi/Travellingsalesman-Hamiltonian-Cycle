from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

# store all vertex apart from source vertex
    vertex=[i for i in range(V) if i!=s]
                                                         #   print(vertex)
    
# store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    
    for p in next_permutation:
                                                         #   print("\n For :",p)
        
        # store current Path weight(cost)
        current_pathweight = 0
        
        # [0, 10, 15, 20], [10, 0, 35, 25]
        # [15, 35, 0, 30], [20, 25, 30, 0]
        
        # compute current path weight
        k = s
        for j in p:
            
                                                        # print(current_pathweight,graph[k][j])
            current_pathweight += graph[k][j]
                                                        # print(current_pathweight)
            k = j
            
                                                        # print(f"{graph[k][s]}+{current_pathweight}:",end=" ")
        current_pathweight += graph[k][s]
                                                        # print(current_pathweight)
 
        # update minimum
        min_path = min(min_path, current_pathweight)
        
         
    return min_path
 
 
# Driver Code
if __name__ == "__main__":
 
    # matrix representation of graph
    
    graph = [
         #   a   b   c   d
            [0, 10, 15, 20], [10, 0, 35, 25],
    
            [15, 35, 0, 30], [20, 25, 30, 0]
            ]
    s = 0
    print("Travelling Salesman Minimum weight Hamiltonian Cycle :",travellingSalesmanProblem(graph, s))









# def recursive_dfs(graph, source,path = []):

#       if source not in path:

#           path.append(source)

#           if source not in graph:
#               # leaf node, backtrack
#               return path

#           for neighbour in graph[source]:

#               path = recursive_dfs(graph, neighbour, path)


#       return path
# graph = {"A":["B","C", "D"],
#           "B":["E"],
#           "C":["F","G"],
#           "D":["H"],
#           "E":["I"],
#           "F":["J"]}


# path = recursive_dfs(graph, "E")

# print(" ".join(path))
