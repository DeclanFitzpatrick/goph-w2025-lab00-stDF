import numpy as np

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.goph420_lab00.operator import add, multiply, subtract

def main():
    # test for scalars
    print(f'add(1, 3): {add(1, 3)}')
    print(f'multiply(2, 12.): {multiply(2, 12.)}')
    # test for arrays
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = 2. * np.ones(A.shape)
    print(f'A:\n{A}')
    print(f'B:\n{B}')
    print(f'add(A, B):\n{add(A, B)}')
    print(f'multiply(A, B):\n{multiply(A, B)}')
    print(f'Subtraction and multiply: {subtract(A, B)}')


if __name__ == '__main__':
    main()