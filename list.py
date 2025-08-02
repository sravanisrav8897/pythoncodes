numbers=[1,2,3,4,5,6]
print(numbers)


names=["srav","meena","chinni","ram","anji","krishna","siri"]
print(names)


combination=[1,2,3,4,"sravani","chinni",7,8,"siri"]
print(combination)


fruits = ["apple", "banana", "cherry"]
print(fruits)


fruits = ["apple", "banana", "cherry"]
print(fruits[0])        
print(fruits[-1])       

# slicing a list
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])      
print(numbers[:3])       
print(numbers[::-1])  


#list methonds
names = ["sravani", "kavya", "pallavi"]
names.append("mouni")
print(names)                 
names.remove("kavya")
print(names)                 
names.insert(1, "teju")
print(names)                 
names.sort()
print(names)             


languages = ["Python", "Java", "C++"]
for lang in languages:
    print(f"I like {lang}")


colors = ["red", "blue", "green"]
print(len(colors))             
if "blue" in colors:
    print("Blue is present")   


nums = [1, 2, 3, 4, 5, 6]
count = 0
for num in nums:
    if num % 2 == 0:
        count += 1
print("Even count:", count)

list = [10, 20, 30, 40, 50]
for i in range(len(list)-1, -1, -1):
    print(list[i])

mixed = [1, "sravani", 2.5, "kavya", True]
for item in mixed:
    if type(item) == str:
        print(item)

mixed = [1, "sravani", 2.5, "kavya", True]
for item in mixed:
    if type(item) == int:
        print(item)

mixed = [1, "sravani", 2.5, "kavya", True]
for item in mixed:
    if type(item) == bool:
        print(item)


mixed = [1, "sravani", 2.5, "kavya", True]
for item in mixed:
    if type(item) == float:
        print(item)


matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()


squares = [x*x for x in range(1, 6)]
print(squares)         
