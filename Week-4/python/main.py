# temp = int(input("Enter temp: "))

# if temp >= 28:
#     print(f"現在溫度為 {temp} 度, 可開冷氣.")
# elif temp <= 15:
#     print(f"現在溫度為 {temp} 度, 可開暖氣.")

# else:
#     print(f"現在溫度為 {temp} 度, 不開暖氣.")

# 3

# year = int(input("Enter year: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("leap year")
# else:
#     print("common year")

# 5 
# grade = int(input("Enter grade: "))
# if grade >= 90:
#     print(f"Your grade is: A")
# elif grade >= 80:
#     print(f"{grade} 分，等級為: B")
# elif grade >= 70:
#     print(f"{grade} 分，等級為: C")
# elif grade >= 60:
#     print(f"{grade} 分，等級為: D")

# 7
# a 
# print('5為奇數' if 5 % 2 == 1 else '5為偶數')

# b 
# x, y = 6, 3

# print(x if x > y else y)

# 8 
# month = int(input("enter month (1-12): "))
# # month = 8

# if 3 <= month <= 5: print(f"{month} 月為春季")
# elif 6 <= month <= 8:print(f"{month} 月為夏季")
# elif 9 <= month <= 11: print(f"{month} 月為秋季")
# elif 2 >= month <= 12: print(f"{month} 月為冬季")
# else: print("Enter only month number!!")


# 9
# 1 hour 60 min and 3600 second
# sec = 14865

# hour = sec // 3600
# seconds = sec % 3600
# min =  seconds // 60 
# second = seconds % 60


# print(f"{hour} hours, {min} minutes, {second} seconds")

# 10. 
# hour = int(input("Enter hours: "))

# if hour >= 12:
#     fees = 30 * (hour - 12) + (12 * 40)
# else:
#     fees = 40 * hour
# print(f"停車 {hour}  小時， 應繳 {fees} 元")


# 12
# coin 50, 10, 5, 1
# price = int(input("Enter price: "))


# if price > 100:
# 	print("Insufficient money.")
# else:
# 	change = 100 - price

# 	if change >= 50:
# 		coin_50 = change // 50 # count number
# 		change  %= 50 # debit money
# 	else:
# 		coin_50 = 0

# 	if change >= 10:
# 		coin_10 = change // 10
# 		change %= 10

# 	else:
# 		coin_10 = 0

# 	if change >= 5:
# 		coin_5 = change // 5
# 		change %= 5
# 	else:
# 		coin_5 = 0

# 	coin_1 = change 


# 	print(f"50元 {coin_50}枚, 10元 {coin_10}元, 5元 {coin_5}元, 1元 {coin_1}元.")


# import math
# print(math.factorial(n))

# def fact(n):
# 	if n >= 1:
# 		return n * fact(n - 1)
# 	else:
# 		return 1
# print(fact(5))

# 13

# n = int(input("Enter number for factorial: "))

# result = 1

# for i in range(1, n + 1):
# 	result = i * result
# print(result)

# 15

# a = int(input("enter amount a: "))
# b = int(input("enter amount b: "))
# c = 1

# if a <= b:
# 	for i in range(1, a + 1):
# 		if a % c == 0 and b % c == 0 :
# 			c += i
# print(c)

# 16






# 19


data = [[2,4,5], [5,8, None], [10, 3, 4]]

for i in range(len(data)):
	value = 0
	for k in range(len(data)):
		# print(i, data[i][k])
		if data[i][k] == None:		
			print("Incomplete data")
			value = 0
			break

		value += data[i][k] 

	if value == 0:
		pass
	else: print(value)

