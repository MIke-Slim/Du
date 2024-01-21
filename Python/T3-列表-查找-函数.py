''' 
现有一组列表形式存储的中英翻译：dictcn = [('one','一'),('two','二'),('three','三'),('four','四')]
(1) 请编写一个函数translate(en)，参数en为要查询的英文单词，返回对应的中文翻译结果，
    如果找不到该单词，则返回None.
（2）主程序调用该函数，输出用户输入的英文单词的查询结果，
     如果该单词没有在中英翻译列表中，则：输出“中文翻译未找到，请输入正确翻译”，询问用户该单词的翻译，并加入到列表中，而后输出列表。
例如：
当用户输入two
输出 二

当用户输入five
输出：中文翻译未找到，请输入正确翻译
用户输入五后，输出 [('one','一'),('two','二'),('three','三'),('four','四'),('five','五')]
'''
 
def translate(en):  #函数定义
    for e,c in dictcn:   #遍历列表dictcn,这里列表元素是双元素，可以写成两个变量的形式e和c，方便下面的使用
        if e == en:     
            return c     #当e不等于en时，返回None

dictcn = [('one','一'),('two','二'),('three','三'),('four','四')] #初始化
word = input() #输入
ch = translate(word) #函数调用

if ch: #查找并输出
    print(ch)
else:
     print("中文翻译未找到，请输入正确翻译")
     ch = input()
     dictcn.append((word,ch))
print(dictcn)
