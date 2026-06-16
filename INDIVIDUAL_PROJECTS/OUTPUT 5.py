import numpy as np

height = np.array([150, 160, 170, 180, 190])
weight = np.array([60, 62, 64, 68, 70])

bmi = weight / (height / 100) ** 2

print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"BMI: {bmi.round(2)}")