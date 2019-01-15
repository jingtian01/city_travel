
import networkx as nx
def Dijkstra(G, start, end):
    RG = G.reverse();
    dist = {};
    previous = {}
    for v in RG.nodes():
        dist[v] = float('inf')  # 初始化为正无穷
        previous[v] = 'none'
    dist[end] = 0
    u = end
    while u != start:
        u = min(dist, key=dist.get)
        distu = dist[u]
        del dist[u]
        for u, v in RG.edges(u):
            if v in dist:
                alt = distu + RG[u][v]['weight']
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
    path = (start,)
    last = start
    while last != end:
        nxt = previous[last]
        path += (nxt,)
        last = nxt
    path1 = []
    for i in path:
        path1.append(i)
    dist1 = 0
    for i in range(len(path) - 1):
        dist1 += G[path[i]][path[i + 1]]['weight']
    return path1, dist1

G = nx.DiGraph()
G.add_edge(0, 1, weight=469)
G.add_edge(1, 0, weight=469)
G.add_edge(0, 2, weight=269.1)
G.add_edge(2, 0, weight=269.1)
G.add_edge(0, 3, weight=409.3)
G.add_edge(3, 0, weight=409.3)
G.add_edge(0, 4, weight=153)
G.add_edge(4, 0, weight=153)
G.add_edge(0, 5, weight=341.9)
G.add_edge(5, 0, weight=341.9)
G.add_edge(0, 6, weight=586.6)
G.add_edge(6, 0, weight=586.6)
G.add_edge(0, 7, weight=453)
G.add_edge(7, 0, weight=453)
G.add_edge(0, 8, weight=340.3)
G.add_edge(8, 0, weight=340.3)
G.add_edge(0, 9, weight=593.3)
G.add_edge(9, 0, weight=593.3)
G.add_edge(0, 10, weight=709.0)
G.add_edge(10, 0, weight=709.0)
G.add_edge(0, 11, weight=108.5)
G.add_edge(11, 0, weight=108.5)
G.add_edge(1, 2, weight=779.9)
G.add_edge(2, 1, weight=779.9)
G.add_edge(1, 3, weight=807.5)
G.add_edge(3, 1, weight=807.5)
G.add_edge(1, 4, weight=149)
G.add_edge(4, 1, weight=149)
G.add_edge(1, 5, weight=952)
G.add_edge(5, 1, weight=952)
G.add_edge(1, 6, weight=888.5)
G.add_edge(6, 1, weight=888.5)
G.add_edge(1, 7, weight=645.9)
G.add_edge(7, 1, weight=645.9)
G.add_edge(1, 8, weight=1105)
G.add_edge(8, 1, weight=1105)
G.add_edge(1, 9, weight=891)
G.add_edge(9, 1, weight=891)
G.add_edge(1, 10, weight=493)
G.add_edge(10, 1, weight=493)
G.add_edge(1, 11, weight=533)
G.add_edge(11, 1, weight=533)
G.add_edge(2, 11, weight=583)
G.add_edge(11, 2, weight=583)
G.add_edge(2, 10, weight=1273)
G.add_edge(10, 2, weight=1273)
G.add_edge(2, 9, weight=708)
G.add_edge(9, 2, weight=708)
G.add_edge(2, 8, weight=375)
G.add_edge(8, 2, weight=375)
G.add_edge(2, 7, weight=822)
G.add_edge(7, 2, weight=822)
G.add_edge(2, 6, weight=574)
G.add_edge(6, 2, weight=574)
G.add_edge(2, 5, weight=172)
G.add_edge(5, 2, weight=172)
G.add_edge(2, 4, weight=654)
G.add_edge(4, 2, weight=654)
G.add_edge(2, 3, weight=561)
G.add_edge(3, 2, weight=561)
G.add_edge(3, 4, weight=595)
G.add_edge(4, 3, weight=595)
G.add_edge(3, 5, weight=366)
G.add_edge(5, 3, weight=366)
G.add_edge(3, 6, weight=84)
G.add_edge(6, 3, weight=84)
G.add_edge(3, 7, weight=294)
G.add_edge(7, 3, weight=294)
G.add_edge(3, 8, weight=276)
G.add_edge(8, 3, weight=276)
G.add_edge(3, 9, weight=67)
G.add_edge(9, 3, weight=67)
G.add_edge(3, 10, weight=842)
G.add_edge(10, 3, weight=842)
G.add_edge(3, 11, weight=416)
G.add_edge(11, 3, weight=416)
G.add_edge(4, 5, weight=779)
G.add_edge(5, 4, weight=779)
G.add_edge(4, 6, weight=748)
G.add_edge(6, 4, weight=748)
G.add_edge(4, 7, weight=666)
G.add_edge(4, 8, weight=723)
G.add_edge(8, 4, weight=723)
G.add_edge(7, 4, weight=666)
G.add_edge(4, 9, weight=741)
G.add_edge(9, 4, weight=741)
G.add_edge(4, 10, weight=866)
G.add_edge(10, 4, weight=866)
G.add_edge(4, 11, weight=187)
G.add_edge(11, 4, weight=187)
G.add_edge(5, 6, weight=434)
G.add_edge(6, 5, weight=434)
G.add_edge(5, 7, weight=562)
G.add_edge(7, 5, weight=562)
G.add_edge(5, 8, weight=75)
G.add_edge(8, 5, weight=75)
G.add_edge(5, 9, weight=444)
G.add_edge(9, 5, weight=444)
G.add_edge(5, 10, weight=1400)
G.add_edge(10, 5, weight=1400)
G.add_edge(5, 11, weight=741)
G.add_edge(11, 5, weight=741)
G.add_edge(6, 11, weight=700)
G.add_edge(11, 6, weight=700)
G.add_edge(6, 10, weight=993)
G.add_edge(10, 6, weight=993)
G.add_edge(6, 9, weight=270)
G.add_edge(9, 6, weight=270)
G.add_edge(6, 8, weight=156)
G.add_edge(8, 6, weight=156)
G.add_edge(6, 7, weight=465)
G.add_edge(7, 6, weight=465)
G.add_edge(7, 8, weight=552)
G.add_edge(8, 7, weight=552)
G.add_edge(7, 9, weight=132)
G.add_edge(9, 7, weight=132)
G.add_edge(7, 10, weight=480)
G.add_edge(10, 7, weight=480)
G.add_edge(7, 11, weight=165)
G.add_edge(11, 7, weight=165)
G.add_edge(8, 11, weight=604)
G.add_edge(11, 8, weight=604)
G.add_edge(8, 10, weight=1339)
G.add_edge(10, 8, weight=1339)
# dict1 = {0: '哈尔滨', 1: '齐齐哈尔',2:'牡丹江',3:'佳木斯',4:'大庆',5:'鸡西'
# ,6:'双鸭山',7:'伊春',8:'七台河',9:'鹤岗',10:'黑河',11:'绥化'}
G.add_edge(8, 9, weight=383)
G.add_edge(9, 8, weight=383)
G.add_edge(9, 10, weight=829)
G.add_edge(10, 9, weight=829)
G.add_edge(9, 11, weight=423)
G.add_edge(11, 9, weight=423)
G.add_edge(11, 10, weight=500)
G.add_edge(10, 11, weight=500)
G.add_edge(0, 12, weight=375)
G.add_edge(12, 0, weight=375)
G.add_edge(0, 13, weight=251)
G.add_edge(13, 0, weight=251)
G.add_edge(0, 14, weight=499)
G.add_edge(14, 0, weight=499)
G.add_edge(0, 15, weight=838)
G.add_edge(15, 0, weight=838)
G.add_edge(0, 16, weight=840)
G.add_edge(16, 0, weight=840)
G.add_edge(0, 17, weight=700)
G.add_edge(17, 0, weight=700)
G.add_edge(0, 18, weight=626)
G.add_edge(18, 0, weight=626)
G.add_edge(0, 19, weight=185)
G.add_edge(19, 0, weight=185)
G.add_edge(0, 20, weight=876)
G.add_edge(20, 0, weight=876)
G.add_edge(0, 21, weight=1188)
G.add_edge(21, 0, weight=1188)
G.add_edge(0, 22, weight=1130)
G.add_edge(22, 0, weight=1130)
G.add_edge(0, 23, weight=1090)
G.add_edge(23, 0, weight=1090)
G.add_edge(0, 24, weight=1125)
G.add_edge(24, 0, weight=1125)
G.add_edge(0, 25, weight=1300)
G.add_edge(25, 0, weight=1300)
G.add_edge(0, 26, weight=1150)
G.add_edge(26, 0, weight=1150)
G.add_edge(0, 27, weight=1000)
G.add_edge(27, 0, weight=1000)
G.add_edge(0, 29, weight=900)
G.add_edge(29, 0, weight=900)
G.add_edge(0, 30, weight=811)
G.add_edge(30, 0, weight=811)
G.add_edge(0, 31, weight=800)
G.add_edge(31, 0, weight=800)
G.add_edge(0, 32, weight=990)
G.add_edge(32, 0, weight=990)
G.add_edge(0, 33, weight=1150)
G.add_edge(33, 0, weight=1150)
G.add_edge(1, 12, weight=800)
G.add_edge(12, 1, weight=800)
G.add_edge(1, 13, weight=820)
G.add_edge(13, 1, weight=820)
G.add_edge(1, 14, weight=930)
G.add_edge(14, 1, weight=930)
G.add_edge(1, 15, weight=1130)
G.add_edge(15, 1, weight=1130)
G.add_edge(1, 16, weight=1150)
G.add_edge(16, 1, weight=1150)
G.add_edge(1, 17, weight=950)
G.add_edge(17, 1, weight=950)
G.add_edge(1, 18, weight=250)
G.add_edge(18, 1, weight=250)
G.add_edge(1, 19, weight=533)
G.add_edge(19, 1, weight=533)
G.add_edge(1, 20, weight=1150)
G.add_edge(20, 1, weight=1150)
G.add_edge(1, 21, weight=1390)
G.add_edge(21, 1, weight=1390)
G.add_edge(1, 22, weight=1330)
G.add_edge(22, 1, weight=1330)
G.add_edge(1, 23, weight=1300)
G.add_edge(23, 1, weight=1300)
G.add_edge(1, 24, weight=1350)
G.add_edge(24, 1, weight=1350)
G.add_edge(1, 25, weight=1480)
G.add_edge(25, 1, weight=1480)
G.add_edge(1, 26, weight=1300)
G.add_edge(26, 1, weight=1300)
G.add_edge(1, 27, weight=1200)
G.add_edge(27, 1, weight=1200)
G.add_edge(1, 29, weight=1100)
G.add_edge(29, 1, weight=1100)
G.add_edge(1, 30, weight=1040)
G.add_edge(30, 1, weight=1040)
G.add_edge(1, 31, weight=1000)
G.add_edge(31, 1, weight=1000)
G.add_edge(1, 32, weight=1150)
G.add_edge(32, 1, weight=1150)
G.add_edge(1, 33, weight=1250)
G.add_edge(33, 1, weight=1250)
G.add_edge(2, 12, weight=658)
G.add_edge(12, 2, weight=658)
G.add_edge(2, 13, weight=349)
G.add_edge(13, 2, weight=349)
G.add_edge(2, 14, weight=767)
G.add_edge(14, 2, weight=767)
G.add_edge(2, 15, weight=832)
G.add_edge(15, 2, weight=832)
G.add_edge(2, 16, weight=451)
G.add_edge(16, 2, weight=451)
G.add_edge(2, 17, weight=778)
G.add_edge(17, 2, weight=778)
G.add_edge(2, 18, weight=986)
G.add_edge(18, 2, weight=986)
G.add_edge(2, 19, weight=807)
G.add_edge(19, 2, weight=807)
G.add_edge(2, 20, weight=996)
G.add_edge(20, 2, weight=996)
G.add_edge(2, 21, weight=1258)
G.add_edge(21, 2, weight=1258)
G.add_edge(2, 22, weight=1175)
G.add_edge(22, 2, weight=1175)
G.add_edge(2, 23, weight=1136)
G.add_edge(23, 2, weight=1136)
G.add_edge(2, 24, weight=1100)
G.add_edge(24, 2, weight=1100)
G.add_edge(2, 25, weight=1383)
G.add_edge(25, 2, weight=1383)
G.add_edge(2, 26, weight=1156)
G.add_edge(26, 2, weight=1156)
G.add_edge(2, 27, weight=1090)
G.add_edge(27, 2, weight=1090)
G.add_edge(2, 29, weight=1000)
G.add_edge(29, 2, weight=1000)
G.add_edge(2, 30, weight=950)
G.add_edge(30, 2, weight=950)
G.add_edge(2, 31, weight=940)
G.add_edge(31, 2, weight=940)
G.add_edge(2, 32, weight=1130)
G.add_edge(32, 2, weight=1130)
G.add_edge(2, 33, weight=1280)
G.add_edge(33, 2, weight=1280)
G.add_edge(3, 12, weight=950)
G.add_edge(12, 3, weight=950)
G.add_edge(3, 13, weight=525)
G.add_edge(13, 3, weight=525)
G.add_edge(3, 14, weight=1093)
G.add_edge(14, 3, weight=1093)
G.add_edge(3, 15, weight=1099)
G.add_edge(15, 3, weight=1099)
G.add_edge(3, 16, weight=1088)
G.add_edge(16, 3, weight=1088)
G.add_edge(3, 17, weight=1060)
G.add_edge(17, 3, weight=1060)
G.add_edge(3, 18, weight=1130)
G.add_edge(18, 3, weight=1130)
G.add_edge(3, 19, weight=573)
G.add_edge(19, 3, weight=573)
G.add_edge(3, 20, weight=1273)
G.add_edge(20, 3, weight=1273)
G.add_edge(3, 21, weight=1573)
G.add_edge(21, 3, weight=1573)
G.add_edge(3, 22, weight=1500)
G.add_edge(22, 3, weight=1500)
G.add_edge(3, 23, weight=1453)
G.add_edge(23, 3, weight=1453)
G.add_edge(3, 24, weight=1439)
G.add_edge(24, 3, weight=1439)
G.add_edge(3, 25, weight=1673)
G.add_edge(25, 3, weight=1673)
G.add_edge(3, 26, weight=1393)
G.add_edge(26, 3, weight=1393)
G.add_edge(3, 27, weight=1404)
G.add_edge(27, 3, weight=1404)
G.add_edge(3, 29, weight=1291)
G.add_edge(29, 3, weight=1291)
G.add_edge(3, 30, weight=1191)
G.add_edge(30, 3, weight=1191)
G.add_edge(3, 31, weight=1201)
G.add_edge(31, 3, weight=1201)
G.add_edge(3, 32, weight=1421)
G.add_edge(32, 3, weight=1421)
G.add_edge(3, 33, weight=1481)
G.add_edge(33, 3, weight=1481)
G.add_edge(4, 12, weight=505)
G.add_edge(12, 4, weight=505)
G.add_edge(4, 13, weight=523)
G.add_edge(13, 4, weight=523)
G.add_edge(4, 14, weight=628)
G.add_edge(14, 4, weight=628)
G.add_edge(4, 15, weight=755)
G.add_edge(15, 4, weight=755)
G.add_edge(4, 16, weight=896)
G.add_edge(16, 4, weight=896)
G.add_edge(4, 17, weight=656)
G.add_edge(17, 4, weight=656)
G.add_edge(4, 18, weight=365)
G.add_edge(18, 4, weight=365)
G.add_edge(4, 19, weight=178)
G.add_edge(19, 4, weight=178)
G.add_edge(4, 20, weight=919)
G.add_edge(20, 4, weight=919)
G.add_edge(4, 21, weight=1178)
G.add_edge(21, 4, weight=1178)
G.add_edge(4, 22, weight=1115)
G.add_edge(22, 4, weight=1115)
G.add_edge(4, 23, weight=1089)
G.add_edge(23, 4, weight=1089)
G.add_edge(4, 24, weight=1118)
G.add_edge(24, 4, weight=1118)
G.add_edge(4, 25, weight=1293)
G.add_edge(25, 4, weight=1293)
G.add_edge(4, 26, weight=1121)
G.add_edge(26, 4, weight=1121)
G.add_edge(4, 27, weight=978)
G.add_edge(27, 4, weight=978)
G.add_edge(4, 29, weight=925)
G.add_edge(29, 4, weight=925)
G.add_edge(4, 30, weight=875)
G.add_edge(30, 4, weight=875)
G.add_edge(4, 31, weight=855)
G.add_edge(31, 4, weight=855)
G.add_edge(4, 32, weight=937)
G.add_edge(32, 4, weight=937)
G.add_edge(4, 33, weight=1125)
G.add_edge(33, 4, weight=1125)

G.add_edge(5, 12, weight=858)
G.add_edge(12, 5, weight=858)
G.add_edge(5, 13, weight=599)
G.add_edge(13, 5, weight=599)
G.add_edge(5, 14, weight=967)
G.add_edge(14, 5, weight=967)
G.add_edge(5, 15, weight=1032)
G.add_edge(15, 5, weight=1032)
G.add_edge(5, 16, weight=651)
G.add_edge(16, 5, weight=651)
G.add_edge(5, 17, weight=978)
G.add_edge(17, 5, weight=978)
G.add_edge(5, 18, weight=1186)
G.add_edge(18, 5, weight=1186)
G.add_edge(5, 19, weight=1007)
G.add_edge(19, 5, weight=1007)
G.add_edge(5, 20, weight=1196)
G.add_edge(20, 5, weight=1196)
G.add_edge(5, 21, weight=1458)
G.add_edge(21, 5, weight=1458)
G.add_edge(5, 22, weight=1375)
G.add_edge(22, 5, weight=1375)
G.add_edge(5, 23, weight=1336)
G.add_edge(23, 5, weight=1336)
G.add_edge(5, 24, weight=1300)
G.add_edge(24, 5, weight=1300)
G.add_edge(5, 25, weight=1583)
G.add_edge(25, 5, weight=1583)
G.add_edge(5, 26, weight=1356)
G.add_edge(26, 5, weight=1356)
G.add_edge(5, 27, weight=1290)
G.add_edge(27, 5, weight=1290)
G.add_edge(5, 29, weight=1200)
G.add_edge(29, 5, weight=1200)
G.add_edge(5, 30, weight=1150)
G.add_edge(30, 5, weight=1150)
G.add_edge(5, 31, weight=1140)
G.add_edge(31, 5, weight=1140)
G.add_edge(5, 32, weight=1330)
G.add_edge(32, 5, weight=1330)
G.add_edge(5, 33, weight=1480)
G.add_edge(33, 5, weight=1480)

G.add_edge(6, 12, weight=1158)
G.add_edge(12, 6, weight=1158)
G.add_edge(6, 13, weight=899)
G.add_edge(13, 6, weight=899)
G.add_edge(6, 14, weight=1267)
G.add_edge(14, 6, weight=1267)
G.add_edge(6, 15, weight=1332)
G.add_edge(15, 6, weight=1332)
G.add_edge(6, 16, weight=951)
G.add_edge(16, 6, weight=951)
G.add_edge(6, 17, weight=1278)
G.add_edge(17, 6, weight=1278)
G.add_edge(6, 18, weight=1486)
G.add_edge(18, 6, weight=1486)
G.add_edge(6, 19, weight=1307)
G.add_edge(19, 6, weight=1307)
G.add_edge(6, 20, weight=1496)
G.add_edge(20, 6, weight=1496)
G.add_edge(6, 21, weight=1758)
G.add_edge(21, 6, weight=1758)
G.add_edge(6, 22, weight=1675)
G.add_edge(22, 6, weight=1675)
G.add_edge(6, 23, weight=1636)
G.add_edge(23, 6, weight=1636)
G.add_edge(6, 24, weight=1600)
G.add_edge(24, 6, weight=1600)
G.add_edge(6, 25, weight=1883)
G.add_edge(25, 6, weight=1883)
G.add_edge(6, 26, weight=1656)
G.add_edge(26, 6, weight=1656)
G.add_edge(6, 27, weight=1590)
G.add_edge(27, 6, weight=1590)
G.add_edge(6, 29, weight=1500)
G.add_edge(29, 6, weight=1500)
G.add_edge(6, 30, weight=1450)
G.add_edge(30, 6, weight=1450)
G.add_edge(6, 31, weight=1440)
G.add_edge(31, 6, weight=1440)
G.add_edge(6, 32, weight=1630)
G.add_edge(32, 6, weight=1630)
G.add_edge(6, 33, weight=1780)
G.add_edge(33, 6, weight=1780)

G.add_edge(7, 12, weight=675)
G.add_edge(12, 7, weight=675)
G.add_edge(7, 13, weight=551)
G.add_edge(13, 7, weight=551)
G.add_edge(7, 14, weight=799)
G.add_edge(14, 7, weight=799)
G.add_edge(7, 15, weight=1138)
G.add_edge(15, 7, weight=1138)
G.add_edge(7, 16, weight=1140)
G.add_edge(16, 7, weight=1140)
G.add_edge(7, 17, weight=1000)
G.add_edge(17, 7, weight=1000)
G.add_edge(7, 18, weight=926)
G.add_edge(18, 7, weight=926)
G.add_edge(7, 19, weight=485)
G.add_edge(19, 7, weight=485)
G.add_edge(7, 20, weight=1176)
G.add_edge(20, 7, weight=1176)
G.add_edge(7, 21, weight=1488)
G.add_edge(21, 7, weight=1488)
G.add_edge(7, 22, weight=1430)
G.add_edge(22, 7, weight=1430)
G.add_edge(7, 23, weight=1390)
G.add_edge(23, 7, weight=1390)
G.add_edge(7, 24, weight=1425)
G.add_edge(24, 7, weight=1425)
G.add_edge(7, 25, weight=1700)
G.add_edge(25, 7, weight=1700)
G.add_edge(7, 26, weight=1450)
G.add_edge(26, 7, weight=1450)
G.add_edge(7, 27, weight=1300)
G.add_edge(27, 7, weight=1300)
G.add_edge(7, 29, weight=1200)
G.add_edge(29, 7, weight=1200)
G.add_edge(7, 30, weight=1111)
G.add_edge(30, 7, weight=1111)
G.add_edge(7, 31, weight=1100)
G.add_edge(31, 7, weight=1100)
G.add_edge(7, 32, weight=1290)
G.add_edge(32, 7, weight=1290)
G.add_edge(7, 33, weight=1450)
G.add_edge(33, 7, weight=1450)

G.add_edge(8, 12, weight=958)
G.add_edge(12, 8, weight=958)
G.add_edge(8, 13, weight=699)
G.add_edge(13, 8, weight=699)
G.add_edge(8, 14, weight=1067)
G.add_edge(14, 8, weight=1067)
G.add_edge(8, 15, weight=1132)
G.add_edge(15, 8, weight=1132)
G.add_edge(8, 16, weight=751)
G.add_edge(16, 8, weight=751)
G.add_edge(8, 17, weight=1078)
G.add_edge(17, 8, weight=1078)
G.add_edge(8, 18, weight=1286)
G.add_edge(18, 8, weight=1286)
G.add_edge(8, 19, weight=1107)
G.add_edge(19, 8, weight=1107)
G.add_edge(8, 20, weight=1296)
G.add_edge(20, 8, weight=1296)
G.add_edge(8, 21, weight=1558)
G.add_edge(21, 8, weight=1558)
G.add_edge(8, 22, weight=1475)
G.add_edge(22, 8, weight=1475)
G.add_edge(8, 23, weight=1436)
G.add_edge(23, 8, weight=1436)
G.add_edge(8, 24, weight=1400)
G.add_edge(24, 8, weight=1400)
G.add_edge(8, 25, weight=1683)
G.add_edge(25, 8, weight=1683)
G.add_edge(8, 26, weight=1656)
G.add_edge(26, 8, weight=1656)
G.add_edge(8, 27, weight=1490)
G.add_edge(27, 8, weight=1490)
G.add_edge(8, 29, weight=1300)
G.add_edge(29, 8, weight=1300)
G.add_edge(8, 30, weight=1250)
G.add_edge(30, 8, weight=1250)
G.add_edge(8, 31, weight=1240)
G.add_edge(31, 8, weight=1240)
G.add_edge(8, 32, weight=1430)
G.add_edge(32, 8, weight=1430)
G.add_edge(8, 33, weight=1580)
G.add_edge(33, 8, weight=1580)

G.add_edge(9, 12, weight=1050)
G.add_edge(12, 9, weight=1050)
G.add_edge(9, 13, weight=625)
G.add_edge(13, 9, weight=625)
G.add_edge(9, 14, weight=1193)
G.add_edge(14, 9, weight=1193)
G.add_edge(9, 15, weight=1199)
G.add_edge(15, 9, weight=1199)
G.add_edge(9, 16, weight=1188)
G.add_edge(16, 9, weight=1188)
G.add_edge(9, 17, weight=1160)
G.add_edge(17, 9, weight=1160)
G.add_edge(9, 18, weight=1230)
G.add_edge(18, 9, weight=1230)
G.add_edge(9, 19, weight=673)
G.add_edge(19, 9, weight=673)
G.add_edge(9, 20, weight=1373)
G.add_edge(20, 9, weight=1373)
G.add_edge(9, 21, weight=1673)
G.add_edge(21, 9, weight=1673)
G.add_edge(9, 22, weight=1600)
G.add_edge(22, 9, weight=1600)
G.add_edge(9, 23, weight=1553)
G.add_edge(23, 9, weight=1553)
G.add_edge(9, 24, weight=1539)
G.add_edge(24, 9, weight=1539)
G.add_edge(9, 25, weight=1773)
G.add_edge(25, 9, weight=1773)
G.add_edge(9, 26, weight=1493)
G.add_edge(26, 9, weight=1493)
G.add_edge(9, 27, weight=1504)
G.add_edge(27, 9, weight=1504)
G.add_edge(9, 29, weight=1391)
G.add_edge(29, 9, weight=1391)
G.add_edge(9, 30, weight=1291)
G.add_edge(30, 9, weight=1291)
G.add_edge(9, 31, weight=1301)
G.add_edge(31, 9, weight=1301)
G.add_edge(9, 32, weight=1521)
G.add_edge(32, 9, weight=1521)
G.add_edge(9, 33, weight=1581)
G.add_edge(33, 9, weight=1581)

G.add_edge(10, 12, weight=1075)
G.add_edge(12, 10, weight=1075)
G.add_edge(10, 13, weight=951)
G.add_edge(13, 10, weight=951)
G.add_edge(10, 14, weight=1199)
G.add_edge(14, 10, weight=199)
G.add_edge(10, 15, weight=1538)
G.add_edge(15, 10, weight=1538)
G.add_edge(10, 16, weight=1540)
G.add_edge(16, 10, weight=1540)
G.add_edge(10, 17, weight=1400)
G.add_edge(17, 10, weight=1400)
G.add_edge(10, 18, weight=1326)
G.add_edge(18, 10, weight=1326)
G.add_edge(10, 19, weight=885)
G.add_edge(19, 10, weight=885)
G.add_edge(10, 20, weight=1576)
G.add_edge(20, 10, weight=1576)
G.add_edge(10, 21, weight=1888)
G.add_edge(21, 10, weight=1888)
G.add_edge(10, 22, weight=1830)
G.add_edge(22, 10, weight=1830)
G.add_edge(10, 23, weight=1790)
G.add_edge(23, 10, weight=1790)
G.add_edge(10, 24, weight=1825)
G.add_edge(24, 10, weight=1825)
G.add_edge(10, 25, weight=2000)
G.add_edge(25, 10, weight=2000)
G.add_edge(10, 26, weight=1850)
G.add_edge(26, 10, weight=1850)
G.add_edge(10, 27, weight=1700)
G.add_edge(27, 10, weight=1700)
G.add_edge(10, 29, weight=1600)
G.add_edge(29, 10, weight=1600)
G.add_edge(10, 30, weight=1511)
G.add_edge(30, 10, weight=1511)
G.add_edge(10, 31, weight=1500)
G.add_edge(31, 10, weight=1500)
G.add_edge(10, 32, weight=1690)
G.add_edge(32, 10, weight=1690)
G.add_edge(10, 33, weight=1850)
G.add_edge(33, 10, weight=1850)

G.add_edge(11, 12, weight=575)
G.add_edge(12, 11, weight=575)
G.add_edge(11, 13, weight=451)
G.add_edge(13, 11, weight=451)
G.add_edge(11, 14, weight=699)
G.add_edge(14, 11, weight=699)
G.add_edge(11, 15, weight=1038)
G.add_edge(15, 11, weight=1038)
G.add_edge(11, 16, weight=1040)
G.add_edge(16, 11, weight=1040)
G.add_edge(11, 17, weight=900)
G.add_edge(17, 11, weight=900)
G.add_edge(11, 18, weight=826)
G.add_edge(18, 11, weight=826)
G.add_edge(11, 19, weight=385)
G.add_edge(19, 11, weight=385)
G.add_edge(11, 20, weight=1076)
G.add_edge(20, 11, weight=1076)
G.add_edge(11, 21, weight=1388)
G.add_edge(21, 11, weight=1388)
G.add_edge(11, 22, weight=1330)
G.add_edge(22, 11, weight=1330)
G.add_edge(11, 23, weight=1290)
G.add_edge(23, 11, weight=1290)
G.add_edge(11, 24, weight=1225)
G.add_edge(24, 11, weight=1225)
G.add_edge(11, 25, weight=1500)
G.add_edge(25, 11, weight=1500)
G.add_edge(11, 26, weight=1450)
G.add_edge(26, 11, weight=1450)
G.add_edge(11, 27, weight=1300)
G.add_edge(27, 11, weight=1300)
G.add_edge(11, 29, weight=1100)
G.add_edge(29, 11, weight=1100)
G.add_edge(11, 30, weight=1111)
G.add_edge(30, 11, weight=1111)
G.add_edge(11, 31, weight=1000)
G.add_edge(31, 11, weight=1000)
G.add_edge(11, 32, weight=1190)
G.add_edge(32, 11, weight=1190)
G.add_edge(11, 33, weight=1350)
G.add_edge(33, 11, weight=1350)

G.add_edge(12, 13, weight=113)
G.add_edge(13, 12, weight=113)
G.add_edge(12, 14, weight=119)
G.add_edge(14, 12, weight=119)
G.add_edge(12, 15, weight=363)
G.add_edge(15, 12, weight=363)
G.add_edge(12, 16, weight=365)
G.add_edge(16, 12, weight=365)
G.add_edge(12, 17, weight=114)
G.add_edge(17, 12, weight=114)
G.add_edge(12, 18, weight=449)
G.add_edge(18, 12, weight=449)
G.add_edge(12, 19, weight=171)
G.add_edge(19, 12, weight=171)
G.add_edge(12, 20, weight=441)
G.add_edge(20, 12, weight=441)
G.add_edge(12, 21, weight=771)
G.add_edge(21, 12, weight=771)
G.add_edge(12, 22, weight=723)
G.add_edge(22, 12, weight=723)
G.add_edge(12, 23, weight=712)
G.add_edge(23, 12, weight=712)
G.add_edge(12, 24, weight=709)
G.add_edge(24, 12, weight=709)
G.add_edge(12, 25, weight=974)
G.add_edge(25, 12, weight=974)
G.add_edge(12, 26, weight=788)
G.add_edge(26, 12, weight=788)
G.add_edge(12, 27, weight=647)
G.add_edge(27, 12, weight=647)
G.add_edge(12, 29, weight=474)
G.add_edge(29, 12, weight=474)
G.add_edge(12, 31, weight=396)
G.add_edge(31, 12, weight=396)
G.add_edge(12, 30, weight=447)
G.add_edge(30, 12, weight=447)
G.add_edge(12, 32, weight=574)
G.add_edge(32, 12, weight=574)
G.add_edge(12, 33, weight=770)
G.add_edge(33, 12, weight=770)
G.add_edge(13, 14, weight=325)
G.add_edge(14, 13, weight=325)
G.add_edge(13, 15, weight=278)
G.add_edge(15, 13, weight=278)
G.add_edge(13, 16, weight=261)
G.add_edge(16, 13, weight=261)
G.add_edge(13, 17, weight=222)
G.add_edge(17, 13, weight=222)
G.add_edge(13, 18, weight=544)
G.add_edge(18, 13, weight=544)
G.add_edge(13, 19, weight=266)
G.add_edge(19, 13, weight=266)
G.add_edge(13, 20, weight=548)
G.add_edge(20, 13, weight=548)
G.add_edge(13, 21, weight=871)
G.add_edge(21, 13, weight=871)
G.add_edge(13, 22, weight=818)
G.add_edge(22, 13, weight=818)
G.add_edge(13, 23, weight=801)
G.add_edge(23, 13, weight=801)
G.add_edge(13, 24, weight=823)
G.add_edge(24, 13, weight=823)
G.add_edge(13, 25, weight=1018)
G.add_edge(25, 13, weight=1018)
G.add_edge(13, 26, weight=849)
G.add_edge(26, 13, weight=849)
G.add_edge(13, 27, weight=717)
G.add_edge(27, 13, weight=717)
G.add_edge(13, 29, weight=741)
G.add_edge(29, 13, weight=741)
G.add_edge(13, 30, weight=541)
G.add_edge(30, 13, weight=541)
G.add_edge(13, 31, weight=534)
G.add_edge(31, 13, weight=534)
G.add_edge(13, 32, weight=753)
G.add_edge(32, 13, weight=753)
G.add_edge(13, 33, weight=901)
G.add_edge(33, 13, weight=901)
G.add_edge(14, 15, weight=359)
G.add_edge(15, 14, weight=359)
G.add_edge(14, 16, weight=538)
G.add_edge(16, 14, weight=538)
G.add_edge(14, 17, weight=84)
G.add_edge(17, 14, weight=84)
G.add_edge(14, 18, weight=466)
G.add_edge(18, 14, weight=466)
G.add_edge(14, 19, weight=407)
G.add_edge(19, 14, weight=407)
G.add_edge(14, 20, weight=348)
G.add_edge(20, 14, weight=348)
G.add_edge(14, 21, weight=563)
G.add_edge(21, 14, weight=563)
G.add_edge(14, 22, weight=567)
G.add_edge(22, 14, weight=567)
G.add_edge(14, 23, weight=557)
G.add_edge(23, 14, weight=557)
G.add_edge(14, 24, weight=569)
G.add_edge(24, 14, weight=569)
G.add_edge(14, 25, weight=817)
G.add_edge(25, 14, weight=817)
G.add_edge(14, 26, weight=636)
G.add_edge(26, 14, weight=636)
G.add_edge(14, 27, weight=501)
G.add_edge(27, 14, weight=501)
G.add_edge(14, 29, weight=381)
G.add_edge(29, 14, weight=381)
G.add_edge(14, 30, weight=197)
G.add_edge(30, 14, weight=197)
G.add_edge(14, 31, weight=137)
G.add_edge(31, 14, weight=137)
G.add_edge(14, 32, weight=441)
G.add_edge(32, 14, weight=441)
G.add_edge(14, 33, weight=595)
G.add_edge(33, 14, weight=595)
G.add_edge(15, 16, weight=58.5)
G.add_edge(16, 15, weight=58.5)
G.add_edge(15, 17, weight=176)
G.add_edge(17, 15, weight=176)
G.add_edge(15, 18, weight=813)
G.add_edge(18, 15, weight=813)
G.add_edge(15, 19, weight=534)
G.add_edge(19, 15, weight=534)
G.add_edge(15, 20, weight=375)
G.add_edge(20, 15, weight=375)
G.add_edge(15, 21, weight=834)
G.add_edge(21, 15, weight=834)
G.add_edge(15, 22, weight=778)
G.add_edge(22, 15, weight=778)
G.add_edge(15, 23, weight=704)
G.add_edge(23, 15, weight=704)
G.add_edge(15, 24, weight=595)
G.add_edge(24, 15, weight=595)
G.add_edge(15, 25, weight=879)
G.add_edge(25, 15, weight=879)
G.add_edge(15, 26, weight=274)
G.add_edge(26, 15, weight=274)
G.add_edge(15, 27, weight=556)
G.add_edge(27, 15, weight=556)
G.add_edge(15, 29, weight=408)
G.add_edge(29, 15, weight=408)
G.add_edge(15, 30, weight=217)
G.add_edge(30, 15, weight=217)
G.add_edge(15, 31, weight=309)
G.add_edge(31, 15, weight=309)
G.add_edge(15, 32, weight=720)
G.add_edge(32, 15, weight=720)
G.add_edge(15, 33, weight=786)
G.add_edge(33, 15, weight=786)

G.add_edge(16, 17, weight=200)
G.add_edge(17, 16, weight=200)
G.add_edge(16, 18, weight=814)
G.add_edge(18, 16, weight=814)
G.add_edge(16, 19, weight=536)
G.add_edge(19, 16, weight=536)
G.add_edge(16, 20, weight=515)
G.add_edge(20, 16, weight=515)
G.add_edge(16, 21, weight=946)
G.add_edge(21, 16, weight=946)
G.add_edge(16, 23, weight=772)
G.add_edge(23, 16, weight=772)
G.add_edge(16, 22, weight=900)
G.add_edge(22, 16, weight=900)
G.add_edge(16, 24, weight=765)
G.add_edge(24, 16, weight=765)
G.add_edge(16, 25, weight=950)
G.add_edge(25, 16, weight=950)
G.add_edge(16, 26, weight=505)
G.add_edge(26, 16, weight=505)
G.add_edge(16, 27, weight=712)
G.add_edge(27, 16, weight=712)
G.add_edge(16, 29, weight=546)
G.add_edge(29, 16, weight=546)
G.add_edge(16, 30, weight=457)
G.add_edge(30, 16, weight=457)
G.add_edge(16, 32, weight=787)
G.add_edge(32, 16, weight=787)
G.add_edge(16, 31, weight=499)
G.add_edge(31, 16, weight=499)
G.add_edge(16, 33, weight=856)
G.add_edge(33, 16, weight=856)

G.add_edge(17, 18, weight=563)
G.add_edge(18, 17, weight=563)
G.add_edge(17, 19, weight=384)
G.add_edge(19, 17, weight=384)
G.add_edge(17, 20, weight=370)
G.add_edge(20, 17, weight=370)
G.add_edge(17, 21, weight=730)
G.add_edge(21, 17, weight=730)
G.add_edge(17, 22, weight=575)
G.add_edge(22, 17, weight=575)
G.add_edge(17, 23, weight=532)
G.add_edge(23, 17, weight=532)
G.add_edge(17, 24, weight=554)
G.add_edge(24, 17, weight=554)
G.add_edge(17, 25, weight=916)
G.add_edge(25, 17, weight=916)
G.add_edge(17, 26, weight=579)
G.add_edge(26, 17, weight=579)
G.add_edge(17, 27, weight=477)
G.add_edge(27, 17, weight=477)
G.add_edge(17, 29, weight=420)
G.add_edge(29, 17, weight=420)
G.add_edge(17, 30, weight=225)
G.add_edge(30, 17, weight=225)
G.add_edge(17, 31, weight=165)
G.add_edge(31, 17, weight=165)
G.add_edge(17, 32, weight=500)
G.add_edge(32, 17, weight=500)
G.add_edge(17, 33, weight=673)
G.add_edge(33, 17, weight=673)

G.add_edge(18, 19, weight=193)
G.add_edge(19, 18, weight=193)
G.add_edge(18, 20, weight=940)
G.add_edge(20, 18, weight=940)
G.add_edge(18, 21, weight=1101)
G.add_edge(21, 18, weight=1101)
G.add_edge(18, 22, weight=1055)
G.add_edge(22, 18, weight=1055)
G.add_edge(18, 23, weight=966)
G.add_edge(23, 18, weight=966)
G.add_edge(18, 24, weight=1028)
G.add_edge(24, 18, weight=1028)
G.add_edge(18, 25, weight=1343)
G.add_edge(25, 18, weight=1343)
G.add_edge(18, 26, weight=1088)
G.add_edge(26, 18, weight=1088)
G.add_edge(18, 27, weight=974)
G.add_edge(27, 18, weight=974)
G.add_edge(18, 29, weight=965)
G.add_edge(29, 18, weight=965)
G.add_edge(18, 30, weight=862)
G.add_edge(30, 18, weight=862)
G.add_edge(18, 31, weight=780)
G.add_edge(31, 18, weight=780)
G.add_edge(18, 32, weight=924)
G.add_edge(32, 18, weight=924)
G.add_edge(18, 33, weight=970)
G.add_edge(33, 18, weight=970)

G.add_edge(19, 20, weight=761)
G.add_edge(20, 19, weight=761)
G.add_edge(19, 21, weight=922)
G.add_edge(21, 19, weight=922)
G.add_edge(19, 22, weight=876)
G.add_edge(22, 19, weight=876)
G.add_edge(19, 23, weight=804)
G.add_edge(23, 19, weight=804)
G.add_edge(19, 24, weight=844)
G.add_edge(24, 19, weight=844)
G.add_edge(19, 25, weight=1081)
G.add_edge(25, 19, weight=1081)
G.add_edge(19, 26, weight=909)
G.add_edge(26, 19, weight=909)
G.add_edge(19, 27, weight=756)
G.add_edge(27, 19, weight=756)
G.add_edge(19, 29, weight=786)
G.add_edge(29, 19, weight=786)
G.add_edge(19, 30, weight=703)
G.add_edge(30, 19, weight=703)
G.add_edge(19, 31, weight=503)
G.add_edge(31, 19, weight=503)
G.add_edge(19, 32, weight=745)
G.add_edge(32, 19, weight=745)
G.add_edge(19, 33, weight=868)
G.add_edge(33, 19, weight=868)

G.add_edge(20, 21, weight=438)
G.add_edge(21, 20, weight=438)
G.add_edge(20, 22, weight=392)
G.add_edge(22, 20, weight=392)
G.add_edge(20, 23, weight=177)
G.add_edge(23, 20, weight=177)
G.add_edge(20, 24, weight=177)
G.add_edge(24, 20, weight=177)
G.add_edge(20, 25, weight=554)
G.add_edge(25, 20, weight=554)
G.add_edge(20, 26, weight=344)
G.add_edge(26, 20, weight=344)
G.add_edge(20, 27, weight=87)
G.add_edge(27, 20, weight=87)
G.add_edge(20, 29, weight=35)
G.add_edge(29, 20, weight=35)
G.add_edge(20, 30, weight=67)
G.add_edge(30, 20, weight=67)
G.add_edge(20, 31, weight=75)
G.add_edge(31, 20, weight=75)
G.add_edge(20, 32, weight=215)
G.add_edge(32, 20, weight=215)
G.add_edge(20, 33, weight=484)
G.add_edge(33, 20, weight=484)

G.add_edge(21, 22, weight=55)
G.add_edge(22, 21, weight=55)
G.add_edge(21, 23, weight=246)
G.add_edge(23, 21, weight=246)
G.add_edge(21, 24, weight=308)
G.add_edge(24, 21, weight=308)
G.add_edge(21, 25, weight=600)
G.add_edge(25, 21, weight=600)
G.add_edge(21, 26, weight=583)
G.add_edge(26, 21, weight=583)
G.add_edge(21, 27, weight=363)
G.add_edge(27, 21, weight=363)
G.add_edge(21, 29, weight=417)
G.add_edge(29, 21, weight=417)
G.add_edge(21, 30, weight=503)
G.add_edge(30, 21, weight=503)
G.add_edge(21, 31, weight=510)
G.add_edge(31, 21, weight=510)
G.add_edge(21, 32, weight=335)
G.add_edge(32, 21, weight=335)
G.add_edge(21, 33, weight=145)
G.add_edge(33, 21, weight=145)

G.add_edge(22, 23, weight=94)
G.add_edge(23, 22, weight=94)
G.add_edge(22, 24, weight=148)
G.add_edge(24, 22, weight=148)
G.add_edge(22, 25, weight=478)
G.add_edge(25, 22, weight=478)
G.add_edge(22, 26, weight=538)
G.add_edge(26, 22, weight=538)
G.add_edge(22, 27, weight=318)
G.add_edge(27, 22, weight=318)
G.add_edge(22, 29, weight=373)
G.add_edge(29, 22, weight=373)
G.add_edge(22, 30, weight=458)
G.add_edge(30, 22, weight=458)
G.add_edge(22, 31, weight=398)
G.add_edge(31, 22, weight=398)
G.add_edge(22, 32, weight=124)
G.add_edge(32, 22, weight=124)
G.add_edge(22, 33, weight=92)
G.add_edge(33, 22, weight=92)

G.add_edge(23, 24, weight=60)
G.add_edge(24, 23, weight=60)
G.add_edge(23, 25, weight=463)
G.add_edge(25, 23, weight=463)
G.add_edge(23, 26, weight=446)
G.add_edge(26, 23, weight=446)
G.add_edge(23, 27, weight=96)
G.add_edge(27, 23, weight=96)
G.add_edge(23, 29, weight=303)
G.add_edge(29, 23, weight=303)
G.add_edge(23, 30, weight=366)
G.add_edge(30, 23, weight=366)
G.add_edge(23, 31, weight=362)
G.add_edge(31, 23, weight=362)
G.add_edge(23, 32, weight=131)
G.add_edge(32, 23, weight=131)
G.add_edge(23, 33, weight=292)
G.add_edge(33, 23, weight=292)

G.add_edge(24, 25, weight=219)
G.add_edge(25, 24, weight=219)
G.add_edge(24, 26, weight=264)
G.add_edge(26, 24, weight=264)
G.add_edge(24, 27, weight=94)
G.add_edge(27, 24, weight=94)
G.add_edge(24, 29, weight=322)
G.add_edge(29, 24, weight=322)
G.add_edge(24, 30, weight=390)
G.add_edge(30, 24, weight=390)
G.add_edge(24, 31, weight=399)
G.add_edge(31, 24, weight=399)
G.add_edge(24, 32, weight=297)
G.add_edge(32, 24, weight=297)
G.add_edge(24, 33, weight=357)
G.add_edge(33, 24, weight=357)

G.add_edge(25, 26, weight=303)
G.add_edge(26, 25, weight=303)
G.add_edge(25, 27, weight=397)
G.add_edge(27, 25, weight=397)
G.add_edge(25, 29, weight=519)
G.add_edge(29, 25, weight=519)
G.add_edge(25, 30, weight=541)
G.add_edge(30, 25, weight=541)
G.add_edge(25, 31, weight=548)
G.add_edge(31, 25, weight=548)
G.add_edge(25, 32, weight=511)
G.add_edge(32, 25, weight=511)
G.add_edge(25, 33, weight=570)
G.add_edge(33, 25, weight=570)

G.add_edge(26, 27, weight=250)
G.add_edge(27, 26, weight=250)
G.add_edge(26, 29, weight=213)
G.add_edge(29, 26, weight=213)
G.add_edge(26, 30, weight=329)
G.add_edge(30, 26, weight=329)
G.add_edge(26, 31, weight=413)
G.add_edge(31, 26, weight=413)
G.add_edge(26, 32, weight=559)
G.add_edge(32, 26, weight=559)
G.add_edge(26, 33, weight=730)
G.add_edge(33, 26, weight=730)

G.add_edge(27, 29, weight=92)
G.add_edge(29, 27, weight=92)
G.add_edge(27, 30, weight=265)
G.add_edge(30, 27, weight=265)
G.add_edge(27, 31, weight=272)
G.add_edge(31, 27, weight=272)
G.add_edge(27, 32, weight=203)
G.add_edge(32, 27, weight=203)
G.add_edge(27, 33, weight=411)
G.add_edge(33, 27, weight=411)

G.add_edge(29, 30, weight=63)
G.add_edge(30, 29, weight=63)
G.add_edge(29, 31, weight=157)
G.add_edge(31, 29, weight=157)
G.add_edge(29, 32, weight=354)
G.add_edge(32, 29, weight=354)
G.add_edge(29, 33, weight=452)
G.add_edge(33, 29, weight=452)

G.add_edge(30, 31, weight=60)
G.add_edge(31, 30, weight=60)
G.add_edge(30, 32, weight=342)
G.add_edge(32, 30, weight=342)
G.add_edge(30, 33, weight=474)
G.add_edge(33, 30, weight=474)

G.add_edge(31, 32, weight=219)
G.add_edge(32, 31, weight=219)
G.add_edge(31, 33, weight=442)
G.add_edge(33, 31, weight=442)

G.add_edge(33, 32, weight=138)
G.add_edge(32, 33, weight=138)

'''
dict1 = {0: '哈尔滨', 1: '齐齐哈尔',2:'牡丹江',3:'佳木斯',4:'大庆',5:'鸡西',6:'双鸭山',
7:'伊春',8:'七台河',9:'鹤岗',10:'黑河',11:'绥化',12:'长春',13:'吉林',14:'四平',15:'通化',
16:'白山',17:'辽源',18:'白城',19:'松原',20:'沈阳',21:'葫芦岛',22:'锦州',23:'盘锦', 
24:'营口',25:'大连市',26:'丹东',27:'鞍山',29:'本溪市',30:'抚顺',31:'铁岭',32:'阜新',33:'朝阳'}
'''
'''
黑龙江：哈尔滨，齐齐哈尔，牡丹江，佳木斯，大庆，鸡西，双鸭山，伊春，七台河，鹤岗，黑河，绥化
辽宁：沈阳葫芦岛市 锦州市 盘锦市 营口市 大连市 丹东市 鞍山市 本溪市 抚顺市 铁岭市 阜新市 朝阳市 
吉林：长春、吉林、四平、通化、白山、辽源、白城、松原
'''
dict1 = {0: '哈尔滨', 1: '齐齐哈尔',2:'牡丹江',3:'佳木斯',4:'大庆',5:'鸡西',6:'双鸭山',7:'伊春',8:'七台河',9:'鹤岗',10:'黑河',11:'绥化',12:'长春',13:'吉林',14:'四平',15:'通化',16:'白山',17:'辽源',18:'白城',19:'松原',20:'沈阳',21:'葫芦岛',22:'锦州',23:'盘锦', 24:'营口',25:'大连',26:'丹东',27:'鞍山',28:'',29:'本溪',30:'抚顺',31:'铁岭',32:'阜新',33:'朝阳'}
rs1 = []
start1 = '齐齐哈尔'
end1 = '丹东'
for i in range(len(dict1)):
    if dict1[i] == start1:
        start2 = i
    if dict1[i] == end1:
        end2 = i
rs, ds = Dijkstra(G, start2, end2)
print(rs,type(ds))
for i in rs:
    rs1.append(dict1[i])
print(rs1)
print(ds)
