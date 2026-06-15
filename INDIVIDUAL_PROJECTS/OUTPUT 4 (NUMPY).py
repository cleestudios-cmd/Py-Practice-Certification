import numpy as np

scores = np.array([72, 85, 90, 61, 78, 95, 55, 88, 74, 82])

mean_score = np.mean(scores)
max_score = np.max(scores)
min_score = np.min(scores)
std_dev_score = np.std(scores)

passing_grade = 75

passed = scores >= passing_grade
failed = scores < passing_grade

pass_count = len(passed)
fail_count = len(failed)

grades = np.select(
    [scores >= 90, scores >= 80, scores >= 70, scores >= 60],
    ['A', 'B', 'C', 'D'],
    default='F'
) 

print(f"Mean Score: {mean_score}")
print(f"Max Score: {max_score}")
print(f"Min Score: {min_score}")
print(f"Standard Deviation: {std_dev_score.round(2)}")
print(f"Number of Passed Students: {pass_count}")
print(f"Number of Failed Students: {fail_count}")
print(f"Grades: {grades}")