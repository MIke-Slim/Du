#include<stdio.h>
#include <stdlib.h> 
#define InitSize 10  
//定义类型
typedef struct {
	int* data;
	int MaxSize;
	int length;
}SeqList;

SeqList* InitList(SeqList& L);//定义函数
SeqList* IncreaseSize(SeqList& L, int len);//定义函数

//main 函数
int main() {
	SeqList L;
	InitList(L);
	printf("请输入数字");
	for (int i = 0; i < InitSize; i++) {
		scanf("%d", &L.data[i]);//scanf不安全 需定义条件 防数据溢出
		L.length++;
	}
	IncreaseSize(L, 5);//给L链表添加5个长度
	return 0;
}

SeqList* InitList(SeqList& L) {
	L.data = (int*)malloc(InitSize * sizeof(int));
	L.length = 0;
	L.MaxSize = InitSize;
	return &L;
}//返回的数据应该是链表类型的指针
SeqList* IncreaseSize(SeqList&L, int len) {
	int* p = L.data;
	L.data = (int*)malloc((L.MaxSize + len) * sizeof(int));
	for (int i = 0; i < L.length; i++) {
		L.data[i] = p[i];
	}
	L.MaxSize = L.MaxSize + len;
	free(p);
	return &L;
}