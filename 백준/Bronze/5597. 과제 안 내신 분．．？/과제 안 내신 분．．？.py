import sys

student = list(i for i in range(1, 31))
for i in range(28):
    submit = int(sys.stdin.readline().rstrip())
    student.remove(submit)
    
student.sort()
print(student[0])
print(student[1])