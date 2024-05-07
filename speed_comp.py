import numpy as np
from sigmulib import compute_sigmul

print("Imported packages")

# Create a sample matrix A (as a NumPy array)
A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0],
              [7.0, 8.0, 9.0]])

print("Created A")

# Call the sigmul function to apply the operation
result = compute_sigmul(A.tolist())  # Convert A to a Python list before passing to sigmul

# Print the result
print(result)

print(np.allclose(result, (A / (1 + np.exp(-A)))))
