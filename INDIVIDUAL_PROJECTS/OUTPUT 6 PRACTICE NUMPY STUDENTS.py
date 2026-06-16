import numpy as np

names   = np.array(["James","Sofia","Carlos","Alyssa","Ryan","Maria","Derek","Nicole","Miguel","Jessica"])
sections= np.array(["A","A","A","A","A","B","B","B","B","B"])
genders = np.array(["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"])
heights = np.array([172, 158, 168, 162, 175, 155, 170, 160, 165, 157])
weights = np.array([68, 52, 72, 55, 80, 48, 74, 54, 69, 50])
code = np.array(["S001","S002","S003","S004","S005","S006","S007","S008","S009","S010"])

bmi = np.round(weights / (heights / 100) ** 2, 2)
mean_bmi = np.round(np.mean(bmi), 2)


students_data = np.array([names, sections, genders, bmi, code])
while True:
    info = input('Enter the Student Code: ')
    if info in code:
        index = np.where(code == info)[0][0]
        print(f"Name: {names[index]}")
        print(f"Section: {sections[index]}")
        print(f"Gender: {genders[index]}")
        print(f"BMI: {bmi[index]}")
    else:
        print("Student not found.")
        continue

    find_mean = input('Do you want to find the mean BMI of all students? (yes/no): ')
    if find_mean.lower() == 'yes':
        print(f"Mean BMI: {mean_bmi}")
        break
    else:
        break