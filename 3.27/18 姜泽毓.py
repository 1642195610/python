# 7.输出9行内容，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789
# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j,end="")
#         j += 1
#     print()
#     i += 1

# 1. 计算从1到1000以内所有能被3或者17整除的数的和并输出
# count=1
# sum=0
# while count < 1000:
#     if count % 3 == 0 or count % 17 == 0:
#         sum += count
#     count += 1
# print("sum= %s"%(sum))

# 2. 求1到10的阶乘 (格式为 5的阶乘为: 120 )
# 	5: 5 * 4 * 3 * 2 * 1
# 	4: 4 * 3 * 2 * 1
# 	3: 3 * 2 * 1
# 	2: 2 * 1
# 	1: 1
# 	结果:
# 	5的阶乘为: 120
# 	4的阶乘为: 120
# 	3的阶乘为: 120
# 	2的阶乘为: 120
# 	1的阶乘为: 120
# i = 1
# while i <= 10:
#     j = 1
#     s = 1
#     while j <= i:
#         s *= j
#         j += 1
#     print("%s的阶乘为: %s" % (i, s))
#     i += 1

# 3. 求一到十阶乘之和。(1: 1 2: 2  3: 6  4: 24 5: 120)
# i = 1
# sum = 0
# while i <= 10:
#     j = 1
#     s = 1
#     while j <= i:
#         s *= j
#         j += 1
#     sum += s
#     i += 1
# print("1-10的阶乘之和为:%s"%(sum))

# 4. 功能：用户登录(三次机会尝试)
# 用户名密码：
# name = "aaa"
# password = "123"
# 让用户输入，如果输入正确，显示登录成功， 失败，显示还有几次机会， 超过三次失败，显示失去登录机会，明天再来。退出程序。
# i = 1
# while i <= 3:
#     name = input("请输入用户名:")
#     password = int(input("请输入密码:"))
#     if name == "aaa" and password == 123 :
#         print("登录成功")
#         break
#     elif 3-i > 0 :
#         print("失败,还有%s次机会"%(3-i))
#     else:
#         print("失去登录机会, 明天再来")
#     i += 1

# 5. 打印出所有的“水仙花数”。
# 所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。
# i = 100
# print("所有的水仙花数为:",end=" ")
# while i <= 999 :
#     a = i // 100
#     b = i % 100 // 10
#     c = i % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i,end=" ")
#     i += 1

# 6.五位数中，对称的数称为回文数，打印所有的回文数并计算个数。如:12321
# i = 10000
# t = 1
# print("所有的回文数为:")
# while i <= 99999 :
#     a = i // 10000
#     b = i % 10000 // 1000
#     c = i % 100 // 10
#     d = i % 10
#     if a == d and b == c :
#         print(i,end=" ")
#         t += 1
#         # 10 个数换行
#         if t == 10 :
#             print()
#             t = 1
#     i += 1

# 8.打印等腰三角形
# *
# ***
# *****
# *******
# *****
# ***
# *
# j = 1
# i = 1
# while j <= 7 :
#     if j <= 4 :
#         print("*" * i)
#         if j == 4 :
#             i -= 2
#         i += 2
#     else :
#         i -= 2
#         print("*" * i)
#     j += 1

# 9.打印菱形
# 提示:
# print(' ' * 3,end='')
# print('*')
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# j = 1
# i = 1
# while j <= 7 :
#     if j <= 4 :
#         print(" " * (4-j),end="")
#         print("*" * i)
#         if j == 4 :
#             i -= 2
#         i += 2
#     else :
#         i -= 2
#         print(" " * (j-4), end="")
#         print("*" * i)
#     j += 1

# 10.打印九九乘法表
# 1 * 1 = 1
# 1 * 2 = 2	2 * 2 = 4
# 1 * 3 = 3	2 * 3 = 6	3 * 3 = 9
# 1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16
# 1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25
# 1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36
# 1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49
# 1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64
# 1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81
# i = 1
# while i <= 9 :
#     j = 1
#     while j <= i :
#         print("%s * %s = %s"%(j,i,i * j),end="\t")
#         j += 1
#     print()
#     i += 1


# 11.公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？
# 假设这是第七天剩余的桃子数
# i = 1
# j = 1
# #前6天吃的桃子
# while j <= 6 :
#     i =(i + 1) *2
#     j += 1
# print("桃子总数为:%s"%(i))

# 12.求出1-100所有的质数(质数: 只能被1和它本身整除的数)
#判断的数为i
# i = 2
# #a是换行计数
# a = 1
# print("1-100所有的质数为:")
# while i <= 100 :
#     #j是被除数
#     j = 1
#     #t是判断被整除几次
#     t = 0
#     #一个数整除的一遍
#     while j <= i :
#         if i % j == 0 :
#             #被整除一次＋1
#             t += 1
#         j += 1
#         #证明只能被1和它本身整除
#     if t <= 2 :
#         print("%s"%(i),end="\t")
#         a += 1
#         #10个数换一行
#         if a > 10 :
#             print()
#             a=1
#     i += 1
















