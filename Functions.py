Exercize_Funtions

1.
def difference(a, b):
    return a - b

difference(2,2) # 0
difference(0,2) # -2

2.
def print_day(day_of_the_week):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if day_of_the_week in days:
        return days[day_of_the_week]
    return None
print(print_day(4))   # "Wednesday"
print(print_day(41))  # None

3.
def last_element(list):
    if len(list) == 0:
        return None
    return list[-1]
last_element([1,2,3,4]) # 4
last_element([]) # None

4.
def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater."
    elif num2 > num1:
        return "Second is greater."
    else:
        return "Numbers are equal."

print(number_compare(1, 1))   # "Numbers are equal"
print(number_compare(1, 2))   # "Second is greater"
print(number_compare(2, 1))   # "First is greater"

5.
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count('amazing', 'A'))  # 2
print(single_letter_count('amazing', 'a'))  # 2
print(single_letter_count('amazing', 'z'))  # 1
print(single_letter_count('amazing', 'x'))  # 0

6.
def multiple_letter_count(word):
    result = {}
    for char in word:
        result[char] = result.get(char, 0) + 1
    return result

print(multiple_letter_count("hello"))   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(multiple_letter_count("person"))  # {'p': 1, 'e': 1, 'r': 1, 's': 1, 'o': 1, 'n': 1}

7.
def list_manipulation(list, command, location, value=None):
    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "beginning":
        list.insert(0, value)
        return list
    elif command == "add" and location == "end":
        list.append(value)
        return list

print(list_manipulation([1, 2, 3], "remove", "end"))              # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))        # 1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))       # [20, 1, 2, 3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  

8.
def is_palindrome(text):
    # Remove whitespace and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    # Check if it equals its reverse
    return cleaned == cleaned[::-1]

print(is_palindrome('testing'))                          # False
print(is_palindrome('tacocat'))                          # True
print(is_palindrome('hannah'))                           # True
print(is_palindrome('robert'))                           # False
print(is_palindrome('a man a plan a canal Panama'))      # True           # [1, 2, 3, 30]

9.
def frequency(list, search_term):
    return list.count(search_term)

print(frequency([1, 2, 3, 4, 4, 4], 4))              # 3
print(frequency([True, False, True, True], False))   # 1

10.
def flip_case(string, letter):
    return "".join(char.swapcase() if char.lower() == letter.lower() else char for char in string)

print(flip_case("Hardy har har", "h"))  # "hardy Har Har"
print(flip_case("Hello World", "l"))    # "HeLLo WorLd"

11.
def multiply_even_numbers(list):
    product = 1
    for num in list:
        if num % 2 == 0:
            product *= num
    return product

print(multiply_even_numbers([2, 3, 4, 5, 6]))  # 48
print(multiply_even_numbers([1, 2, 3, 4]))     # 8
print(multiply_even_numbers([1, 3, 5]))        # 1

12.
def mode(list):
    counts = {}
    for num in list:
        counts[num] = counts.get(num, 0) + 1
    
    max_count = 0
    most_frequent = None
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent = num
    
    return most_frequent

print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))  # 4
print(mode([1, 1, 1, 2, 2, 3])) # 1

13.
def capitalize(name):
    return name.capitalize()

print(capitalize("tim"))    # "Tim"
print(capitalize("matt"))   # "Matt"
print(capitalize("hello"))  # "Hello"

14.
def compact(list):
    return [item for item in list if item]

print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))  # [1, 2, "All done"]
print(compact([False, 0, "", None, "Hello", 5]))                # ["Hello", 5]

15.
def partition(lst, callback):
    true_list = []
    false_list = []
    
    for item in lst:
        if callback(item):
            true_list.append(item)
        else:
            false_list.append(item)
    
    return [true_list, false_list]

def is_even(num):
    return num % 2 == 0

print(partition([1, 2, 3, 4], is_even))  # [[2, 4], [1, 3]]
print(partition([1, 2, 3, 4, 5, 6], is_even))  # [[2, 4, 6], [1, 3, 5]]

16.
def intersection(lst):
    if not lst:
        return []
    return list(set(lst[0]).intersection(*[set(l) for l in lst[1:]]))

print(intersection([[1, 2, 3], [2, 3, 4]]))              # [2, 3]
print(intersection([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))   # [2, 3]
print(intersection([[1, 2], [3, 4]]))                    # []

17.
def once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)
        return None
    
    wrapper.has_run = False
    return wrapper

def add(a, b):
    return a + b

one_addition = once(add)

print(one_addition(2, 2))      # 4
print(one_addition(2, 2))      # None
print(one_addition(12, 200))   # None