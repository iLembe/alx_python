def print_matrix_integer(matrix=[[]]):\n    for row in matrix:\n        for i in range(len(row)):\n            if i != len(row) - 1:\n                print("{:d}".format(row[i]), end=" ")\n            else:\n                print("{:d}".format(row[i]), end="")\n        print()\n\n# Example usage:\nmatrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nprint_matrix_integer(matrix)
