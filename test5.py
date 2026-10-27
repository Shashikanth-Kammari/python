import numpy as n

a = n.array([1.0, 2.0, 3.0])
b = n.array([4.0, 5.0, 6.0])
print(a + b)            # [5. 7. 9.]  element by element
print(a @ b)            # 32.0        dot product
m = n.arange(6).reshape(2, 3)
print(m.shape, m.mean(axis=0))