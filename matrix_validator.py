def is_toeplitz(matrix):
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            if matrix[r][c] != matrix[r + 1][c + 1]:
                return False
    return True

def is_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            if matrix[r][c] != matrix[c][r]:
                return False
    return True

def row_with_max_sum(matrix):
    max_sum = -float('inf')
    max_row_index = -1
    for i, row in enumerate(matrix):
        current_sum = sum(row)
        if current_sum > max_sum:
            max_sum = current_sum
            max_row_index = i
    return max_row_index, max_sum

def rotate_90_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    new_matrix = [[0] * n for _ in range(m)]
    
    for r in range(n):
        for c in range(m):
            new_matrix[c][n - 1 - r] = matrix[r][c]
            
    return new_matrix

if __name__ == "__main__":
    toeplitz_matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    
    symmetric_matrix = [
        [1, 7, 3],
        [7, 4, -5],
        [3, -5, 6]
    ]

    print(f"Is Toeplitz: {is_toeplitz(toeplitz_matrix)}")
    print(f"Is Symmetric: {is_symmetric(symmetric_matrix)}")
    
    row_idx, row_sum = row_with_max_sum(toeplitz_matrix)
    print(f"Row with Max Sum: Index {row_idx}, Sum {row_sum}")
    
    print("Original Matrix (Symmetric):")
    for row in symmetric_matrix: print(row)
    
    print("Rotated 90 Clockwise:")
    rotated = rotate_90_clockwise(symmetric_matrix)
    for row in rotated: print(row)
