# Edit distance Function
def levenshtein(a, b):

    # Lenghts of strings a and b
    m, n = len(a), len(b)

    # Make a matrix of shape (m x n)
    matrix = [[0] * (n+1) for i in range(m+1)]

    # Initialize the first column (1 to m)
    for i in range(m+1):
      matrix[i][0] = i
    # Initialize the first row (1 to n)
    for j in range(n+1):
      matrix[0][j] = j

    # Fill the matrix
    for i in range(1, m+1):
      for j in range(1, n+1):
        insert = matrix[i-1][j] + 1
        delete = matrix[i][j-1] + 1
        substitute = matrix[i-1][j-1] + (1 if a[i-1] != b[j-1] else 0)

        # Find min of the three
        minimum = min(insert, delete, substitute)

        # Fill matrix[i, j] with mimimum
        matrix[i][j] = minimum

    for i in range(m+1):
        for j in range(n+1):
            print(f"{matrix[i][j]:2}", end = " ")
        print()

    return matrix[m][n]

# function to Read file
def read_file(path):
    with open(path, 'r') as file:
        return file.readline().strip().split()

# function to Write to file
def write_file(path, distance):
    with open(path, 'w') as file:
        file.write(f"Levenshtein Distance: {distance}")

# Read the files
reference = read_file("reference.txt")
hypothesis = read_file("hypothesis.txt")

distance = levenshtein(reference, hypothesis)

write_file("result.txt", distance)
print("Writing to file (result.txt)...")
print(f"Levenshtein Distance: {distance}")