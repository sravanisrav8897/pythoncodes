name='sravani'
print(name)

name = input("Enter your name: ")
print("Hello,", name)

#indexing
text = "sravani"
print(text[0])
print(text[2])
print(text[-1])
print(text[-2])

#slicing and indexing
text="sravani"
print(text[1:5])
print(text[3:])
print(text[2:])
print(text[::-1])


#methods
text = "  Hello Python World  "
my=text.replace("Python","sravani")
print(text.lower())
print(text.upper())
print(text.split())
print(my)
print(text.strip())


sentence = "learning python is super fun"
print(sentence)
print(sentence.title())
print(sentence[0:8])
print(sentence[::-1])
#print(sentence[reversed=True])
print(sentence.replace("super","really"))



text = "my name is SRAVANI"
clean = text.strip()
lower = clean.lower()
count = 0
for char in lower:
    if char == "o":
        count += 1
start_word= clean.startswith("Python")
last_word = clean.split()[-1]
print("Stripped Text:", clean)
print("Lowercase Text:", lower)
print("Count of 'o':", count)
print("Starts with 'Python':", start_word)
print("Last word:", last_word)

#Join()method
word=["my","name","is","sravani"]
join=" ".join(word)
print(join)


#find and index
name= "hello sravani"
print(name.find("s"))   
print(name.index("i"))   

#startwith and endwith
message= "my name is sravani"
print(message.startswith("my"))  
print(message.endswith("sravani"))     

print("abc".isalpha())     
print("123".isdigit())     
print("abc123".isalnum())  
print("   ".isspace())     

#f string
name = "sravani"
age = 19
print(f"My name is {name} and I am {age} years old.")
