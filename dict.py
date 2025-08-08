#example-1
students = {
    "student1": {"name": "Sravani", "age": 19},
    "student2": {"name": "Pavan", "age": 22}
}
print(students["student1"]["name"])  
print(students["student2"]["name"])  
print(students["student1"]["age"])  
print(students["student2"]["age"])


#example-2
person = {
    "name": "Sravani",
    "age": 19,
    "city": "India"
}
print(person)
print(person["name"])     
print(person.get("age"))  
person["age"] = 30
print(person)
person["email"] = "sravani@example.com"
print(person)
person.pop("city")
del person["email"]
print(person)
print(person.keys())       
print(person.values())     
print(person.items())      
for key in person:
    print(key, ":", person[key])
for key, value in person.items():
    print(f"{key} => {value}")


#example-3
squares = {x: x**2 for x in range(1, 6)}
print(squares)  

#example-4
fruits = {
    "apple": 50,
    "banana": 20,
    "cherry": 100
}
print(fruits)
fruits["mango"] = 60
fruits["banana"] = 25
print(fruits)
fruits.pop("cherry")
print("apple" in fruits)  


text = "hello world"
freq = {}
for char in text:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1
print(freq)


a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = {**a, **b}
print(merged)  


d1 = {"a": 100}
d2 = {"b": 200}
merged = {**d1, **d2}
print(merged)


a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
a.update(b)
print(a)  


keys = ["name", "age", "gender"]
values = ["Alice", 25, "female"]
result = dict(zip(keys, values))
print(result)


student = {
    "name": "Ravi",
    "marks": [80, 90, 85]
}
print(student["marks"][1])  


keys = ["a", "b", "c"]
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)


d = {"x": 10}
d.setdefault("y", 20)  
print(d)


a = {"x": 1}
b = {"y": 2}
c = a | b
print(c)


word = "banana"
count = {}
for char in word:
    count[char] = count.get(char, 0) + 1
print(count)


contacts={"sravani":9346107835,"pravallika":8796654345,"pavan":8756347834,"krishna":9876567854,"rani":6785456789}
print(contacts)
search=input("Enter the search one: ")
if search in contacts:
    print(contacts[search])
else:
    print("this name is not in the contacts list")
