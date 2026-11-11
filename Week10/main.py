# 5
# lst = [43, 12, 12, 34]

# (a)
# lst.append([2, 12])
# print(lst)
# print(lst.count(12))

# # (b)
# lst.append([25, 99])
# print(lst)

# # (c)
# lst[1] = 65
# print(lst)
# print(lst[2])

# # (d) 
# # way 1
# lst.remove(12)

# # way 3
# print(lst.index(12))
# lst.pop(1)

# print(lst)


# # (e)
# print(lst)
# lst.sort()
# print(lst)

# # (f)
# print(lst)
# lst.pop()
# lst.pop(2)
# print(lst)


# # 7
# lst = [
#     [17, 21],
#     [98, 12],
#     [33, [44, [21, 38, 35]]],
#     [35, 42]]

# # (a)
# print(lst[0])

# # (b) 
# print(lst[0][1])

# # (c)
# print(lst[2][0])

# # (d)
# print(lst[3])

# # (e)
# print(lst[1][0])

# # (f)
# print(lst[2][1][0])

# # (g)
# print(lst[2][1][1])

# # (h)
# print(lst[2][1][1][1:])

# # (i)
# print(lst[2][1][1][0:-1])

# # (j)
# print(lst[2][1][1][1])

# # (k)
# print(lst[0:2])

# # (l)
# print(lst[2][1])



# # 9

# tpl = (12, 65, 37, 37, 34, 65, 37)

# # (a)
# print(max(tpl))
# print(sum(tpl))

# # (b)
# print(66 in tpl)

# # (c)
# print(tpl.index(34))

# # (d)
# print(tpl.count(37))


# # 10
# tpl = (10, 20, 30, 40)
# target = 30

# def find_value(tpl, target):

#     while target >= 1:
#         if target in tpl:
#             return tpl.index(target)
#     return -1

# print(find_value(tpl, target))


# # 13
# s1 = {3, 2, 2, 1, 4, 5}

# # (a)
# print("a: ", s1)

# # (b)
# print("b: ", 0 in s1)

# # (c)
# s2 = {0, 1, 2}
# print("c: ", s2 <= s1 )

# # (d)
# s3 = set(range(9))
# print(s3 >= s1)



# # 14
# s1 = {1, 2, 4, 4, 8}
# s2 = {4, 5, 6, 7, 8}

# # (a)
# s1.add(5)
# print("a: ", s1)

# # (b)
# s1.discard(8)
# print("b: ", s1)

# # (c)
# print("c: ", s1.difference(s2))

# # (d)
# print("d: ", s1.intersection(s2))

# # (e)
# print("e: ", s1.symmetric_difference(s2))

# # (f)
# print("f: ", s1.union(s2))

# # (g)
# print("g: ", s2.difference(s1))

# # (h)
# s1.clear()
# s2.clear()
# print("h: ", s1, s2)


# # 15

# def unique_intersection(s1, s2):
#     return s1.intersection(s2)

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(unique_intersection(s1, s2))


# # 17
# name = [(1, "January"), (2, "Feb"), (3, "Mar")]

# name = dict(name)
# print(name)


# # 18
# d1 = {0:'red', 1:'green', 2:'blue'}

# # a
# print("a: ", d1[1])

# # b
# d1[2] = "yellow"
# print("b: ", d1[2])

# # c
# d1.pop(0)
# print("c: ", d1)

# # d
# print("d: ", 4 in d1)


# # 19
# lst = ['Jan', 'Feb', 'Mar']
# d1 = {}
# d2 = {}

# # a
# for i in lst:
#     d1[i], d2[i] = None, None
# print("d1: ", d1)
# print("d2: ", d2)

# # b
# count = 0
# for i in lst:
#     count += 1
#     d1[i] = count
# print("b: ", d1)

# # c
# d1.update({"Apr": 4})
# print("c: ", d1)

# # d
# remove_value = d1.pop("Feb")
# print("d: ", remove_value)


# # 21 

# def make_dict(keys, values=None):
#     if values is None:
#         num = 0
#         d = {}
#         for i in keys:    
#             d[i] = num
#         return d
#     else:
#         return dict(zip(keys, values))

# print(make_dict([0, 1, 2], [32, 43, 55]))
# print(make_dict([0, 1, 2]))


# 22
def invert_dict(dic:dict):
    d = dict()
    for key, value in dic.items():
        d[value] = key
        # print(key, value)
    return d

d = {'a':1, 'b':2, 'c': 3}
print(invert_dict(d))




