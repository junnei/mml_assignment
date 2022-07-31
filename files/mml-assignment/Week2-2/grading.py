
import numpy as np
def inversable_matrix_generator(matrix_size, dtype='float'):
    while True:
        if dtype=='int':
            M = np.random.randint(1,1000,[matrix_size, matrix_size])
        elif dtype=='float':
            M = np.random.randn(matrix_size, matrix_size)*10
            
        if np.linalg.det(M) != 0:
            return M

def basis_change_test(func):
    for idx in range(10):
        random_size = np.random.randint(1,100,2)
        A = np.random.randint(1,100,random_size)
        B = np.eye(random_size[1])
        C = np.eye(random_size[0])
        B_tilde = inversable_matrix_generator(random_size[1])
        C_tilde = inversable_matrix_generator(random_size[0])
        
        S = np.dot(B, B_tilde)
        T_inv = np.dot(np.linalg.inv(C_tilde),C)
        A_tilde = np.dot(np.dot(T_inv,A),S)
        
        if (func(A,B_tilde,C_tilde) != A_tilde).any():
            print("Something Wrong. Try again!")
            return False
    print("Success!")
    return True
