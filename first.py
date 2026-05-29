# Python program to swap two variables
x = 5
y = 10

temp = x
x = y
y = temp

print(x)
print(y)


# Python program to find area of circle
radius=int(input("Enter radius:"))
area=3.14*radius**2
print(area)

# Python program of 5 arithmic expression

exp1 = 5 + 3 * 2

exp2 = (10 - 4) / 2

exp3 = 7**2 + 6

exp4 = 15 / 3 + 8 * 2

exp5 = (9 + 1) * (5 - 2)

print(exp1, exp2, exp3, exp4, exp5)

num=int(input("Enter a number:"))
# python program to find even or odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Python program of grade calculator

marks = int(input("Enter your marks : "))

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F (Fail)")
