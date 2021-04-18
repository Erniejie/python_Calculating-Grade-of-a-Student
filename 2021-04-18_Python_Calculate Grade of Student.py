#2021-04-18_Python_ Calculate Grade of Student
"Computer Programmming Tutor, March18,2021"

print("Enter Scores Achieved in 5 Subjects:")

m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

Total = m1 + m2 + m3 + m4 + m5
avg = Total/5

if avg >= 91 and avg <=100:
    print("Grade is A1")

elif avg >=81 and avg<91:
    print("Grade is B2")

elif avg>=71 and avg<81:
    print("Grade is B3")


elif avg >=61 and avg<71:
    print("Grade is C4")

elif avg>=51 and avg<61:
    print("Grade is C5")

#---
elif avg>=41 and avg<51:
    print("Grade is C6")


elif avg >=33 and avg<41:
    print("Grade is D7")

elif avg>=21 and avg<33:
    print("Grade is E8")

elif avg>=0 and avg<21:
    print("Grade is F9")

else:
    print("Invalid Input!!!")



    
