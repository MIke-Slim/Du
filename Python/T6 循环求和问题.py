#1.对输入数据求均值，当输入的数据为-1时程序结束，并输出不含-1的数据的数据的平均值
total = k = 0
x = eval(input())
while x!=-1:
    total += x
    k += 1
    x = eval(input())
if k==0:   #考虑边界数据，当用户输入的第一个数是-1的情况
    print("输入的数据不合法!")
else:
    print(total/k)
    

#2，有公式s=1-1/3+1/5-1/7+1/9.。。计算s，直到最后一项的绝对值小于0.001。

total = 0
flag = divisor = 1  # 初始化第一项符号和分母
n = flag*1/divisor  # 先计算第一项
# 构建循环结构完成判定和求和以及计算下一项工作
while abs(n)>=0.001:
    total += n
    flag = - flag   #符号变化
    divisor += 2    #分母增2
    n = flag*1/divisor

print(total)