import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])
print(a + b)            # [5. 7. 9.]  element by element
print(a @ b)            # 32.0        dot product
m = np.arange(6).reshape(2, 3)
print(m.shape, m.mean(axis=0))