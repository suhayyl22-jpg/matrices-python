import numpy as np

print("=== ESCALAR DE MATRICES ===")
A = np.array([[1, 2], [3, 4]])
print("1:", 2 * A)

B = np.array([[0, -1], [5, 3]])
print("2:", 3 * B)

C = np.array([[2, 2], [2, 2]])
print("3:", -1 * C)

print("\n=== SUMA DE MATRICES ===")
A1 = np.array([[1, 2], [3, 4]])
B1 = np.array([[5, 6], [7, 8]])
print("4:", A1 + B1)

A2 = np.array([[2, 0], [1, 3]])
B2 = np.array([[4, 1], [2, 2]])
print("5:", A2 + B2)

A3 = np.array([[0, 0], [0, 0]])
B3 = np.array([[1, 1], [1, 1]])
print("6:", A3 + B3)

print("\n=== RESTA DE MATRICES ===")
print("7:", A1 - B1)
print("8:", A2 - B2)
print("9:", A3 - B3)
