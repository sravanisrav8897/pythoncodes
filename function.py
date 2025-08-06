def name():
    print("sravani")
name()


def name(name):
    print("Hello", name)
name("Sravani")
name("Python")


def add(a, b):
    return a + b
result = add(5, 10)
print("Sum:", result)


def info(name, age):
    print(f"{name} is {age} years old.")
info("Sravani", 22)


def name(name="User"):
    print("Hello", name)
name()
name("Sravani")


def total(*numbers):
    return sum(numbers)
print(total(1, 2, 3))
print(total(5, 10, 15, 20))


def info(**details):
    for key, value in details.items():
        print(key, ":", value)
info(name="Sravani", age=22, country="India")


def outer():
    print("This is the outer function.")
    def inner():
        print("This is the inner function.")
    inner()
outer()


square = lambda x: x * x
print(square(5))
add = lambda a, b: a + b
print(add(3, 7))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  


x = 10  
def test():
    x = 5  
    print("Inside function:", x)
test()
print("Outside function:", x)


def is_even(num):
    return num % 2 == 0
print(is_even(4))  
print(is_even(5))  


def maximum(a, b, c):
    return max(a, b, c)
print(maximum(10, 20, 5))  


def reverse_string(s):
    return s[::-1]
print(reverse_string("python"))  


def vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
print(vowels("Sravani"))  


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(11))  
print(is_prime(12))  
