def levenshtein(a, b):

    # Get the lnghts of the strings
    m, n = len(a), len(b)

    # Create a matrix of size (m+1 x n+1)
    matrix = [[0] * (n+1) for i in range(m+1)]

    # Fill the first row and column of the matrix from 1 to m and n 
    for i in range(m+1):
      matrix[i][0] = i
    for j in range(n+1):
      matrix[0][j] = j

    # Fill in the matrix (dynamic programming)
    for i in range(1, m+1):
      for j in range(1, n+1):
        insert = matrix[i-1][j] + 1
        delete = matrix[i][j-1] + 1
        substitute = matrix[i-1][j-1] + (1 if a[i-1] != b[j-1] else 0)
        # Choose minimum of the three
        matrix[i][j] = min(insert, delete, substitute)

    # Print the matrix
    for i in range(m+1):
        for j in range(n+1):
            print(matrix[i][j], end = " ")
        print()

    return matrix[m][n]
    
# input strings and print distance
a = input("Enter string 1: ")
b = input("Enter string 2: ")

# Calculate the edit distance and print it
distance = levenshtein(a, b)
print(f"\nEdit Distance: {distance}")
