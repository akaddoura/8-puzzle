# 8-puzzle
A python driver program to solve a 3x3 8 puzzle using either breadth-first search, depth-first search or A* heuristic search using the Manhattan distance statistic.  

Using the program: 
driver.py will accept two parameters: 

  1. the algorithm to be used: "bfs", "dfs", or "ast"
  2. the puzzle in the form of a string of 9 numbers separated by space, with 0 representing the empty tile. For example: "0 1 2 3 4 5 6 7 8"
  
  Note: currently the program will not fully check for correct puzzle input such as repeated numbers, but will simply error out when it fails 
  to move a tile to an impossible decision or keep searching without finding an answer. 
  
  Example parameter input: 
  
  $ driver.py ast "6 1 8 4 0 2 7 3 5"

driver.py will create an output.txt file in the same folder with the steps to solve the problem.
