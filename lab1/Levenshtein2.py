# Edit distance Function
def levenshtein(a, b):

  # Lenghts of strings a and b
  m, n = len(a), len(b)

  # Make a matrix of shape (m x n)
  matrix = [[0] * (n+1) for i in range(m+1)]
  # Create a matrix for counting operations
  operations = [[(0, 0, 0)] * (n+1) for i in range(m+1)]

  for i in range(m+1):
    matrix[i][0] = i
    operations[i][0] = (i, 0, 0) # Deletions
  for j in range(n+1):
    matrix[0][j] = j
    operations[0][j] = (0, j, 0) # Insertions

  # Fill the matrix
  for i in range(1, m+1):
    for j in range(1, n+1):
      delete = matrix[i-1][j] + 1
      insert = matrix[i][j-1] + 1
      substitute = matrix[i-1][j-1] + (1 if a[i-1] != b[j-1] else 0)

      # Find min of the three
      minimum = min(insert, delete, substitute)

      # Fill matrix[i, j] with mimimum
      matrix[i][j] = minimum

      if minimum ==  delete:
        operations[i][j] = (operations[i-1][j][0] + 1, operations[i-1][j][1], operations[i-1][j][2])
      elif minimum == insert:
        operations[i][j] = (operations[i][j-1][0], operations[i][j-1][1] + 1, operations[i][j-1][2])
      else:
        operations[i][j] = (operations[i-1][j-1][0], operations[i-1][j-1][1], operations[i-1][j-1][2] + (1 if a[i-1] != b[j-1] else 0))

  for i in range(m+1):
      for j in range(n+1):
          print(f"{matrix[i][j]:2}", end = " ")
      print()

  deletions, insertions, substitutions = operations[m][n]

  return matrix[m][n], insertions, deletions, substitutions

# function to Read file
def read_file(path):
  with open(path, 'r') as file:
    return file.readline().strip().split()

# function to Write to file
def write_file(path, distance, insertions, deletions, substitutions):
  with open(path, 'w') as file:
    file.write(f"\nLevenshtein Distance: {distance}\n\nInsertions: {insertions}\nDeletions: {deletions}\nSubstitutions: {substitutions}")

# Read the files
reference = read_file("reference.txt")
hypothesis = read_file("hypothesis.txt")

distance, insertions, deletions, substitutions = levenshtein(reference, hypothesis)

write_file("result.txt", distance, insertions, deletions, substitutions)
print("Writing to file (result.txt)...")
print(f"Levenshtein Distance: {distance}")