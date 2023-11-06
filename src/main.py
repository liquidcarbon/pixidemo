import ctypes

# Load the shared library (replace with the appropriate extension on Windows, e.g., .dll)
mylib = ctypes.CDLL("src/mylib.so")

# Call the C functions
mylib.hello_from_c()
result = mylib.add_numbers(3, 5)
print("Result from C function:", result)

# Some NumPy
import numpy as np
a = np.random.randint(100, size=(3,3), dtype=np.uint8)
print("a numpy matrix:\n", a)
