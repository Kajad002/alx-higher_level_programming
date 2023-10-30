import sys

def solve_n_queens(n):
    """
    Solve the N queens problem using backtracking.

    Parameters:
    n (int): The number of queens and the size of the chess board.

    Returns:
    None
    """

    def can_place(board, row, col):
        """
        Check if a queen can be placed at board[row][col].

        Parameters:
        board (list): The chess board.
        row (int): The row index.
        col (int): The column index.

        Returns:
        bool: True if a queen can be placed at board[row][col], False otherwise.
        """
        for i in range(col):
            if board[i] == row or \
                    board[i] - i == row - col or \
                    board[i] + i == row + col:
                        return False
        return True

    def place_queens(board, col, n):
        """
        Place queens on the chess board.

        Parameters:
        board (list): The chess board.
        col (int): The column index.
        n (int): The number of queens and the size of the chess board.

        Returns:
        None
        """
        if col == n:
            result = []
            for i in range(n):
                result.append([i, board[i]])
            print(result)
            return

        for row in range(n):
            if can_place(board, row, col):
                board[col] = row
                place_queens(board, col + 1, n)

    # Initialize the chess board.
    board = [-1] * n
    # Start placing queens.
    place_queens(board, 0, n)

def main():
    """
    The main function of the program. It checks command line arguments and solves
    the N queens problem.

    Returns:
    None
    """

    # Check command line arguments.
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem.
    solve_n_queens(n)

if __name__ == "__main__":
    main()
