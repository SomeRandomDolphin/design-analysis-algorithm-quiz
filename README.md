# QUIZ 2 DAA

|    NRP     |      Name      |
| :--------: | :------------: |
| 5025221185 | Pradipta Arya Daniswara |
| 5025221214 | Irfan Ridhana |

Our program is a python implementation of informed and uninformed search to solve the 8-puzzle problem. The informed search algorithms used BFS (Breadth-First Search) and DFS (Depth-First Search), while the uninformed search algorithm is the greedy algorithm.

## 8-Puzzle Problem
The 8-puzzle problem is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one blank space. The objective is to rearrange the tiles from an initial configuration to a desired goal configuration by sliding the tiles into the empty space. The following are the initial state and goal state that we use : 
![Screenshot 2024-05-24 183046](https://github.com/SomeRandomDolphin/design-analysis-algorithm-quiz/assets/118520867/18555567-4c6f-477d-9f07-6384a8f6f6e7)

## Uninformed Search 
Uninformed search algorithms, also known as blind search algorithms, operate without any prior knowledge or heuristic information about the problem domain or the path to the solution. These algorithms treat the search space as a "black box" and explore it systematically without any specific guidance. We use BFS (Breadth First Search) and DFS (Depth First Search) algorithm for our uninformed search algorithm.

**BFS (Breadth First Search) :**
Breadth-First Search (BFS) is an uninformed search algorithm used for traversing or searching a tree or graph data structure. It explores all the vertices at the current depth level before moving on to the vertices at the next depth level. BFS is guaranteed to find the shortest path between the start node and the goal node, provided that a solution exists.

**DFS (Depth First Search) :**
Depth-First Search (DFS) is an uninformed search algorithm used for traversing or searching a tree or graph data structure. It explores as far as possible along each branch before backtracking and exploring another branch. DFS is useful for finding a solution if it exists but may not find the optimal solution.

## Informed Search 
Informed search algorithms, also known as heuristic search algorithms, utilize additional information or heuristics to guide the search process towards the goal state more efficiently. These algorithms take advantage of domain-specific knowledge or an evaluation function (heuristic) that estimates the cost or distance to the goal. We use Greedy Search algorithm for our informed search solution.

**Greedy Search :**
Greedy algorithm is a type of algorithm that makes the locally optimal choice at each step with the hope of finding a global optimum. Greedy algorithms are often used to solve problems where it is difficult or impossible to find the global optimum directly. Greedy algorithms work by maintaining a current state and repeatedly making the locally optimal choice to improve the state. The algorithm terminates when it reaches a state where no further improvement is possible.
