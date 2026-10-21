# # 1
# ## (a)
# counter = 0
# def increment():
#     global counter
#     counter += 1
#     print("Counter : ", counter)

# ## (b)
# def get_counter():
#     return counter

# ### (c)
# increment()
# increment()
# increment()
# print(get_counter())

# 3
# def total(n):
#     if n <= 1:
#         return 1
#     return n + total(n - 1)
# print(total(5))

# # 4
# def r_pow(base, n):
#     if n == 0:
#         return 1
#     return base * r_pow(base, n - 1)

# print(r_pow(2, 8))

# # 6
# ## (a)
# def fib_for(n):  
#     lst = [1, 1]
#     for i in range(3, n + 1):
#         lst.append(lst[-2] + lst[-1])    
#     return lst[-1]
# print(fib_for(40))

# ## (b)
# # 102334155
# def fib_rec(n):
#     if n <= 1:
#         return n
#     return  fib_rec(n - 1) + fib_rec(n - 2)
    
# print(fib_rec(40))

# # (c)
# """
# For loop is better than recursive function. Because recursive function is too slow.

# """

# # 7
# ## (a)
# def sing(x):
#     if x >= 0:
#         return 1
#     else:
#         return -1

# print(sing(2))

# ## (b)
# x = 1
# result = lambda x: 1 if x > 1 else -1
# print(result(-5))
# print(result(5))

# ## (c)

# lst = [9, -3, 8, 2, 1, -1, -4]

# ans = lambda x:  [1  if i >= 0 else -1  for i in lst]

# print(ans(lst))


# ## (d)
# def sing2(x):
#     result = lambda x: 1 if x > 0 else -1
#     return result(x)
# print(sing2(-5))
# print(sing2(5))

# # 8
# ## (1)
# ans1 = lambda x: x if x > 0 else -x
# print(ans1(5))

# ## (2)
# ans2 = lambda x: "True" if x % 2 ==0 else "False"
# print(ans2(5))


# 10
# lst = [-3, 6, -4, 6, 8]
# ans = lambda: [i if i > 0 else 0 for i in lst]
# print(ans())

# 13
# a = (45, 33, 75)
# b = (109, 85, 63)
# c = (9, 8, 5)
# result = zip(a, b, c)
# print(list(result))

# 15
def gen(n):
    if n % 3 == 0 and n % 5 != 0:
        yield f"可以被 3 整除，但不能被 5 整除的數: {n}"
    yield f"不可以被 3 整除 : {n}"
print(next(gen(9)))

# 16
n = 8
def isprime(x):
    if x <= 1:
        return False
    elif x % 2 == 0:
        return False
    else:
        return True
    
def prime(n):
    lst = []
    for i in range(2, n):
        if isprime(i):
            lst.append(i)
    return lst


print(prime(n))

# 17
prime = (i for i in range(2, n) if isprime(i))
print(next(prime))
print(next(prime))
print(next(prime))
# print(next(prime))

