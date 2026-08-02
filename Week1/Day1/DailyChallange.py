import random

mystring = input("Enter a 10 character string: ")
good_string =""
build_a_string =""

if len(mystring) < 10:
    print("String not long enough.")
elif len(mystring) > 10:
    print("String too long.")
else:
    print("Perfect string.")
    good_string = mystring

print(good_string[0])
print(good_string[-1])  

for num in good_string:
    build_a_string += num 
    print(build_a_string)

randomize = list (good_string)
random.shuffle(randomize)
randomized_string = "".join(randomize)
print(randomized_string)
