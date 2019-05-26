# coding: utf-8
"""
Comment
Comment
Comment
"""
# Comment
# print("Hell World")

# 変数
# msg = "Hell World"
# print(msg)
# msg = "Hell Again"
# print(msg)

# 定数
# ADMIN_EMAIL = "taguchi@gmail.com"

# 文字列
# s = "he\nllo wor\tld"
# html = """<html>
# <body></body>
# </html>"""
# print(s)
# print(html)

# 整数
# i = 10

# 浮動小数点
# f = 23.4

# 論理値
# flag = True # false

# + - * / //切り捨て %余り **べき乗
# x = 10
# print(x / 3) # 3.33....
# print(x // 3) # 3
# print(x % 3) # 1
# print(x ** 2) # 100

# y = 4
# y = y + 12
# y += 12
# print(y) # 16

# and or not
# print(True and False) # False
# print(True or False) # True
# print(not True) # False

# + *繰り返し
# print("hello " + "word")
# print("hello " * 3)

# 文字列に値を埋め込み %s:文字列 %f:浮動小数点 %d整数　その後に%を記述し埋め込みたい値を記述
# name = "taguchi"
# score = 52.8

# print("name: %s, sore: %f" % (name, score))
# -左揃え10巾、
# print("name: %-10s, sore: %10.2f" % (name, score))
# 0番目、1番目の要素
# print("name: {0}, score: {1}".format(name, score))
# >右揃え桁数、<左揃え桁数
# print("name: {0:>10s}, score: {1:<10.2f}".format(name, score))
# > >= <= == !=
# score = int(input("score ?"))
# if score > 80:
#   print("Great!")
# elif score > 60:
#   print("Good!")
# else:
#   print("so so ...")
# print("Great!" if score > 80 else "so so ...")

# while
i = 0
while i < 10:
  if i == 5:
    break
  print(i)
  i += 1
else:
  print("end")

