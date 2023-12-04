import math

def matrix_definer(matrix, rows, columns):
    print("We will now begin filling the matrix, row by row (including the constants column).")
    for i in range(rows):
        for j in range(columns):
            value = float(input(f"Please enter a value for row {i + 1}, column {j + 1}: "))
            matrix[i][j] = value
        if i < rows - 1:
            print("Moving to the next row")

def matrix_print(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end="\t")
        print()

def gauss_elimination(matrix):
    n = len(matrix)
    solutions = [0] * n

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    for i in range(n - 1, -1, -1):
        sum_val = sum(matrix[i][j] * solutions[j] for j in range(i + 1, n))
        solutions[i] = (matrix[i][n] - sum_val) / matrix[i][i]

    return solutions

def gauss_jordan_elimination(matrix):
    n = len(matrix)
    solutions = [0] * n

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        pivot_val = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot_val

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i):
            ratio = matrix[j][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    solutions = [matrix[i][n] for i in range(n)]

    return solutions

def main():
    eq = int(input("Please enter the number of equations in your system: "))
    matrix = [[0] * (eq + 1) for _ in range(eq)]

    matrix_definer(matrix, eq, eq + 1)
    matrix_print(matrix, eq, eq + 1)

    solutions_gauss = gauss_elimination(matrix)
    print("\nSolutions using Gauss elimination:")
    for i, solution in enumerate(solutions_gauss):
        print(f"x{i + 1} = {solution}")

    solutions_gauss_jordan = gauss_jordan_elimination(matrix)
    print("\nSolutions using Gauss-Jordan elimination:")
    for i, solution in enumerate(solutions_gauss_jordan):
        print(f"x{i + 1} = {solution}")

if __name__ == "__main__":
    main()
