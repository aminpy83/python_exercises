student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for val in student_scores:
    score = student_scores[val]
    if student_scores[val] >= 91:
        student_grades[val] = "outstanding"
    if student_scores[val] >= 81 and student_scores[val] <= 90:
        student_grades[val] = "exceeds"
    if student_scores[val] >= 71 and student_scores[val] <= 80:
        student_grades[val] = "acceptable"
    if student_scores[val] <= 70:
        student_grades[val] = "fail"    

# 🚨 Don't change the code below 👇
print(student_grades)