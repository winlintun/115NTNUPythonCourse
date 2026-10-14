# 3
# def isprime(x):
#     if x <= 1:
#         return False
#     elif x % 2 == 0:
#         return False
#     else:
#         return True

# print(isprime(17))

# # 4
# print([i for i in range(2, 18) if isprime(i)])

# 5

# def prime_factors(x):
#     lst = []
#     divisor = 2

#     while (x >= divisor):
#         if x % divisor == 0:
#             if divisor not in lst:
#                 lst.append(divisor)
#             x = x // divisor
#         else:
#             divisor += 1

#     return lst


# print(prime_factors(72))

# 6

# def factor(x):
#     lst = []
#     divisor = 2
#     while (x >= 2):
#         if x % divisor == 0:
#             count = 0

#             while x % divisor == 0:
#                 count += 1
#                 x = x // divisor
            
#             lst.append([divisor, count])
#         else:
#             divisor += 1
        
#     return lst

# print(factor(72))

# 8
# def to_number(worlds):
#     result = ''

#     text = worlds.upper()

#     for i in text:
#         if i in 'ABC':
#             result += '2'
#         elif i in 'DEF':
#             result += '3'
#         if i in 'GHI':
#             result += '4'
#         if i in 'JKL':
#             result += '5'
#         if i in 'MNO':
#             result += '6'
#         if i in 'PQRS':
#             result += '7'
#         if i in 'TUV':
#             result += '8'
#         if i in 'WXYZ':
#             result += '9'
#     return result

# print(to_number("python"))

# 9 

# n = 5591
# def n_digit(num):
#     count = 0
#     for _ in str(num):
#         count += 1
#     return count

# print(n_digit(n))

# 11

# my_list = [2, 4, 6]

# def square(lst):
   
#     return [i*i for i in lst]

# print(square(my_list))
# print(my_list)

# 12

# def combine(lst1, lst2):
#     my_list = []
#     for i in lst1:
#         my_list.append(i)
#     for i in lst2:
#         my_list.append(i)
#     return my_list

# list1 = [1,3]
# list2 = [2,5,6]
# print(combine(list1, list2))

# 14
# def add_n(lst, n=0):
#     return [i+n for i in lst]

# my_list = [1, 2, 3, 4]
# print(add_n(my_list))
# print(add_n(my_list, 2))

# 15
# def repeat_text(text, times=2):
#     return text * times

# print(repeat_text("Hi", 3))

# 17

def find_max(*arg):
    return max(arg)

print(find_max(4, 9, 3))
print(find_max(6, 4))