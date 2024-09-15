def levenshtein(a, b):

    # Get the lnghts of the strings
    m, n = len(a), len(b)

    # Create a matrix of size (m+1 x n+1)
    matrix = [[0] * (n+1) for i in range(m+1)]
    # Create a matrix for counting operations
    operations = [[(0, 0, 0)] * (n+1) for i in range(m+1)]

    # Fill the first row and column of the matrix from 1 to m and n 
    for i in range(m+1):
      matrix[i][0] = i
      operations[i][0] = (i, 0, 0) # Deletions
    for j in range(n+1):
      matrix[0][j] = j
      operations[0][j] = (0, j, 0) # Insertions

    insertions, deletions, substitutions = 0, 0, 0

    # Fill in the matrix (dynamic programming)
    for i in range(1, m+1):
      for j in range(1, n+1):
        delete = matrix[i-1][j] + 1
        insert = matrix[i][j-1] + 1
        substitute = matrix[i-1][j-1] + (1 if a[i-1] != b[j-1] else 0)
        # Choose minimum of the three
        minimum = min(insert, delete, substitute)
        matrix[i][j] = minimum

        if minimum ==  delete:
          operations[i][j] = (operations[i-1][j][0] + 1, operations[i-1][j][1], operations[i-1][j][2])
        elif minimum == insert:
          operations[i][j] = (operations[i][j-1][0], operations[i][j-1][1] + 1, operations[i][j-1][2])
        else:
          operations[i][j] = (operations[i-1][j-1][0], operations[i-1][j-1][1], operations[i-1][j-1][2] + (1 if a[i-1] != b[j-1] else 0))

    # Print the matrix
    for i in range(m+1):
        for j in range(n+1):
            print(matrix[i][j], end = " ")
        print()

    deletions, insertions, substitutions = operations[m][n]

    return matrix[m][n], insertions, deletions, substitutions
    
# input strings and print distance
a = input("Enter string 1: ")
b = input("Enter string 2: ")

# Calculate the edit distance and print it
distance, insertions, deletions, substitutions = levenshtein(a, b)
print(f"\nEdit Distance: {distance}\n\nInsertions: {insertions}\nDeletions: {deletions}\nSubstitutions: {substitutions}")
