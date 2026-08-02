my_string = "1231231231234567890"
count_sum = 0
for num in my_string:
    if num in "235":
        count_sum += int(num)
print(count_sum)