#记录去重问题。请输出去掉重复记录之后的记录，及有重复学号的记录。

#方法1
lst1=['180001','180002','180003','180002','180004','180005','180005','180006']
set1=set(lst1)         #应用集合去重
lst2=list(set1).sort()
print(lst2)  #输出去掉重复记录之后的记录

lst3=[]
for item in lst1:
    if lst1.count(item)>1 and item not in lst3: 
        lst3.append(item)
print(lst3) #输出有重复学号的记录


#方法2：
lst1 = ['180001','180002','180003','180002','180004','180005','180005','180006']
list2 = [] 
duplicated = [] 
for someone in lst1: 
       if someone not in list2: 
	     list2.append(someone) 
      else:
             if someone not in duplicated: 
                  duplicated.append(someone) 
print(list2) 
print(duplicated) 