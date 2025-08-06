for i in range(1, 10):
    print(i)


for i in range(1,100):
    if i%2==0:
        print(i)


for i in range(1,100):
    if i%2!=0:
        print(i)


name = "sravani"
for char in name:
    print(char)


name = input("enter the name: ")
for char in name:
    print(char)


name = "sravani"
for char in name[::-1]:
    print(char)


name = input("enter the name: ")
for char in name[::-1]:
    print(char)


text = input("Enter the text: ")
for char in text:
    print(char)


def reverse_names(*names):
    for name in names[::-1]:
        print(name)
reverse_names("sravani","meena","chinni")


def reverse_names(*names):
    for name in names[::-1]:
        if len(name) % 2 == 0:
            print(name)
reverse_names("sravani","meena","chinni")

text = "my name is sravani and also im 19 years old"
count = 0
for char in text:
    if "o" in char:
        count += 1
print(count)


sentence = "sravani world"
print(sentence.title()) 
print(sentence.replace("world", "life"))


def reverse_names(*names):
    count = 0
    for name in names:
        if len(name) % 2 != 0:
            print(name[::-1])
            count += 1
    print(count)
reverse_names("sravani","srav","pavan","chinni")



def reverse_names(*names):
    count = 0
    for name in names:
        if len(name) % 2 == 0:
            print(name[::-1])
            count += 1
    print(count)
reverse_names("sravani","srav","pavan","chinni")


#vowel count
char = input("Enter a character: ").lower()
count = 0
for c in char:
    if c in "aeiou":
        count += 1
print(count)


#vowels or consonents
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("Vowel")
else:
    print("Consonant")


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

