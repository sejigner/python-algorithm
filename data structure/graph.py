class Graph:
    def __init__(self, vertex_num = None):
        # 인접 리스트
        self.adj_list = []
        self.vtx_num = 0
        # 정점이 있으면 True, 없으면 False
        self.vtx_arr = []

        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]

            self.adj_list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        return False
    
    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            # vtx_arr[i] 값이 False면 삭제된 정점
            if self.vtx_arr[i] == False:
                self.vtx_num += 1
                self.vtx_arr[i] = True
                return i
        self.adj_list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1
    
    def delete_vertex(self, v):
        if v >= self.vtx_num:
            raise Exception(f"There is no vertex of {v}")
        # 정점 v가 있으면
        if self.vtx_arr[v]:
            # 정점 v의 인접 정점 집합을 초기화
            self.adj_list[v] = []
            self.vtx_num -= 1
            self.vtx_arr[v] = False

            for adj in self.adj_list:
                for vertex in adj:
                    if vertex == v:
                        adj.remove(vertex)
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def delete_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def adj(self, v):
        return self.adj_list[v]