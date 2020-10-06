
import copy
import time
from collections import deque
import re
import heapq as heap
import os
from argparse import ArgumentParser

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, msg):
        self.msg = msg

#########################################################33
##
##  // Frontier Class \\

class Frontier:
# Frontier holds all data structures inside. It initialized the data structure according
# to the desired algorithm and provides the required functions using the same methods.
    def __init__(self, alg):
        self.algorithm = alg

        if self.algorithm == "bfs":
            self.open_nodes_bfs = []
            self.explored_nodes_bfs = set()
        elif self.algorithm == "dfs":
            self.open_nodes_dfs = deque()
            self.explored_nodes_dfs = set()
        elif self.algorithm == "ast":
            self.open_nodes_ast = []
            self.explored_nodes_ast = set()
            heap.heapify(self.open_nodes_ast)
        else:
            raise InputError("Incorrect algorithm specified.")

    def enqueue(self, item):
        if self.algorithm == "bfs":
            add_node = True
            for check_node in self.explored_nodes_bfs:
                if item.values == check_node.values:
                    add_node = False
            for check_node in self.open_nodes_bfs:
                if item.values == check_node.values:
                    add_node = False
            if add_node is True:
                self.open_nodes_bfs.insert(0, item)
            else:
                return

        elif self.algorithm == "dfs":
            add_node = True
            for check_node in self.explored_nodes_dfs:
                if item.values == check_node.values:
                    add_node = False
            for check_node in self.open_nodes_dfs:
                if item.values == check_node.values:
                    add_node = False
            if add_node is True:
                self.open_nodes_dfs.append(item)
            else:
                return
        elif self.algorithm == "ast":
            add_node = True
            for check_node in self.explored_nodes_ast:
                if item.values == check_node.values:
                    add_node = False
            for check_node in self.open_nodes_ast:
                if item.values == check_node.values:
                    add_node = False
            if add_node is True:
                heap.heappush(self.open_nodes_ast, item)
            else:
                return

    def get_item(self):
        if self.algorithm == "bfs":
            self.explored_nodes_bfs.add(self.open_nodes_bfs[-1])
            return self.open_nodes_bfs.pop()
        elif self.algorithm == "dfs":
            self.explored_nodes_dfs.add(self.open_nodes_dfs[-1])
            return self.open_nodes_dfs.pop()
        elif self.algorithm == "ast":
            exit_node = heap.heappop(self.open_nodes_ast)
            self.explored_nodes_ast.add(exit_node)
            return exit_node

    def size(self):
        return len(self.open_nodes_bfs)

    def explored_size(self):
        if self.algorithm == "bfs":
            return len(self.explored_nodes_bfs)
        elif self.algorithm == "dfs":
            return len(self.explored_nodes_dfs)
        elif self.algorithm == "ast":
            return len(self.explored_nodes_ast)

    def get_max_depth(self):
        if self.algorithm == "bfs":
            max_depth = 0
            for b in self.explored_nodes_bfs:
                if b.depth > max_depth:
                    max_depth = b.depth
            return max_depth
        elif self.algorithm == "dfs":
            max_depth = 0
            for b in self.explored_nodes_dfs:
                if b.depth > max_depth:
                    max_depth = b.depth
            return max_depth
        elif self.algorithm == "ast":
            max_depth = 0
            for b in self.explored_nodes_ast:
                if b.depth > max_depth:
                    max_depth = b.depth
            return max_depth

#########################################################33
##
##  // Solver Class \\
class Solver:
    def __init__(self, alg, sequence):
        self.goal = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.root = Board(sequence)
        self.nodes_structure = None
        self.algorithm = alg
        self.goal_board = None
        self.goal_depth = None
        self.max_depth = None
        self.nodes_expanded = None


    def solve(self):
        if self.algorithm == "bfs":
            self.nodes_structure = Frontier(self.algorithm)
            self.bfs_search()
        elif self.algorithm == "dfs":
            self.nodes_structure = Frontier(self.algorithm)
            self.dfs_search()
        elif self.algorithm == "ast":
            self.nodes_structure = Frontier(self.algorithm)
            self.ast_search()

    def generate_nodes_bfs(self, node):
        # Generate possible nodes from root state
        # Using Queues: FIFO
        for t in node.tiles:
            if t.value == '0':
                if t.posy > 0:
                    new_node = copy.deepcopy(node)
                    new_node.move_up()
                    new_node.path.append("Up, ")
                    self.nodes_structure.enqueue(new_node)
                if t.posy < 2:
                    new_node = copy.deepcopy(node)
                    new_node.move_down()
                    new_node.path.append("Down, ")
                    self.nodes_structure.enqueue(new_node)
                if t.posx > 0:
                    new_node = copy.deepcopy(node)
                    new_node.move_left()
                    new_node.path.append("Left, ")
                    self.nodes_structure.enqueue(new_node)
                if t.posx < 2:
                    new_node = copy.deepcopy(node)
                    new_node.move_right()
                    new_node.path.append("Right, ")
                    self.nodes_structure.enqueue(new_node)
                return

    def bfs_search(self):
        #self.nodes_queue.isempty()
        self.nodes_structure.enqueue(self.root)
        while len(self.nodes_structure.open_nodes_bfs) > 0:
            print(self.nodes_structure.explored_size())
            current_state = self.nodes_structure.get_item()
            current_state.add_depth()
            if current_state.values == self.goal:
                self.goal_board = current_state
                self.goal_depth = current_state.depth
                self.set_nodes_expanded()
                self.set_max_search_depth()
                return current_state
            self.generate_nodes_bfs(current_state)
        return None

    def generate_nodes_dfs(self, node):
        # Generate possible nodes from root state
        # Using Queues: LIFO
        for t in node.tiles:
            if t.value == '0':
                if t.posy > 0:
                    new_node = copy.deepcopy(node)
                    new_node.move_up()
                    new_node.path.append("Up, ")
                    self.nodes_structure.enqueue(new_node)
                if t.posy < 2:
                    new_node = copy.deepcopy(node)
                    new_node.move_down()
                    new_node.path.append("Down, ")
                    self.nodes_structure.enqueue(new_node)
                if t.posx > 0:
                    new_node = copy.deepcopy(node)
                    new_node.move_left()
                    new_node.path.append("Left, ")
                    self.nodes_structure.enqueue(new_node)
                if t.posx < 2:
                    new_node = copy.deepcopy(node)
                    new_node.move_right()
                    new_node.path.append("Right, ")
                    self.nodes_structure.enqueue(new_node)
                return

    def dfs_search(self):
        self.nodes_structure.enqueue(self.root)
        while len(self.nodes_structure.open_nodes_dfs) > 0:
            current_state = self.nodes_structure.get_item()
            print(self.nodes_structure.explored_size())
            current_state.add_depth()
            if current_state.values == self.goal:
                self.goal_board = current_state
                self.goal_depth = current_state.depth
                self.set_nodes_expanded()
                self.set_max_search_depth()
                return current_state
            self.generate_nodes_dfs(current_state)
        return None

    def generate_nodes_a_star(self, node):
        # Generate possible nodes from root state
        # Using Priority Queues
        for t in node.tiles:
            if t.value == '0':
                if t.posy > 0:
                    new_node = copy.deepcopy(node)
                    new_node.move_up()
                    new_node.path.append("Up")
                    #new_node.get_f_value_misplaced_tiles()
                    new_node.get_f_value_manhattan_distance()
                    self.nodes_structure.enqueue(new_node)
                if t.posy < 2:
                    new_node = copy.deepcopy(node)
                    new_node.move_down()
                    new_node.path.append("Down")
                    #new_node.get_f_value_misplaced_tiles()
                    new_node.get_f_value_manhattan_distance()
                    self.nodes_structure.enqueue(new_node)
                if t.posx > 0:
                    new_node = copy.deepcopy(node)
                    new_node.move_left()
                    new_node.path.append("Left")
                    #new_node.get_f_value_misplaced_tiles()
                    new_node.get_f_value_manhattan_distance()
                    self.nodes_structure.enqueue(new_node)
                if t.posx < 2:
                    new_node = copy.deepcopy(node)
                    new_node.move_right()
                    new_node.path.append("Right")
                    #new_node.get_f_value_misplaced_tiles()
                    new_node.get_f_value_manhattan_distance()
                    self.nodes_structure.enqueue(new_node)
                return

    def ast_search(self):
        self.nodes_structure.enqueue(self.root)
        while len(self.nodes_structure.open_nodes_ast) > 0:
            current_state = self.nodes_structure.get_item()
            #print(self.nodes_structure.explored_size())
            print("f-value: " + str(current_state.f_value))
            current_state.add_depth()
            if current_state.values == self.goal:
                self.goal_board = current_state
                self.goal_depth = current_state.depth
                self.set_nodes_expanded()
                self.set_max_search_depth()
                return current_state
            current_state.increment_g_value()
            self.generate_nodes_a_star(current_state)
        return None

    def set_nodes_expanded(self):
        self.nodes_expanded = self.nodes_structure.explored_size()

    def set_max_search_depth(self):
        self.max_depth = self.nodes_structure.get_max_depth()

#########################################################33
##
##  // Tile Class \\

class Tile:
    def __init__(self, x, y, v):
        self.posx = x
        self.posy = y
        self.value = v
        self.distance_to_goal = None
        self.at_goal = None
        self.correct_tiles = {
                '0' : (0, 0),
                '1' : (1, 0),
                '2' : (2, 0),
                '3' : (0, 1),
                '4' : (1, 1),
                '5' : (2, 1),
                '6' : (0, 2),
                '7' : (1, 2),
                '8' : (2, 2)
            }
        self.calculate_heuristics()

    def calculate_heuristics(self):
        goal_posx = self.correct_tiles[self.value][0]
        goal_posy = self.correct_tiles[self.value][1]
        if goal_posx == self.posx and goal_posy == self.posy:
            self.distance_to_goal = 0
            self.at_goal = True
        else:
            self.at_goal = False
            self.distance_to_goal = (goal_posx - self.posx) + (goal_posy - self.posy)
            if self.distance_to_goal < 0:
                self.distance_to_goal *= -1

#########################################################33
##
##  // Board Class \\

class Board:
    def __init__(self, p):
        self.puzzle = []
        self.tiles = []
        self.values = []
        self.path = []
        self.depth = 0
        self.f_value = None
        self.g_value = 0
        self.h_value = 0
        self.move_actions = []
        s = 1  # Index to insert values from p.
        pattern = re.compile("(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)")
        puzzle = pattern.match(p)
        if puzzle is not None:
            for y in range(0, 3):
                for x in range(0, 3):
                    new_tile = Tile(x, y, puzzle[s])  # Make a new tile
                    s += 1
                    self.tiles.append(new_tile)
            for t in self.tiles:
                self.values.append(t.value)
            print(self.values)
        else:
            raise InputError("Incorrect input format.")

    def __lt__(self, other):
        # this magic-method specifies how the object board will compare itself to similar
        # objects using less than operator, which is how heaps are sorted (and lists).
        return self.f_value < other.f_value

    def get_f_value_misplaced_tiles(self):
        self.h_value = 0
        self.f_value = 0
        for t in self.tiles:
            t.calculate_heuristics()
            if t.at_goal is True:
                self.h_value += 1
        self.f_value = self.h_value + self.g_value

    def get_f_value_manhattan_distance(self):
        self.f_value = 0
        self.h_value = 0
        for t in self.tiles:
            if t.value == 0:
                continue
            t.calculate_heuristics()
            self.h_value += t.distance_to_goal
        self.f_value = self.h_value + self.g_value

    def increment_g_value(self):
        self.g_value += 1

    # Move Functions: Currently using nested for loops, look for a better way.
    # Add check for space tile
    def reinit_values(self):
        self.values = []
        for t in self.tiles:
            self.values.append(t.value)

    def add_depth(self):
        self.depth += 1

    def get_depth(self):
        print("Depth: " + str(self.depth))

    def move_up(self):
        if len(self.tiles) < 9:
            print("Grid is not generated.")
        for t in self.tiles:  # search for 0 tile
            if t.value == '0':
                if t.posy == 0:  # Error if tile is on bottom row
                    print("Error: Space tile cannot go up.")
                    break
                self.move_actions.append(1)
                for new_space in self.tiles:  # Search for tile below it
                    if new_space.posy == t.posy - 1 and new_space.posx == t.posx:
                        t.value = new_space.value  # Swap values
                        new_space.value = '0'  # Move space to new position
                        self.reinit_values()
                        return

    def move_down(self):
        if len(self.tiles) < 9:
            print("Grid is not yet generated.")
        for t in self.tiles:  # search for 0 tile
            if t.value == '0':
                if t.posy == 2:  # Error if tile is on bottom row
                    print("Error: Space tile cannot go down.")
                    break
                self.move_actions.append(3)
                for new_space in self.tiles:  # Search for tile below it
                    if new_space.posy == t.posy + 1 and new_space.posx == t.posx:
                        t.value = new_space.value  # Swap values
                        new_space.value = '0'  # Move space to new position
                        self.reinit_values()
                        return

    def move_right(self):
        if len(self.tiles) < 9:
            print("Grid is not yet generated.")
        for t in self.tiles:  # search for 0 tile
            if t.value == '0':
                if t.posx == 2:  # Error if tile is on bottom row
                    print("Error: Space tile cannot go right.")
                    break
                self.move_actions.append(2)
                for new_space in self.tiles:  # Search for right-side tile
                    if new_space.posx == t.posx + 1 and new_space.posy == t.posy:
                        t.value = new_space.value  # Swap values
                        new_space.value = '0'  # Move space to new position
                        self.reinit_values()
                        return

    def move_left(self):
        if len(self.tiles) < 9:
            print("Grid is not yet generated.")
        for t in self.tiles:  # search for 0 tile
            if t.value == '0':
                if t.posx == 0:  # Error if tile is on bottom row
                    print("Error: Space tile cannot go left.")
                    break
                self.move_actions.append(4)
                for new_space in self.tiles:  # Search for left-side tile
                    if new_space.posx == t.posx - 1 and new_space.posy == t.posy:
                        t.value = new_space.value  # Swap values
                        new_space.value = '0'  # Move space to new position
                        self.reinit_values()
                        return

    def __str__(self):
    # Prints the board in a grid
        return  '+-----+\n'\
                '|' + self.values[0] + '|' + self.values[1] + '|' + self.values[2] + '|' + '\n'\
                '-------\n'\
                '|' + self.values[3] + '|' + self.values[4] + '|' + self.values[5] + '|' + '\n'\
                '-------\n'\
                '|' + self.values[6] + '|' + self.values[7] + '|' + self.values[8] + '|' + '\n'\
                '+-----+\n'\

#########################################################33
##  ::Main:: ##

def main():
    try:
        test_1 = "3 1 2 0 4 5 6 7 8"
        test_2 = "6 1 8 4 0 2 7 3 5"
        test_3 = "8 6 4 2 1 3 5 7 0"
        start_time = time.time()
        #alg = "ast"
        parser = ArgumentParser()
        parser.add_argument("solver", help = "algorithm (bfs, dfs or ast")
        parser.add_argument("board", help = "8 numbers for the board string separated by white space")
        args = parser.parse_args()
        puzzle = Solver(alg = args.solver, sequence = args.board)
        puzzle.solve()
        print(puzzle.goal_board.path)
        print(puzzle.nodes_expanded)

        if puzzle is None:
            print("No solution")
            elapsed_time = time.time() - start_time
            time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

        e = int(time.time() - start_time)

        with open('output.txt', 'w+') as f:
            f.write(f"path_to_goal:     {puzzle.goal_board.path}\n")
            f.write(f"nodes_expanded:   {puzzle.nodes_expanded}\n")
            f.write(f"search_depth:     {puzzle.goal_depth}\n")
            f.write(f"max_search_depth: {puzzle.max_depth}\n")
            f.write(f"running_time:     {'{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60)}\n\n")
            if puzzle.algorithm == "ast":
                puzzle.root.get_f_value_manhattan_distance()
                f.write(f"h-value: {puzzle.root.h_value}, g-value: {puzzle.root.g_value}, f-value: {puzzle.root.f_value}\n")
            f.write(f"{str(puzzle.root)}")
            f.write(f"   |\n")
            f.write(f"   v\n")


            for move in puzzle.goal_board.move_actions:
                if move == 1:
                    puzzle.root.move_up()
                    if puzzle.algorithm == "ast":
                        puzzle.root.get_f_value_manhattan_distance()
                        f.write(f"h-value: {puzzle.root.h_value}, g-value: {puzzle.root.g_value}, f-value: {puzzle.root.f_value}\n")
                    f.write(f"{str(puzzle.root)}")
                    if puzzle.root.values == puzzle.goal:
                        break
                    f.write(f"   |\n")
                    f.write(f"   v\n")
                if move == 2:
                    puzzle.root.move_right()
                    if puzzle.algorithm == "ast":
                        puzzle.root.get_f_value_manhattan_distance()
                        f.write(f"h-value: {puzzle.root.h_value}, g-value: {puzzle.root.g_value}, f-value: {puzzle.root.f_value}\n")
                    f.write(f"{str(puzzle.root)}")
                    if puzzle.root.values == puzzle.goal:
                        break
                    f.write(f"   |\n")
                    f.write(f"   v\n")
                if move == 3:
                    puzzle.root.move_down()
                    if puzzle.algorithm == "ast":
                        puzzle.root.get_f_value_manhattan_distance()
                        f.write(f"h-value: {puzzle.root.h_value}, g-value: {puzzle.root.g_value}, f-value: {puzzle.root.f_value}\n")
                    f.write(f"{str(puzzle.root)}")
                    if puzzle.root.values == puzzle.goal:
                        break
                    f.write(f"   |\n")
                    f.write(f"   v\n")
                if move == 4:
                    puzzle.root.move_left()
                    if puzzle.algorithm == "ast":
                        puzzle.root.get_f_value_manhattan_distance()
                        f.write(f"h-value: {puzzle.root.h_value}, g-value: {puzzle.root.g_value}, f-value: {puzzle.root.f_value}\n")
                    f.write(f"{str(puzzle.root)}")
                    if puzzle.root.values == puzzle.goal:
                        break
                    f.write(f"   |\n")
                    f.write(f"   v\n")

    except TypeError as e:
        print(e)
        exit(1)

    except RuntimeError as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    main()


