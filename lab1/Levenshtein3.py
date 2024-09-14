common_words = ["the", "of", "and", "be", "this", "this", "there", "and", "been", "some"]

def levenshtein(a, b, ignore_words_list):
    # imports
    import numpy as np

    # check length of strings/lists
    m, n = len(a), len(b)

    # Make a matrix of size (m+1 x n+1)
    lev = np.zeros((m+1, n+1), int)

    # Fill the first row and first column
    for i in range(m+1):
        lev[i, 0] = i
    for j in range(n+1):
        lev[0, j] = j

    # Caclulate edit distance using matrix
    for i in range (1, m+1):
        for j in range (1, n+1):

            insert = lev[i-1, j] + 1
            delete = lev[i, j-1] + 1

            ### MOFIFIED STATEMENT: (Added a condition which results in ignoring the words present in the "ignore_words_list" list)
            substitute = lev[i-1, j-1] + (0 if a[i-1] == b[j-1] or a[i-1]  in ignore_words_list or b[j-1] in ignore_words_list else 1)
            
            # Find min of the three
            minimum = min(insert, delete, substitute)

            # Fill matrix[i, j] with mimimum
            lev[i, j] = minimum

    # print the matrix
    for i in range(m+1):
        for j in range(n+1):
            print(f"{lev[i, j]:2}", end = " ")
        print()

    return lev[i, j]
        
# A function to read file   
def read_file(path):
    with open(path, 'r') as file:
        return file.readline().strip().split()
    
# A function to write to file
def write_file(path, distance):
    with open(path, 'w') as file:
        file.write(f"Levenshtein Distance: {distance}")

# Read strings from file
string_1 = read_file("reference.txt")
string_2 = read_file("hypothesis.txt")

# Calculate edit distance
distance = levenshtein(string_1, string_2, common_words)

# Write to file and print the distance
write_file("result2.txt", distance)
print("Writing data to file 'result2.txt'")
print("Levenshtein Distance:", distance)



