//领接矩阵法
#define MAX_VERTEX_NUM 100  //最大顶点数设为100
typedef struct {
    char vexs[MAX_VERTEX_NUM];  //顶点表
    int arcs[MAX_VERTEX_NUM][MAX_VERTEX_NUM];  //邻接矩阵，可看做边表
    int vexnum, arcnum;  //图的当前顶点数和边数
} MGraph;
//求顶点的度：第i行或列的非零元素的个数：无向图
//列加行=度：有向图

//带权图：0=无穷
#define INFINITY INT_MAX  //无穷大
typedef char VertexType;  //顶点类型
typedef int EdgeType;  //边上权值类型
typedef struct {
    VertexType vexs[MAX_VERTEX_NUM];  //顶点表
    EdgeType arc[MAX_VERTEX_NUM][MAX_VERTEX_NUM];  //邻接矩阵，可看做边表
    int vexnum, arcnum;  //图的当前顶点数和边数
    int kind;  //表示图的种类：0表示无向图，1表示有向图
} Graph;