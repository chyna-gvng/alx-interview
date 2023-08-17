def rotate_2d_matrix(matrix):
    """
        function that rotates a 2D matrix 90 degrees clockwise.

        Args:
            matrix: The 2D matrix to rotate.

        Return: Rotated matrix
    """

    n = len(matrix)

    for layer in range(n // 2):
        for i in range(layer, n - layer - 1):
            top = matrix[layer][i]
            bottom = matrix[n - layer - 1][i]
            left = matrix[i][n - layer - 1]
            right = matrix[i][layer]

            matrix[layer][i] = left
            matrix[n - layer - 1][i] = top
            matrix[i][n - layer - 1] = right
            matrix[i][layer] = bottom
