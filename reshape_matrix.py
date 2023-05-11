def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    if r*c != len(matrix)*len(matrix[0]):
        return matrix
    else:
        new_matrix = [[0 for column in range(c)] for row in range(r)]
    
    i = 0
    j = 0
    for x in matrix:
        for y in x:
            new_matrix[i][j] = y
            if j < c-1:
                j += 1
            elif i < r-1:
                i += 1
                j = 0
        
    return new_matrix