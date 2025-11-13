studentNumber= int(input("enter the user number:"))

allUser=[]

for i in range(studentNumber):
    name = input("enter your name:")
    studyNumber = int(input("enter count of study: "))
    userGrades=[]
    for j in range(studyNumber):
        corseScore = int(input(f"enter the study {j+1} score"))
        userGrades.append(corseScore)
    userItem ={
        'studentId':i+1 ,
        'name':name,
        'grades':userGrades
    }
    allUser.append(userItem)
def calcUserGpa(user):
    total = sum(user['grades'])
    gpa = total / len(user['grades'])
    print(f"{user['name']} has GPA: {gpa:.2f}")

    
for user in allUser:
    calcUserGpa(user)
   
