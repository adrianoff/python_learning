import numpy as np

arr1 = np.array([[1, 1], [0, 1]])
arr1_transpose = arr1.transpose()
print(f'Transposed Array:\n{np.matmul(arr1_transpose, arr1)}')


arr1 = np.array([[1/2, 1/2], [-1/2, 1/2]])
arr1_transpose = arr1.transpose()
print(f'Transposed Array:\n{np.matmul(arr1_transpose, arr1)}')


arr1 = np.array([[-1, 0], [0, 1]])
arr1_transpose = arr1.transpose()
print(f'Transposed Array:\n{np.matmul(arr1_transpose, arr1)}')


arr1 = np.array([[3/5, 4/5, 0], [-4/5, 3/5, 0], [0, 0, 1]])
arr1_transpose = arr1.transpose()
print(f'Transposed Array:\n{np.matmul(arr1_transpose, arr1)}')
