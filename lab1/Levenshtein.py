def levenshtein(a, b):

    m, n = len(a), len(b)

    matrix = [[0] * (n+1) for i in range(m+1)]

    for i in range(m+1):
      matrix[i][0] = i
    for j in range(n+1):
      matrix[0][j] = j

    for i in range(1, m+1):
      for j in range(1, n+1):
        if (min(i,j) == 0):
          matrix[i][j] = max(i,j)
        else:
          insert = matrix[i-1][j] + 1
          delete = matrix[i][j-1] + 1
          substitute = matrix[i-1][j-1] + (1 if a[i-1] != b[j-1] else 0)
          matrix[i][j] = min(insert, delete, substitute)

    for i in range(n+1):
        for j in range(m+1):
            print(matrix[j][i], end = " ")
        print()

    return matrix[m][n]
    

a = input("Enter string 1: ")
b = input("Enter string 2: ")

distance = levenshtein(a, b)

print(f"\nDistance: {distance}")
