# # 1
# s = "abc123def456"
# print("".join([c for c in s if c.isdigit()]))

# # 2
# import random

# def guess():
#     count = 0
#     guess_number = random.randint(1, 10)
    
#     while (count >= 0):
#         n = int(input("Enter guess number: "))
#         if n == guess_number:
#             print(f"You guess: {n} is correct!")
#             print(f"You use guess attence: {count}  times")
#             break
#         elif n > guess_number:
#             print(f"You number: {n} is greater than!")
#             count += 1
#         elif n < guess_number:
#             print(f"You number: {n} is less than!")
#             count += 1

# # guess()

# # 3
# array = [1,2, 3, 4, 5]
# ans = 1
# for i in array:
#     if i % 2 != 0:
#         ans *= i 
        
# print(ans)

# # 4
# row = 10
# for i in range(1, row +1): # row
#     for k in range(row - i): #ｓｐｅａｃｅ
#         print(" ", end="")

#     for i in range(2 * i - 1): # column
#         print("*", end="")

#     print()

# # 5
# def check_vowel():
#     vowel = ("a", "e", "i", "o", "u")
#     user = str(input("say somethong: "))
#     count = 0

#     for i in user:
#         for k in vowel:
#             if i == k:
#                 count += 1
#     print(f"The worlds have found {count} vowel.")


# # 6
# def sum_number():
#     n = input("enter any number: ")
#     num = 0
#     while (len(n) > num):
#         for i in n:
#             num += int(i)
#     print(num)

# # 7
# def total_price(price):
#     total = 0
#     tax = 0.05
#     if price >= 200:
#         tax = 0.1
#         total = price * (1+tax)
#     else:
#         total = price * (1 + tax)
#     return round(total, 2)
# print(total_price(100))
# print(total_price(200))

# # 8

# def harmonic_sum(n):
#     return sum(1 / i for i in range(1, n+1))
# print(harmonic_sum(4))


# # 9
# num = 0
# def natural_numbers():
#     global num
#     num = num+1
#     yield(num)
# print(next(natural_numbers()))
# print(next(natural_numbers()))
# print(next(natural_numbers()))
# print(next(natural_numbers()))

# # 10
# names = ["John", "Jane", "Doe"]
# ages = [25, 30, 22]
# scores = [88, 92, 85]
# for index, _ in enumerate(zip(names, ages, scores)):
#     print(f"{names[index]} is {ages[index]} years old and scored {scores[index]}.")


# # 11

# lst = ["apple", 'banana', 'cherry']
# def print_items_with_index(lst):
#     for index, name in enumerate(lst):
#         print(f"index: {index}, itme: {name}")

# print_items_with_index(lst)

# # 12
# def find_first_digit(s:str):
#     for i in s:
#         if i.isdigit():   
#             return i
#     else:
#         return None
        
# print(find_first_digit("abc123"))
# print(find_first_digit("hello456"))
# print(find_first_digit("abc"))
        

# # 13
# def find_target(nums, target):
#     for i in range(num):
#         if target == i:
#             return "Target found"
#     else:
#         return "target not found!"

# print(find_target([1,2,3,4,5], 3))
# print(find_target([10,20,30,40], 25))

# # 14
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# grade = list(zip(names, scores))
# count = 1
# for index, key in enumerate(grade):
#     print(f"{count} {names[index]} scored {scores[index]}")
#     count += 1

# # 15
# numbers = [1, 2, 3, 4, 5, 6 ,7 , 8, 9]
# print([i*i for i in numbers if i % 2 != 0])

# # 16
# num = [12, 5, 8, 7, 9, 3, 7, 6]
# total = 0
# for  i in num:
#     if i % 3 == 0:
#         if i % 2 != 0:
#             total += i
# print(total)

# 17
row = 5
for i in range(row, -1, -1): # row
    line =""
    for c in range(5, -1, -1):
        if i + c == 5:
            line += str(i)
        else:
            line += "*"
    print(line)