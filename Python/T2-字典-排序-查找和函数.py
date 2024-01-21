'''
2.  已知字典scored={'230001':[98,96],'230002':[88,86],'230003':[80,100]},
存放的是每个学生的姓名和两科成绩，编程实现以下功能：
(1)编写函数getAverd(d)，其中d为字典，利用d创建一个新字典，该字典以学号为键，两科成绩的平均成绩为值，并将其返回。
   要求在主程序中调用getAver(scored)，将返回的新字典输出。
(2)对新字典按照平均成绩进行升序排序后输出，输出形式为：
   [('230002', 87.0), ('230003', 90.0), ('230001', 97.0)]
(3)输入一个学号，输出其平均成绩，若该学号不存在，则输出“查无此人”。

'''
def getAver(d): #函数定义：d为形参字典，函数结束后返回新字典newd
    newd = {}  #定义空字典
    for k,v in d.items():   #遍历字典条目，k是键，v是该键对应的值
        newd[k] = sum(v)/len(v)  #给新字典添加键值对
    return newd   #注意return语句的位置：是for循环结束后返回


scored={'230001':[98,96],'230002':[88,86],'230003':[80,100]}  #初始化
averd = getAver(scored) #调用函数getAver并赋值给averd：scored是实参字典，通过这个语句得到新字典averd
print(averd) #输出

t = sorted(averd.items(), key = lambda x:x[1]) #按照平均成绩升序排序，得到列表
print(t)

name = input()  #输入学号
result = averd.get(name,'查无此人')   #查找
print(result)

