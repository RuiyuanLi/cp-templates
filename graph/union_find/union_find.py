# 并查集
# leetcode题目: 5941-找出知晓秘密的所有专家，685-冗余连接 II，765-情侣牵手
class UnionFind:
    def __init__(self, n: int):
        self.ancestor = list(range(n))

    def find(self, node: int):
        if self.ancestor[node] != node:
            self.ancestor[node] = self.find(self.ancestor[node])
        return self.ancestor[node]
    
    def union(self, node1: int, node2: int):
        self.ancestor[self.find(node1)] = self.find(node2)

# 并查集具体操作
# 1. 断开连接
uf.ancestor[x] = x
uf.ancestor[y] = y

# 2. 统计连接块个数
for i in range(m):
    if uf.ancestor[i] == i:
        cnt += 1