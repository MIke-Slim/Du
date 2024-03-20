library(xlsx)
setwd("C:/Users/20858/.vscode/code/R/Alldatasets")
FILE1<-read.xlsx()


for(i in 1:10){
  print(i)
}

x<-c('a','b','c','d')
for(i in seq_along(x)){
  print(x[i])
}
supply(x,mean)
apply(x,mean)

x<-c(157:164)
x1<-c(15:24)
x2<-c(10:1)
x3<-c(-1071:-1075,-1075:-1071)
x3
x4<-c(1.5:5.5)
C=rep()

www.R-bloggers.com