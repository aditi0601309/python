import random
random_numbers ={random.randint(15,45)for _ in range(10)}
print("original set:",random_numbers)
count_less_than_30 = sum(1 for num in random_numbers if num<30)
print("count of numbers less than 30:", count_less_than_30)
filtered_numbers = {num for num in random_numbers if num<= 35}
print("set after removing numbers greater than 35:",filtered_numbers)
