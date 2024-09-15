common_words = ["the", "of", "and", "be", "this", "there", "been", "some"]

def levenshtein(a, b, ignore_words_list):
    # imports
    import numpy as np

    # check length of strings/lists
    m, n = len(a), len(b)

    # Make a matrix of size (m+1 x n+1)
    lev = np.zeros((m+1, n+1), int)
    # Create a matrix for counting operations
    operations = [[(0, 0, 0)] * (n+1) for i in range(m+1)]

    # Fill the first row and first column
    for i in range(m+1):
        lev[i, 0] = i
        operations[i][0] = (i, 0, 0) # Deletions
    for j in range(n+1):
        lev[0, j] = j
        operations[0][j] = (0, j, 0) # Deletions

    # Caclulate edit distance using matrix
    for i in range (1, m+1):
        for j in range (1, n+1):

            delete = lev[i-1, j] + 1
            insert = lev[i, j-1] + 1

            ### MOFIFIED STATEMENT: (Added a condition which results in ignoring the words present in the "ignore_words_list" list)
            substitute = lev[i-1, j-1] + (0 if a[i-1] == b[j-1] or a[i-1]  in ignore_words_list or b[j-1] in ignore_words_list else 1)
            
            # Find min of the three
            minimum = min(insert, delete, substitute)

            # Fill matrix[i, j] with mimimum
            lev[i, j] = minimum

            if minimum ==  delete:
                operations[i][j] = (operations[i-1][j][0] + 1, operations[i-1][j][1], operations[i-1][j][2])
            elif minimum == insert:
                operations[i][j] = (operations[i][j-1][0], operations[i][j-1][1] + 1, operations[i][j-1][2])
            else:
                operations[i][j] = (operations[i-1][j-1][0], operations[i-1][j-1][1], operations[i-1][j-1][2] + (0 if a[i-1] == b[j-1] or a[i-1]  in ignore_words_list or b[j-1] in ignore_words_list else 1))


    # print the matrix
    for i in range(m+1):
        for j in range(n+1):
            print(f"{lev[i, j]:2}", end = " ")
        print()

    deletions, insertions, substitutions = operations[m][n]

    return lev[m, n], insertions, deletions, substitutions
        
# A function to read file   
def read_file(path):
    with open(path, 'r') as file:
        return file.readline().strip().split()
    
# A function to write to file
def write_file(path, distance, insertions, deletions, substitutions):
    with open(path, 'w') as file:
        file.write(f"\nLevenshtein Distance: {distance}\n\nInsertions: {insertions}\nDeletions: {deletions}\nSubstitutions: {substitutions}")

# Read strings from file
string_1 = read_file("reference.txt")
string_2 = read_file("hypothesis.txt")

# Calculate edit distance
distance, insertions, deletions, substitutions = levenshtein(string_1, string_2, common_words)

# Write to file and print the distance
write_file("result2.txt", distance, insertions, deletions, substitutions)
print("Writing data to file 'result2.txt'")
print("Levenshtein Distance:", distance)



