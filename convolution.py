import numpy as np

# Define the input matrix (image)
input_matrix = np.array([[1, 2, 3, 4, 5, 6],
                         [7, 8, 9, 10, 11, 12],
                         [13, 14, 15, 16, 17, 18],
                         [19, 20, 21, 22, 23, 24],
                         [25, 26, 27, 28, 29, 30],
                         [31, 32, 33, 34, 35, 36]])

# Define the filter (kernel)
filter_matrix = np.array([[1, 0, -1],
                          [2, 0, -2],
                          [1, 0, -1]])

# Perform convolution
def convolution(input_matrix, filter_matrix):
    input_rows, input_cols = input_matrix.shape
    filter_rows, filter_cols = filter_matrix.shape
    output_rows = input_rows - filter_rows + 1
    output_cols = input_cols - filter_cols + 1
    output_matrix = np.zeros((output_rows, output_cols))
    
    for i in range(output_rows):
        for j in range(output_cols):
            output_matrix[i, j] = np.sum(input_matrix[i:i+filter_rows, j:j+filter_cols] * filter_matrix)
    
    return output_matrix

# Perform convolution
convoluted_matrix = convolution(input_matrix, filter_matrix)

# Display the result
print("Input Matrix (Image):")
print(input_matrix)
print("\nFilter (Kernel):")
print(filter_matrix)
print("\nResulting Convolved Matrix:")
print(convoluted_matrix)
