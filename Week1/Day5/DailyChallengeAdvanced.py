# Instructions
# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

# target_number   = 3728


# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

# For example

# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728

# #######################################################################################################################################

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

#Way # 1 using a filter to get rid of the numbers above the target as we don't need them.

filtered_list = []


for num in list_of_numbers:
    if num <= 3728:
        filtered_list.append(num)

def check_sums_to_target(filtered_list,target_number):
    list_of_pairs = []
    for i in range(len(filtered_list)):
        for j in range(i+1,len(filtered_list)):
            if filtered_list[i] + filtered_list[j]== target_number:
                list_of_pairs.append((filtered_list[i],filtered_list[j]))  

    return list_of_pairs  

pairs = check_sums_to_target(filtered_list, target_number)
print(f"Found {len(pairs)} pairs!")
print(pairs)


#Way # 2 iterates through the whole list anyways


# def check_sums_to_target_2(list_of_numbers, target_number):
#     list_of_pairs2 = []
#     for i in range(len(list_of_numbers)):
#         for j in range(i+1, len(list_of_numbers)):
#             if list_of_numbers[i] + list_of_numbers[j] == target_number:
#                 list_of_pairs2.append((list_of_numbers[i], list_of_numbers[j]))
#     return list_of_pairs2

# pairs2= check_sums_to_target_2(list_of_numbers,target_number)
# print(f"Found {len(pairs2)} pairs!")
# print(pairs2)