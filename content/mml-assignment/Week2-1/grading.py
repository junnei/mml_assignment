import numpy as np

def grade_matrix_addition(func):
    for idx in range(100):
        x = np.random.randint(100)
        y = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, y))
        B = np.random.randint(-100,100,size=(x, y))
        if func(A,B)!=A+B:
            return False
    return True
    