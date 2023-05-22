class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solution = []

    def is_safe(self, row, col):
        # Check if no queen is present in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check if no queen is present in the upper-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check if no queen is present in the upper-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve_nqueens(self, row):
        if row == self.n:
            # Found a solution, add it to the list of solutions
            current_solution = []
            for i in range(self.n):
                queen_col = self.board[i].index(1)
                current_solution.append((i, queen_col))
            self.solution.append(current_solution)
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1

                if self.solve_nqueens(row + 1):
                    return True

                self.board[row][col] = 0

        return False

    def solve(self):
        if self.solve_nqueens(0):
            return self.solution[0]
        else:
            return []


# Take input from the user
n = int(input("Enter the number of queens (n): "))

# Create an instance of NQueens class and solve the problem
nqueens = NQueens(n)
solution = nqueens.solve()

# Print the solution
if solution:
    print("Solution:")
    for i, j in solution:
        row = "." * j + "Q" + "." * (n - j - 1)
        print(row)
else:
    print("No solution exists for the given number of queens.")
