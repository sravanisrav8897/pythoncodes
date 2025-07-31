count = 1
while count <= 10:
    print(count)
    count += 1


count = 10
while count >= 1:
    print(count)
    count -= 1


#print even numbers between 0 and 100
count = 0
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1


#print odd numbers between 0 and 100
count = 0
while count <= 100:
    if count % 2 != 0:
        print(count)
    count += 1


count = 0
while count <= 100:
    if count % 3 == 0:
        print(count)
    count += 1


count = 0
while count <= 100:
    if count % 3 != 0:
        print(count)
    count += 1

count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("loop end")

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  
    if i == 8:
        break  
    print(i)


count = 1
while count <= 10:
    if count == 5:
        print("Breaking at 5")
        break
    print(count)
    count += 1


while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        print("Valid number.")
        break
    print("Try again.")


