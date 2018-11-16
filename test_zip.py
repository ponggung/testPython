# method 1
import numpy as np
list_a = np.array([0, 1, 2, 3, 4])
list_b = np.array([0, 1, 2, 3, 4])
list_c = np.array([0, 1, 2, 3, 4])
result = (list_a * list_b)**list_c
print(result)

# method 2
list_a = [0, 1, 2, 3, 4]
list_b = [0, 1, 2, 3, 4]
list_c = [0, 1, 2, 3, 4]
result = [(a * b)**c for a, b, c in zip(list_a, list_b, list_c)]
print(result)
