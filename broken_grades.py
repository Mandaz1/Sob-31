# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # added int() before input by muhammad bagosher

exam_three = int(input("Input exam grade three: ")) #changed exam_3 to exam three, and str to int by muhammad bagosher

grades = [exam_one , exam_two , exam_three] #added comas between list components by muhammad bagosher 
sum = 0
for grade in grades: #changed grade to grades by muhammad bagosher
  sum = sum + grade

avg = round(sum / len(grades)) #changed grdes to grades, and rounded the answer by muhammad bagosher

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #added : at the end of elif statement by muhammad bagosher
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #changed ' to " by muhammad bagosher
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: #changed elif to else by muhammad bagosher
    letter_grade = "F"

#for grade in grades: #removed for loop by muhammad bagosher
print("Exams:", end=' ') #changed the print function from inside the loop to a normal print function that doesnt add a line in the end , by muhammad bagosher
print(*grades, sep = ",") #added a print function that prints out the grades list while removing the brackets and separating them by a coma, by muhammad bagosher
# removed 2 print functions from the for loop by muhammad bagosher
print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F": # changed (-) to (_) and (is) to (==) in variable letter_grade by muhammad bagosher
    print ("Student is failing.") #added paranthesis to print statement by muhammad bagosher
else:
    print ("Student is passing.") #added paranthesis to print statement by muhammad bagosher
