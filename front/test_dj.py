import networkx as nx
import pylab
import numpy as np
from django.http import HttpResponse
# 自定义网络
import heapq
import networkx as nx
import ch
ch.set_ch()
from networkx.utils import generate_unique_node

# def index(request):
#求最短路径
def dijkstra_path(G, source, target, weight='weight'):
    (length, path) = single_source_dijkstra(G, source=source, target=target,
                                            weight=weight)
    try:
        return (path[target],length[target])
    except KeyError:
        raise nx.NetworkXNoPath("node %s not reachable from %s" % (source, target))

def single_source_dijkstra(G, source, target=None, cutoff=None, weight='weight'):
    if source == target:
        return ({source: 0}, {source: [source]})
    dist = {}  # dictionary of final distances
    paths = {source: [source]}  # dictionary of paths
    seen = {source: 0}
    fringe = []  # use heapq with (distance,label) tuples
    heapq.heappush(fringe, (0, source))
    while fringe:
        (d, v) = heapq.heappop(fringe)
        if v in dist:
            continue  # already searched this node.
        dist[v] = d
        if v == target:
            break
        # for ignore,w,edgedata in G.edges_iter(v,data=True):
        # is about 30% slower than the following
        if G.is_multigraph():
            edata = []
            for w, keydata in G[v].items():
                minweight = min((dd.get(weight, 1)
                                 for k, dd in keydata.items()))
                edata.append((w, {weight: minweight}))
        else:
            edata = iter(G[v].items())

        for w, edgedata in edata:
            vw_dist = dist[v] + edgedata.get(weight, 1)
            if cutoff is not None:
                if vw_dist > cutoff:
                    continue
            if w in dist:
                if vw_dist < dist[w]:
                    raise ValueError('Contradictory paths found:',
                                     'negative weights?')
            elif w not in seen or vw_dist < seen[w]:
                seen[w] = vw_dist
                heapq.heappush(fringe, (vw_dist, w))
                paths[w] = paths[v] + [w]
    return (dist, paths)

row=np.array(['涡阳','涡阳','涡阳','涡阳'    ,'蒙城','蒙城','蒙城','蒙城',    '利辛','利辛','利辛','利辛',     '亳州市','亳州市','亳州市','亳州市','谯城区','谯城区','谯城区','谯城区'])
col=np.array(['蒙城','利辛','亳州市','谯城区','涡阳','利辛','亳州市','谯城区','蒙城','涡阳','亳州市','谯城区','蒙城','利辛','涡阳','谯城区',      '蒙城','利辛','亳州市','涡阳',])
value=np.array([43.0,  47.0,  61.3,   70.3,       43.0,  38,   123,      149,       38,     48,    116,    126,         103,  116,  75.6, 5,155,136,5,64.3])

G = nx.DiGraph()

for i in range(np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])

'''
Shortest Path with dijkstra_path
'''
print('dijkstra方法寻找最短路径：')

path,dist = dijkstra_path(G, source='蒙城', target='亳州市')
print('节点1到5的路径：', path,'距离是：',dist)
