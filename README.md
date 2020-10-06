# 8-puzzle
A python driver program to solve a 3x3 8 puzzle using either breadth-first search, depth-first search or A* heuristic search using the Manhattan distance statistic.  

Using the program: 
driver.py will accept two parameters: 

  1. the algorithm to be used: "bfs", "dfs", or "ast"
  2. the puzzle in the form of a string of 9 numbers separated by space, with 0 representing the empty tile. For example: "0 1 2 3 4 5 6 7 8"
  
  Note: currently the program will not fully check for correct puzzle input such as repeated numbers, but will simply error out when it fails 
  to move a tile to an impossible decision or keep searching without finding an answer. 
  
  Example parameter input: 
  
  $ driver.py ast "3 1 2 0 4 5 6 7 8"

driver.py will create an output.txt file in the same folder with the steps to solve the problem.

## Example output: 

path_to_goal:     ['Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Left', 'Left', 'Up', 'Right', 'Right', 'Down', 'Left', 'Down', 'Left', 'Up', 'Right', 'Down', 'Right', 'Up', 'Left', 'Left', 'Up', 'Right', 'Down', 'Left', 'Up']
nodes_expanded:   20987
search_depth:     29
max_search_depth: 29
running_time:     00:08:45

h-value: 14
+-----+
/|8|6|4|/
-------
|2|1|3|
-------
|5|7|0|
+-----+
   |
   v
h-value: 14
+-----+
|8|6|4|
-------
|2|1|3|
-------
|5|0|7|
+-----+
   |
   v
h-value: 14
+-----+
|8|6|4|
-------
|2|0|3|
-------
|5|1|7|
+-----+
   |
   v
h-value: 12
+-----+
|8|6|4|
-------
|0|2|3|
-------
|5|1|7|
+-----+
   |
   v
h-value: 10
+-----+
|0|6|4|
-------
|8|2|3|
-------
|5|1|7|
+-----+
   |
   v
h-value: 12
+-----+
|6|0|4|
-------
|8|2|3|
-------
|5|1|7|
+-----+
   |
   v
h-value: 14
+-----+
|6|4|0|
-------
|8|2|3|
-------
|5|1|7|
+-----+
   |
   v
h-value: 14
+-----+
|6|4|3|
-------
|8|2|0|
-------
|5|1|7|
+-----+
   |
   v
h-value: 14
+-----+
|6|4|3|
-------
|8|0|2|
-------
|5|1|7|
+-----+
   |
   v
h-value: 12
+-----+
|6|4|3|
-------
|0|8|2|
-------
|5|1|7|
+-----+
   |
   v
h-value: 10
+-----+
|0|4|3|
-------
|6|8|2|
-------
|5|1|7|
+-----+
   |
   v
h-value: 12
+-----+
|4|0|3|
-------
|6|8|2|
-------
|5|1|7|
+-----+
   |
   v
h-value: 12
+-----+
|4|3|0|
-------
|6|8|2|
-------
|5|1|7|
+-----+
   |
   v
h-value: 12
+-----+
|4|3|2|
-------
|6|8|0|
-------
|5|1|7|
+-----+
   |
   v
h-value: 10
+-----+
|4|3|2|
-------
|6|0|8|
-------
|5|1|7|
+-----+
   |
   v
h-value: 10
+-----+
|4|3|2|
-------
|6|1|8|
-------
|5|0|7|
+-----+
   |
   v
h-value: 8
+-----+
|4|3|2|
-------
|6|1|8|
-------
|0|5|7|
+-----+
   |
   v
h-value: 6
+-----+
|4|3|2|
-------
|0|1|8|
-------
|6|5|7|
+-----+
   |
   v
h-value: 6
+-----+
|4|3|2|
-------
|1|0|8|
-------
|6|5|7|
+-----+
   |
   v
h-value: 8
+-----+
|4|3|2|
-------
|1|5|8|
-------
|6|0|7|
+-----+
   |
   v
h-value: 8
+-----+
|4|3|2|
-------
|1|5|8|
-------
|6|7|0|
+-----+
   |
   v
h-value: 6
+-----+
|4|3|2|
-------
|1|5|0|
-------
|6|7|8|
+-----+
   |
   v
h-value: 4
+-----+
|4|3|2|
-------
|1|0|5|
-------
|6|7|8|
+-----+
   |
   v
h-value: 4
+-----+
|4|3|2|
-------
|0|1|5|
-------
|6|7|8|
+-----+
   |
   v
h-value: 2
+-----+
|0|3|2|
-------
|4|1|5|
-------
|6|7|8|
+-----+
   |
   v
h-value: 4
+-----+
|3|0|2|
-------
|4|1|5|
-------
|6|7|8|
+-----+
   |
   v
h-value: 4
+-----+
|3|1|2|
-------
|4|0|5|
-------
|6|7|8|
+-----+
   |
   v
h-value: 2
+-----+
|3|1|2|
-------
|0|4|5|
-------
|6|7|8|
+-----+
   |
   v
h-value: 0
+-----+
|0|1|2|
-------
|3|4|5|
-------
|6|7|8|
+-----+

