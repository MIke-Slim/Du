x<-5
x
#hello world
x<-c(1,2,3,4,5,6)
x

x<-c(1:6)
x


X<-scan()

Y<-c("Tom","ui")
Y
#repeat
ind<-c(rep("A",12),rep("B",13))
#正太分布
#GroupX<-rnorm(数量，均值，标准差)
GroupA<-rnorm(12,4,1)
GroupB<-rnorm(13,7,1)
GroupC<-rnorm(12,9,1)
GroupD<-rnorm(12,2,1)
dep<-c(GroupA,GroupB)
dim(Data)
Data
Data<-data.frame(ind,dep)
Data$dep<-as,integer(DAta$dep)
tapply(Data$dep,Data$ind,min)
tapply(Data$dep,Data$ind,max)
tapply(Data$dep,Data$ind,mean)
tapply(Data$dep,Data$ind,sum)
Data<5
all(Data$ind>10)
any(Data$dep<10)
sum(Data$ind>10)
Sorted<-order(Data$dep)
Data[Sorted,]
Sorted1<-order(-Data$dep)
Data[Sorted1,]
boxplot(Data$dep~Data$ind)
setwd("C:/Users/20858/.vscode/code/R")
SubsetA<-Data[Data$ind=="A",2]
SubsetB<-Data[Data$ind=="B",2]
hist(SubsetA)
hist(SubsetB)
New1<-Data[Data$dep>5,]
New1
table(New1)
New2<-Data[Data$dep>5 & Data$dep<10,]
table(New2)
length(New2$ind)
length(New2$dep)
table(New2$ind)

2 | 0
2&0
!0
New3<-Data[Data$dep==1|Data$dep==5|Data$dep==8,]
table(New3)
New4<-Data[Data$dep!=1 & Data$dep!=5,]
table(New4)
New5<-Data[Data$ind=="A"&Data$dep>4,]
New5
New6<-Data[(Data$ind=="A"|Data$ind=="B")&Data$dep>5,]
New6
X<-runif(1,2,10)
X=sample(2:10,1)
X<-sample(2:10,100,replace=T)
X<-rnorm(100,10,1)
Names<-c("1","2")
X<-sample(Names,3,replace=T)

