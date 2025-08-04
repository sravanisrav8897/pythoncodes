t1=(1, 2, 3)
print(t1)

t2 = ("apple", "banana", "cherry")
print(t2)

print(t1[0])      
print(t2[-1])  

#t1[1] = 10
#         
t3 = ()                   
t4 = (5,)  

for fruit in t2:
    print(fruit)


print(t1[1:])      
print(t1[::-1])    



#tuple function
nums = (10, 20, 30, 20)
print(len(nums))         
print(min(nums))         
print(max(nums))         
print(nums.count(20))    
print(nums.index(30))    


t = (10, 20, 30)
a, b, c = t
print(a, b, c)     

t = (10, 20, 30, 40, 50)
print(t[::2])       

#reversed
t = (1, 2, 3, 4)
print(t[::-1])      

t = ("a", "e", "i", "o", "u")
print("e" in t)     

marks = (90, 80, 70, 90)
print(marks.count(90))    

t = (1, 2, (3, 4, 5))
print(t[2][1])     

t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)          


