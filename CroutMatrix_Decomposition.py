import numpy as np

def crout(A: np.ndarray):
    n = A.shape[0]  
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for k in range(n):
        U[k, k] = 1  

        for i in range(k, n):
            sum0 = sum(L[i, s] * U[s, k] for s in range(k))  # Correct index ranges
            L[i, k] = A[i, k] - sum0

        for j in range(k+1, n):
            sum1 = sum(L[k, s] * U[s, j] for s in range(k))  # Correct index ranges
            if L[k, k] != 0:
                U[k, j] = (A[k, j] - sum1) / L[k, k]

    print("L =\n", L, "\nU =\n", U)
    return L, U

# Example usage
A = np.array([[35.0, 24.0, 18.0], [9.0, 45.0, 15.0], [21.0, 37.0, 12.0]])
L, U = crout(A)
