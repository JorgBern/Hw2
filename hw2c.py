from copy import deepcopy


def print_matrix(matrix):
    """
    Print a matrix row by row.

    Args:
    - matrix (list): 2D list representing a matrix.
    """
    for row in matrix:
        print(row)


def MakeDiagDom(Aaug):
    """
    Make the matrix diagonally dominant by swapping rows.

    Args:
    - Aaug (list): Augmented matrix.

    Returns:
    - list: Diagonally dominant augmented matrix.
    """
    N = len(Aaug)
    for i in range(N):
        max_val = abs(Aaug[i][i])
        max_row = i
        for k in range(i + 1, N):
            if abs(Aaug[k][i]) > max_val:
                max_val = abs(Aaug[k][i])
                max_row = k

        # Swap rows to make the matrix diagonally dominant
        if max_row != i:
            Aaug[i], Aaug[max_row] = Aaug[max_row], Aaug[i]

    return Aaug


def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of linear equations.

    Args:
    - Aaug (list): Augmented matrix containing coefficients and constants.
    - x (list): Initial guess for the solution.
    - Niter (int): Number of iterations (default is 15).

    Returns:
    - list: Final solution vector.
    """
    N = len(x)

    for _ in range(Niter):
        for i in range(N):
            sum_val = sum(Aaug[i][j] * x[j] for j in range(N) if j != i)
            x[i] = (Aaug[i][-1] - sum_val) / Aaug[i][i]

    return x

def main():
    """
    Main function to demonstrate the Gauss-Seidel method.
    """
    # Set of linear equations
    Aaug_1 = [[3, 1, -1, 2],
              [1, 4, 1, 12],
              [2, 1, 2, 10]]

    Aaug_2 = [[1, -10, 2, 4, 2],
              [3, 1, 4, 12, 12],
              [9, 2, 3, 4, 21],
              [-1, 2, 7, 3, 37]]

    # Initial guess
    x_initial = [0] * (len(Aaug_1[0]) - 1)

    # Make matrices diagonally dominant
    Aaug_1_dom = MakeDiagDom(deepcopy(Aaug_1))
    Aaug_2_dom = MakeDiagDom(deepcopy(Aaug_2))

    print("Diagonally Dominant Aaug_1:")
    print_matrix(Aaug_1_dom)

    print("\nDiagonally Dominant Aaug_2:")
    print_matrix(Aaug_2_dom)

    # Solve and print solutions
    solution_1 = GaussSeidel(deepcopy(Aaug_1_dom), x_initial.copy())
    print("\nSolution 1:", solution_1)

    x_initial_2 = [0] * (len(Aaug_2_dom[0]) - 1)
    solution_2 = GaussSeidel(deepcopy(Aaug_2_dom), x_initial_2.copy())
    print("Solution 2:", solution_2)


if __name__ == "__main__":
    main()
