set = {1, 2, 3, 4, 5}
print(set)   


dup = {1, 2, 2, 3, 4}
print(dup)  

empty_set = {}            
numbers = {10, 20, 30}
mixed = {1, "hello", 3.5}

s = {1, 2, 3}
s.add(4)               
print(s)              
s.update([5, 6])       
print(s)               
s.remove(3)            
s.discard(10)          

for item in s:
    print(item)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))        
print(a.intersection(b)) 
print(a.difference(b))   
print(b.difference(a))   
print(a.symmetric_difference(b)) 

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  
print(a & b)
print(a - b)  
print(a ^ b)  

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list1)
print(list2)


s = {10, 20, 30}
converted = list(s)
print(converted)
