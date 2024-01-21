'''
编写程序实现以下功能：
（1） 输出sentence 中长度最长和最短的单词
（2） 创建字典，存放不同单词出现的个数（单词为键，个数为值），不区分大小写。
（3） 将该字典按照个数进行升序排序后输出
'''
sentence = 'Life is short.I love life and Python.' 
for c in ",.": 
    sentence = sentence.replace(c,' ')
sentence = sentence.lower() 
words = sentence.split()


lenlist =[len(word) for word in words]
m1 = max(lenlist)
m2 = min(lenlist)
print(words[lenlist.index(m1)])
print(words[lenlist.index(m2)])


d={}
for word in words:
    d[word] = d.get(word, 0) + 1
t = sorted(d.items(), key=lambda x:x[1]) 
print(t) 