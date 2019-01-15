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
    (length, path) = single_source_dijkstra(G, source, target=target,
                                            weight=weight)
    try:
        return path[target]
    except KeyError:
        raise nx.NetworkXNoPath("node %s not reachable from %s" % (source, target))

#求最短距离
def dijkstra_path_length(G, source, target, weight='weight'):
    length = single_source_dijkstra_path_length(G, source, weight=weight)
    try:
        return length[target]
    except KeyError:
        raise nx.NetworkXNoPath("node %s not reachable from %s" % (source, target))


def single_source_dijkstra_path_length(G, source, cutoff=None,
                                       weight='weight'):
    dist = {}  # dictionary of final distances
    seen = {source: 0}
    fringe = []  # use heapq with (distance,label) tuples
    heapq.heappush(fringe, (0, source))
    while fringe:
        (d, v) = heapq.heappop(fringe)
        if v in dist:
            continue  # already searched this node.
        dist[v] = d
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
    return dist


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


# row = np.array([1, 1, 1, 2, 3, 4, 4, 4, 6, 7, 6, 7, 8, 8, 9, 10, 10, 11])
# col = np.array([2, 3, 5, 4, 5, 5, 6, 7, 5, 6, 8, 9, 9, 10, 11, 11, 12, 12])
# value = np.array([10, 20, 60, 20, 40, 10, 30, 1, 1, 6, 10, 10, 10, 10, 10, 10, 10, 10])

row=np.array(['涡阳','涡阳','涡阳','涡阳'    ,'蒙城','蒙城','蒙城','蒙城',    '利辛','利辛','利辛','利辛',     '亳州市','亳州市','亳州市','亳州市','谯城区','谯城区','谯城区','谯城区'])
col=np.array(['蒙城','利辛','亳州市','谯城区','涡阳','利辛','亳州市','谯城区','蒙城','涡阳','亳州市','谯城区','蒙城','利辛','涡阳','谯城区',      '蒙城','利辛','亳州市','涡阳',])
value=np.array([43.0,  47.0,  61.3,   70.3,       43.0,  38,   123,      149,       38,     48,    116,    126,         103,  116,  75.6, 5,155,136,5,64.3])
print('生成一个空的有向图')
G = nx.DiGraph()
print('为这个网络添加节点...')
# for i in range(1, 13):
#     G.add_node(i)
# list1=['涡阳','蒙城','利辛','亳州市','谯城区']
# for i in range(5):
#     # print(list1[i])
#     G.add_node(list1[i],coding='utf-8')
print('在网络中添加带权中的边...')
for i in range(np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])
print('给网路设置布局...')
pos = nx.shell_layout(G)
print('画出网络图像：')
nx.draw(G, pos, with_labels=True, node_color='white', edge_color='red', node_size=400, alpha=0.5)
pylab.title('Self_Define Net', fontsize=25)
pylab.show()

'''
Shortest Path with dijkstra_path
'''
print('dijkstra方法寻找最短路径：')
# path = dijkstra_path(G, source=1, target=5)


# distance = dijkstra_path_length(G, source=1, target=5)
distance = dijkstra_path_length(G, source='蒙城', target='谯城区')
print('节点1到5的距离为：', distance)
path = dijkstra_path(G, source='蒙城', target='谯城区')
print('节点1到5的路径：', path)
print('dijkstra方法寻找最短距离：')
row = np.array(
    ['蒙城','涡阳'])
col = np.array(
    ['涡阳','亳州'])
value = np.array(
    [dijkstra_path_length(G, source='蒙城', target='涡阳'),dijkstra_path_length(G, source='涡阳', target='亳州市')])
# print('生成一个空的有向图')
G = nx.DiGraph()
# print('为这个网络添加节点...')
# print('在网络中添加带权中的边...')
for i in range(np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])
print('给网路设置布局...')
pos = nx.shell_layout(G)
print('画出网络图像：')
nx.draw(G, pos, with_labels=True, node_color='white', edge_color='red', node_size=400, alpha=0.5)
pylab.title('Self_Define Net', fontsize=25)
pylab.show()
# return HttpResponse('123')