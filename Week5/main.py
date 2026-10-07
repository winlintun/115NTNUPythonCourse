# 1
# num = int(input("number (n): "))
# count = 0

# if num == 0:
#     count = 1
# else:
#     while num > 0:
#         count += 1
#         num = num // 10
# print(count)


# 2
# user = input("enter thousands signs number: ")
# print(int(user) * 2)

# 3
# num = int(input("enter n of Factors: "))

# total =[]
# n = 1

# while num >= n:
#     if num % n == 0:
#         total.append(n)
#         n += 1 
#     else:
#         n += 1

# print("Total: ", total)


# 6
# num = 1
# while num <= 10:
#     if num % 3 != 0:
#         print(num, end=' ')
#         num += 1
#     else:
#         num += 1


# 7
# total = 0
# n = 1

# while total <= 100:
#     n += 1
#     total += n
# print(n)

# 11
# password = "NTNU115"
# att = 0
# while att >= 1:
#     user_pass = input("enter your password: ")
#     if user_pass == password:
#         print("Correct password")
#         break
#     if 6 > len(user_pass):
#         print("Password at last 6 words!!")
#         att += 1
#     else:
#         print("Wrong password!")
#         att += 1
# if att == 3:
#     print("You attempts have been reach 3 times")

# 12
# string = input("enter string character: ")
# is_digit = True
# for char in string:
#     if not (char >= '0' and char <= '9'):
#         is_digit = False    
#         break
# if is_digit:
#     print(string)
# else:
#     print("string character have contain number")

# 12
# string = input("enter number ")

# for char in string:
#     if not char.isdigit():
#          print("invalid")
#          break
# else:
#     print("string number ", string)


# 13
# nums = [8, 11, 98, 23, 47]
# for i in nums:
#     if i % 3 == 0:
#         print("can divied by: ", i)
#     else:
#         print("list have not found divided by 3")

# 15
# (a)
# arr = [i for i in range(1, 11)]
# print(arr)

# # (b)
# arr1 = []
# for i in range(1, 51):
#     if i % 3 == 0 and i % 4 == 0:
#         arr1.append(i)

# print(arr1)

# # (c)
# print([i for i in 'aeiou'])

# # (d)
# my_arr = [3, -1, 4, 7, -3, 2]
# print([1 if i > 0 else -1 for i in my_arr])

# 16
# my_list = ['Spring', 'Summer', 'Autumn', 'Winter']
# my_vowel = [i for i in "aeiouAEIOU"]
# a = []

# index = 0

## Working but wrong way
# while index <= 3:
#     for j in my_vowel:
#         for i in my_list[index]:
#             print("j = i: ", j , i)
#             if j == i:
#                 a.append(i)
#     index += 1

## Right Way
# while index <= 3:
#     for i in my_list[index]:
#         # print(i)
#         for j in my_vowel:
#             if i == j:
#                 a.append(i)
#     index += 1

# print(a)


# 17

# my_list = ['State', 'University', 'of', 'New', 'York', 'at', 'Buffalo']

# for i in my_list:
#     if 'a' in i:
#         print(i)

# print([i for i in my_list if 'a' in i])
