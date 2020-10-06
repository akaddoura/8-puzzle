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

path_to_goal:     ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up']  
nodes_expanded:   583  
search_depth:     21  
max_search_depth: 21  
running_time:     00:00:01  
  
h-value: 10  
+-----+  
|6|1|8|  
\-------  
|4|0|2|  
\-------  
|7|3|5|  
+-----+  
   |  
   v  
h-value: 9  
+-----+  
|6|1|8|  
\-------  
|4|3|2|  
\-------  
|7|0|5|  
+-----+  
   |  
   v  
h-value: 10  
+-----+  
|6|1|8|  
\-------  
|4|3|2|  
\-------  
|7|5|0|  
+-----+  
   |  
   v  
h-value: 11  
+-----+  
|6|1|8|  
\-------  
|4|3|0|  
\-------  
|7|5|2|  
+-----+   
   |  
   v  
h-value: 10  
+-----+  
|6|1|0|  
\-------  
|4|3|8|  
\-------  
|7|5|2|  
+-----+  
   |  
   v  
h-value: 11  
+-----+
|6|0|1|
-------
|4|3|8|
-------
|7|5|2|
+-----+
   |
   v
h-value: 12
+-----+  
|6|3|1|  
\-------  
|4|0|8|   
\-------  
|7|5|2|  
+-----+  
   |  
   v  
h-value: 13  
+-----+  
|6|3|1|  
\-------  
|4|8|0|  
\-------  
|7|5|2|  
+-----+  
   |  
   v  
h-value: 12  
+-----+
|6|3|1|
-------
|4|8|2|
-------
|7|5|0|
+-----+
   |
   v
h-value: 11
+-----+  
|6|3|1|  
\-------  
|4|8|2|  
\-------  
|7|0|5|  
+-----+  
   |  
   v  
h-value: 10  
+-----+  
|6|3|1|  
\-------  
|4|0|2|  
\-------  
|7|8|5|  
+-----+  
   |  
   v  
h-value: 9  
+-----+  
|6|3|1|  
\-------  
|0|4|2|  
\-------  
|7|8|5|  
+-----+  
   |  
   v  
h-value: 8  
+-----+  
|0|3|1|  
\-------  
|6|4|2|  
\-------  
|7|8|5|  
+-----+  
   |  
   v    
h-value: 7  
+-----+  
|3|0|1|  
\-------  
|6|4|2|  
\-------  
|7|8|5|  
+-----+  
   |  
   v  
h-value: 6  
+-----+  
|3|1|0|  
\-------  
|6|4|2|  
\-------  
|7|8|5|  
+-----+  
   |  
   v  
h-value: 5  
+-----+  
|3|1|2|  
\-------  
|6|4|0|  
\-------  
|7|8|5|  
+-----+  
   |  
   v  
h-value: 4  
+-----+  
|3|1|2|  
\-------  
|6|4|5|  
\-------  
|7|8|0|  
+-----+  
   |  
   v  
h-value: 3  
+-----+  
|3|1|2|  
\-------  
|6|4|5|  
\-------  
|7|0|8|  
+-----+  
   |  
   v  
h-value: 2  
+-----+  
|3|1|2|  
\-------  
|6|4|5|  
\-------  
|0|7|8|  
+-----+  
   |  
   v  
h-value: 1  
+-----+   
|3|1|2|  
\-------  
|0|4|5|  
\-------  
|6|7|8|  
+-----+  
   |  
   v  
h-value: 0  
+-----+  
|0|1|2|  
\-------  
|3|4|5|  
\-------  
|6|7|8|  
+-----+  
