import heapq


class PuzzleState:
    def __init__(self, puzzle, goal, cost=0, parent=None):
        self.puzzle = puzzle
        self.goal = goal
        self.cost = cost
        self.parent = parent
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.puzzle[i][j]
                if value != 0:
                    goal_position = divmod(value - 1, 3)
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return distance

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic


def get_neighbors(state):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for direction in directions:
        new_puzzle = [row[:] for row in state.puzzle]
        zero_pos = find_zero_position(new_puzzle)

        new_pos = (zero_pos[0] + direction[0], zero_pos[1] + direction[1])

        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_puzzle[zero_pos[0]][zero_pos[1]] = new_puzzle[new_pos[0]][new_pos[1]]
            new_puzzle[new_pos[0]][new_pos[1]] = 0
            neighbors.append(PuzzleState(new_puzzle, state.goal, state.cost + 1, state))

    return neighbors


def find_zero_position(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j


def reconstruct_path(node):
    path = []
    current_node = node
    while current_node:
        path.append(current_node.puzzle)
        current_node = current_node.parent
    return list(reversed(path))


def a_star_search(initial_state, goal_state):
    open_list = []
    closed_set = set()

    start_node = PuzzleState(initial_state, goal_state)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.puzzle == goal_state:
            return reconstruct_path(current_node)

        closed_set.add(tuple(map(tuple, current_node.puzzle)))

        for neighbor in get_neighbors(current_node):
            if tuple(map(tuple, neighbor.puzzle)) in closed_set:
                continue

            heapq.heappush(open_list, neighbor)

    return None


# Example usage:

# Prompt the user to enter the initial and goal states
initial_state = []
goal_state = []

print("Enter the initial state (9 numbers from 0 to 8, representing the puzzle configuration):")
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

print("Enter the goal state (9 numbers from 0 to 8, representing the puzzle configuration):")
for _ in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

# Run the A* algorithm for the 8-puzzle problem
path = a_star_search(initial_state, goal_state)

# Print the resulting path
if path:
    print("Path found:")
    for state in path:
        for row in state:
            print(row)
        print()
else:
    print("Path not found.")
