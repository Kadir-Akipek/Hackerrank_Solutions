def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] > 37 and grades[i] % 5 != 0 and (grades[i] % 5) > 2:
            grades[i] += 5 - (grades[i] % 5)
    
    return grades