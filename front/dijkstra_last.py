import time

def test():
    start=time.clock()
    import networkx as nx
    def Dijkstra(G,start,end):
        RG = G.reverse(); dist = {}; previous = {}
        for v in RG.nodes():
            dist[v] = float('inf')#初始化为正无穷
            previous[v] = 'none'
        dist[end] = 0
        u = end
        while u!=start:
            u = min(dist, key=dist.get)           
            distu = dist[u]
            del dist[u]
            for u,v in RG.edges(u):
                if v in dist:
                    alt = distu + RG[u][v]['weight']
                    if alt < dist[v]:
                        dist[v] = alt
                        previous[v] = u
        path=(start,)
        last= start
        while last != end:
            nxt = previous[last]
            path += (nxt,)
            last = nxt
        path1=[]
        for i in path:
            path1.append(i)
        dist1=0
        for i in range(len(path)-1):
            dist1+=G[path[i]][path[i+1]]['weight']
        return path1,dist1
    G=nx.DiGraph()
    G.add_edge(0,1,weight=80)
    G.add_edge(1,2,weight=50)
    G.add_edge(1,3,weight=30)
    G.add_edge(3,2,weight=10)
    G.add_edge(2,4,weight=20)
    G.add_edge(2,5,weight=30)
    G.add_edge(4,5,weight=10)
    G.add_edge(5,3,weight=5)
    G.add_edge(2,6,weight=10)
    G.add_edge(4,6,weight=10)
    G.add_edge(3,6,weight=25)
    G.add_edge(5,6,weight=35)
    dict1={0:'哈尔滨',1:'长春',2:'沈阳',3:'大庆',4:'齐齐哈尔',5:'四平',6:'吉林'}
    rs1=[]
    start1='长春'
    end1='吉林'
    for i in range(len(dict1)):
        if dict1[i]==start1:
            start2=i
        if dict1[i]==end1:
            end2=i
    rs,ds=Dijkstra(G,start2,end2)
    for i in rs:
        rs1.append(dict1[i])
    print(rs1)
    print(ds)
    end=time.clock()
    total_time=end-start
    print("总耗时:"+str(total_time)+'秒')

if __name__=="__main__":
    test()
