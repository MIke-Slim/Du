'''
有一段英文，In the age of economic globalization, countries are closely linked in their development and they all rise and fall together.No country could seek development on its own; and the one sure path is through coordination and cooperation.  编写程序完成：
（1）统计其中出现的字母及其次数，并按照字母升序排序输出
（2）统计单词及其个数，并输出出现次数最高的5个单词
'''
txt = "In the age of economic globalization, countries are closely linked in their development and they all rise and fall together.No country could seek development on its own; and the one sure path is through coordination and cooperation. "
zidict={}
for c in txt:
    if c.isalpha():
        x = c.lower()
        zidict[x]=zidict.get(x,0)+1
print(zidict)   #输出字母及其次数
print(sorted(zidict.items())) #按照字母顺序排序，输出字母及其次数

exclude = ',.;?!'
for c in exclude:
    txt = txt.replace(c,' ')
words = txt.strip().split()   #使用split()根据空格分词，得到单词列表words
worddict={}
for word in words:
    worddict[word] = worddict.get(word,0)+1
print(worddict)
wordlist = sorted(worddict.items(),key=lambda x:x[1], reverse = True )  #按照单词出现的次数降序排列，题型大家注意的地方有：items()，对按照哪个关键字排序是key=lambda x:x[1]，降序reverse = True
for item in wordlist[:5]:   #遍历列表wordlist前5项即0~4项
    print(item)    

'''
运行结果:
{'i': 14, 'n': 20, 't': 16, 'h': 8, 'e': 24, 'a': 13, 'g': 4, 'o': 23, 'f': 2, 'c': 8, 'm': 3, 'l': 12, 'b': 1, 'z': 1, 'u': 5, 'r': 10, 's': 7, 'y': 3, 'k': 2, 'd': 9, 'v': 2, 'p': 4, 'w': 1}
[('a', 13), ('b', 1), ('c', 8), ('d', 9), ('e', 24), ('f', 2), ('g', 4), ('h', 8), ('i', 14), ('k', 2), ('l', 12), ('m', 3), ('n', 20), ('o', 23), ('p', 4), ('r', 10), ('s', 7), ('t', 16), ('u', 5), ('v', 2), ('w', 1), ('y', 3), ('z', 1)]
{'In': 1, 'the': 2, 'age': 1, 'of': 1, 'economic': 1, 'globalization': 1, 'countries': 1, 'are': 1, 'closely': 1, 'linked': 1, 'in': 1, 'their': 1, 'development': 2, 'and': 4, 'they': 1, 'all': 1, 'rise': 1, 'fall': 1, 'together': 1, 'No': 1, 'country': 1, 'could': 1, 'seek': 1, 'on': 1, 'its': 1, 'own': 1, 'one': 1, 'sure': 1, 'path': 1, 'is': 1, 'through': 1, 'coordination': 1, 'cooperation': 1}
('and', 4)
('the', 2)
('development', 2)
('In', 1)
('age', 1)
'''
