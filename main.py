# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum = 0
total_no=0
for i in student_heights:
  sum+=i
  total_no+=1
final = round(sum/total_no)
print(final)




