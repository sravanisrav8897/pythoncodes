
num=80
if num%2==0:
    print("Even number")



num=9
if num%2==0:
    print("Even number")
else:
    print("Odd number")
    
    
x = 5
if x > 0:
    if x < 10:
        print("Between 1 and 9")


age = 20
if age >= 18:
    print("You can vote.")
else:
    print("You are not eligible to vote.")
    
    

marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    
    

n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")


marks = int(input("Enter marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
else:
    print("Fail")


a = 5
b = 9
c = 3
if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")

#leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
    
#vowels or consonents
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#vowel count
char = input("Enter a character: ").lower()
count = 0
for c in char:
    if c in "aeiou":
        count += 1
print(count)


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number ")
            break
    else:
        print(" prime number")
else:
    print(" not a prime number")


for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
