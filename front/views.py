



#第一部分，，首页以及路径城市详情页
import json

from django.shortcuts import render,redirect,reverse
from django.db import connection
from django.http import HttpResponse

from front.baidufanyi import baidu_translate
from front.dj import dict1, Dijkstra, G


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

def getcursor():
    return connection.cursor()
def index(request):
    cursor=getcursor()
    cursor.execute('select * from dj order by id limit 14')
    infos=cursor.fetchall()
    # return HttpResponse('123')
    return render(request,'index.html',context={'infos':infos})

def dj_detail(request,dj_id):
    try:
        cursor=getcursor()
        cursor.execute("select cities from dj where id ='%s'"%dj_id)
        # city=cursor.fetchone()
        cities=str(cursor.fetchone())
        cursor = getcursor()
        cursor.execute("select id from dj where id ='%s'" %dj_id)
        city01=cursor.fetchone()
        id=city01[0]
        print(city01)
        #citier打印出来是（’长春，哈尔滨，‘），所以要截取
        # print(type(cities))
        # print(cities)
        city=cities[2:-3]
        # print('8888888888')
        # print(city)
        length = len(city)
        try:
            city_list=city.split(',')
            print(city_list)
            print(type(city_list))
            # print(length)
            list1=range(length)
            return render(request,'dj_detail.html',context={'cities':city_list,'id':id})
        except Exception as e:
            return render(request,'error_tail.html',context={'e':e})
    except Exception as e:
        return render(request, 'time_out_view.html', context={'e': e})

def dj_detail_two(request,city_list):
    # print('123456789')
    # print(city_list)
    # print(type(city_list))
    str1=''
    for i in city_list:
        if i==',' or is_Chinese(i):
            str1+=i
    # print(str1)
    city_list=str1.split(',')
    # print(city_list)
    # print(type(city_list))
    try:
        try:
            return render(request,'dj_detail.html',context={'cities':city_list})
        except Exception as e:
            return render(request,'error_tail.html',context={'e':e})
    except Exception as e:
        return render(request, 'time_out_view.html', context={'e': e})
def dj_delete(request):
    if request.method=='POST':
        city01=request.POST.get('city01')
        cursor=getcursor()
        cursor.execute("delete from dj where id='%s'" %city01)
        return redirect(reverse('index'))
# def dj_view(request,city):
#     #http://s.lvmama.com/ticket/?keyword=%E4%B8%8A%E6%B5%B7
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
#     }
#     city = urllib.parse.quote(city)
#     url = 'http://s.lvmama.com/ticket/?keyword=' + city
#     # print(url)
#     try:
#         response = urllib.request.urlopen(url)
#         content = response.read().decode('utf-8')
#         content=content.replace('>上海<','>哈尔滨<')
#         with open('templates/dj1.html', 'w', encoding='utf-8')as fp:
#             fp.write(content)
#         return render(request, 'dj1.html', context={'city': city})
#     except:
#         return render(request,'time_out_view.html')
def dj_kinds(request,city):
    return render(request,'dj_kinds.html',context={'city':city})
# def dj_view(request,city):
#     # get_url='.mipang.com/jingdian/'
#     get_url='http://piao.qunar.com/ticket/list.htm?keyword='
#     get_url2='&region=&from=mps_search_suggest'
#     # from xpinyin import Pinyin
#     # p= Pinyin()
#     # pinyin=p.get_pinyin(city)
#     # str1=''
#     # for i in pinyin:
#     #     if i!='-':
#     #         str1+=i
#     # # print(str1)
#     # url='http://'+str1+get_url
#     import urllib.request
#     import urllib.parse
#     # import urllib.parse
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
#     }
#     # city=urllib.parse.urlencode(city)
#     city=urllib.parse.quote(city)
#     # print(city)
#     # request=urllib.request.Request(url=url,headers=headers)
#     # response=urllib.request.urlopen(url)
#     # print(response.read())
#     # content=urllib.request.
#     # with open('di_.html','w',encoding='utf-8')as fp:
#     # url='http://suzhou.mipang.com'
#     url=get_url+city+get_url2
#     # print(url)
#     response = urllib.request.urlopen(url)
#     content=response.read().decode('utf-8')
#     content=content.replace('action="/ticket/list.htm"', 'action="#"')
#     for i in range(len(content)):
#         # href = "/ticket/detail_1086665726
#         if content[i:i+15]=='"/ticket/detail':
#         # if content[i:i+6]=='ticket':
#             content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
#             i+=200
#         elif content[i:i+14]=='"/ticket/list_':
#             content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
#             i += 10
#         # elif content[i:i+17]=='data-pager-pageno':
#         #     content=content[:i]+' target="_self" hidefocus="true"'+content[i:]
#         #     i += 100
#             # print('********')
#     with open('templates/dj1.html','w',encoding='utf-8')as fp:
#         fp.write(content)
#     # urllib.request.urlretrieve(url=url,filename='templates/dj1.html')
#     # return HttpResponse('123')
#     import time
#     # time.sleep(3)
#     return render(request,'dj1.html',context={'city':city})

def dj_view(request,city):
    try:
        if city=='七台河':
            city=city
        else:
            city=city+'古迹'
        print('99999999999999')
        get_url='http://piao.qunar.com/ticket/list.htm?keyword='
        get_url2='&region=&from=mps_search_suggest'
        import urllib.parse
        # import urllib.parse
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
        }
        city=urllib.parse.quote(city)
        # end=urllib.parse.quote(end)
        url=get_url+city+get_url2
        print(url)
        response = urllib.request.urlopen(url)
        content=response.read().decode('utf-8')
        content=content.replace('action="/ticket/list.htm"', 'action="#"')
        for i in range(len(content)):
        # href = "/ticket/detail_1086665726
            if content[i:i+15]=='"/ticket/detail':
            # if content[i:i+6]=='ticket':
                content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
                i+=100
            elif content[i:i+14]=='"/ticket/list_':
                content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
                i += 10
            elif content[i:i+17]=='data-pager-pageno':
                content=content[:i]+' target="_self" hidefocus="true"'+content[i:]
                i += 100
                print('********')
        for i in range(len(content)):

            if content[i:i+27]=='class="mp-search-container"':
                content = content.replace('class="mp-search-container"', 'class="mp-search-container" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
        #     elif content[i:i + 15] == '"/ticket/detail':
        # # if content[i:i+6]=='ticket':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i+=200
        #     elif content[i:i+14]=='"/ticket/list_':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i += 10
        for i in range(len(content)):
            if content[i:i+15]=='class="section"':
                content = content.replace('class="section"','class="section" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
                i += 100

        content = content.replace('48','5', 1)
        # for i in range(len(content)):
        #     if content[i:i+15]=='class ="piao_menu"':
        #         content = content.replace('class ="piao_menu"', 'class ="piao_menu" style="display:none;"', 1)
                # i += 100
        for i in range(len(content)):
            if content[i:i + 13] == 'data-original':
                content=content.replace('data-original','src')
                i += 100
            # if content[i:i+4]=="href":
            #     content = content[0:i] + 'href="#" ' + content[i:]
            if content[i:i+4]=='超值低价':
                print('12345789')
                content=content[0:i-158]
        for i in range(len(content)):
            if content[i:i + 26] == 'class="index_order clrfix"':
                content = content.replace('class="index_order clrfix"','class="index_order clrfix" style="visibility:hidden;" ',1)
                i += 1000

        for i in range(len(content)):
            # content=content.replace('href','alt')
            if content[i:i + 21] == 'class="q_header_main"':
                content=content.replace('class="q_header_main"','class="q_header_main" style="display:none;" ')
                # content = content[0:i] + 'style="display:none;" ' + content[i:]
                i+=1000
        with open('templates/dj1.html','w',encoding='utf-8')as fp:
            fp.write(content)
        return render(request,'dj1.html',context={'city':city})
    except Exception as e:
        print('25252525')
        return render(request,'fanhui.html')

def dj_view_one(request, city):
    try:
        # if city == '七台河':
        #     city = city
        # else:
        city = city + '风景区'
        print('99999999999999')
        get_url = 'http://piao.qunar.com/ticket/list.htm?keyword='
        get_url2 = '&region=&from=mps_search_suggest'
        import urllib.parse
        # import urllib.parse
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
        }
        city = urllib.parse.quote(city)
        # end=urllib.parse.quote(end)
        url = get_url + city + get_url2
        print(url)
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        content = content.replace('action="/ticket/list.htm"', 'action="#"')
        for i in range(len(content)):
            # href = "/ticket/detail_1086665726
            if content[i:i + 15] == '"/ticket/detail':
                # if content[i:i+6]=='ticket':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 100
            elif content[i:i + 14] == '"/ticket/list_':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 10
            elif content[i:i + 17] == 'data-pager-pageno':
                content = content[:i] + ' target="_self" hidefocus="true"' + content[i:]
                i += 100
                print('********')
        for i in range(len(content)):

            if content[i:i + 27] == 'class="mp-search-container"':
                content = content.replace('class="mp-search-container"',
                                          'class="mp-search-container" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
        # elif content[i:i + 15] == '"/ticket/detail':
        # # if content[i:i+6]=='ticket':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i+=200
        #     elif content[i:i+14]=='"/ticket/list_':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i += 10
        for i in range(len(content)):
            if content[i:i + 15] == 'class="section"':
                content = content.replace('class="section"', 'class="section" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
                i += 100

        content = content.replace('48', '5', 1)
        # for i in range(len(content)):
        #     if content[i:i+15]=='class ="piao_menu"':
        #         content = content.replace('class ="piao_menu"', 'class ="piao_menu" style="display:none;"', 1)
        # i += 100
        for i in range(len(content)):
            if content[i:i + 13] == 'data-original':
                content = content.replace('data-original', 'src')
                i += 100
            # if content[i:i+4]=="href":
            #     content = content[0:i] + 'href="#" ' + content[i:]
            if content[i:i + 4] == '超值低价':
                print('12345789')
                content = content[0:i - 158]
        for i in range(len(content)):
            if content[i:i + 26] == 'class="index_order clrfix"':
                content = content.replace('class="index_order clrfix"',
                                          'class="index_order clrfix" style="visibility:hidden;" ', 1)
                i += 1000

        for i in range(len(content)):
            # content=content.replace('href','alt')
            if content[i:i + 21] == 'class="q_header_main"':
                content = content.replace('class="q_header_main"', 'class="q_header_main" style="display:none;" ')
                # content = content[0:i] + 'style="display:none;" ' + content[i:]
                i += 1000
        with open('templates/dj1.html', 'w', encoding='utf-8')as fp:
            fp.write(content)
        return render(request, 'dj1.html', context={'city': city})
    except Exception as e:
        print('25252525')
        return render(request, 'fanhui.html')

def dj_view_two(request, city):
    try:
        # if city == '七台河':
        #     city = city
        # else:
        city = city + '博物馆'
        print('99999999999999')
        get_url = 'http://piao.qunar.com/ticket/list.htm?keyword='
        get_url2 = '&region=&from=mps_search_suggest'
        import urllib.parse
        # import urllib.parse
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
        }
        city = urllib.parse.quote(city)
        # end=urllib.parse.quote(end)
        url = get_url + city + get_url2
        print(url)
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        content = content.replace('action="/ticket/list.htm"', 'action="#"')
        for i in range(len(content)):
            # href = "/ticket/detail_1086665726
            if content[i:i + 15] == '"/ticket/detail':
                # if content[i:i+6]=='ticket':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 100
            elif content[i:i + 14] == '"/ticket/list_':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 10
            elif content[i:i + 17] == 'data-pager-pageno':
                content = content[:i] + ' target="_self" hidefocus="true"' + content[i:]
                i += 100
                print('********')
        for i in range(len(content)):

            if content[i:i + 27] == 'class="mp-search-container"':
                content = content.replace('class="mp-search-container"',
                                          'class="mp-search-container" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
        # elif content[i:i + 15] == '"/ticket/detail':
        # # if content[i:i+6]=='ticket':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i+=200
        #     elif content[i:i+14]=='"/ticket/list_':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i += 10
        for i in range(len(content)):
            if content[i:i + 15] == 'class="section"':
                content = content.replace('class="section"', 'class="section" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
                i += 100

        content = content.replace('48', '5', 1)
        # for i in range(len(content)):
        #     if content[i:i+15]=='class ="piao_menu"':
        #         content = content.replace('class ="piao_menu"', 'class ="piao_menu" style="display:none;"', 1)
        # i += 100
        for i in range(len(content)):
            if content[i:i + 13] == 'data-original':
                content = content.replace('data-original', 'src')
                i += 100
            # if content[i:i+4]=="href":
            #     content = content[0:i] + 'href="#" ' + content[i:]
            if content[i:i + 4] == '超值低价':
                print('12345789')
                content = content[0:i - 158]
        for i in range(len(content)):
            if content[i:i + 26] == 'class="index_order clrfix"':
                content = content.replace('class="index_order clrfix"',
                                          'class="index_order clrfix" style="visibility:hidden;" ', 1)
                i += 1000

        for i in range(len(content)):
            # content=content.replace('href','alt')
            if content[i:i + 21] == 'class="q_header_main"':
                content = content.replace('class="q_header_main"', 'class="q_header_main" style="display:none;" ')
                # content = content[0:i] + 'style="display:none;" ' + content[i:]
                i += 1000
        with open('templates/dj1.html', 'w', encoding='utf-8')as fp:
            fp.write(content)
        return render(request, 'dj1.html', context={'city': city})
    except Exception as e:
        print('25252525')
        return render(request, 'fanhui.html')

def dj_view_three(request, city):
    try:
        # if city == '七台河':
        #     city = city
        # else:
        city = city + '公园'
        print('99999999999999')
        get_url = 'http://piao.qunar.com/ticket/list.htm?keyword='
        get_url2 = '&region=&from=mps_search_suggest'
        import urllib.parse
        # import urllib.parse
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
        }
        city = urllib.parse.quote(city)
        # end=urllib.parse.quote(end)
        url = get_url + city + get_url2
        print(url)
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        content = content.replace('action="/ticket/list.htm"', 'action="#"')
        for i in range(len(content)):
            # href = "/ticket/detail_1086665726
            if content[i:i + 15] == '"/ticket/detail':
                # if content[i:i+6]=='ticket':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 100
            elif content[i:i + 14] == '"/ticket/list_':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 10
            elif content[i:i + 17] == 'data-pager-pageno':
                content = content[:i] + ' target="_self" hidefocus="true"' + content[i:]
                i += 100
                print('********')
        for i in range(len(content)):

            if content[i:i + 27] == 'class="mp-search-container"':
                content = content.replace('class="mp-search-container"',
                                          'class="mp-search-container" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
        # elif content[i:i + 15] == '"/ticket/detail':
        # # if content[i:i+6]=='ticket':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i+=200
        #     elif content[i:i+14]=='"/ticket/list_':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i += 10
        for i in range(len(content)):
            if content[i:i + 15] == 'class="section"':
                content = content.replace('class="section"', 'class="section" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
                i += 100

        content = content.replace('48', '5', 1)
        # for i in range(len(content)):
        #     if content[i:i+15]=='class ="piao_menu"':
        #         content = content.replace('class ="piao_menu"', 'class ="piao_menu" style="display:none;"', 1)
        # i += 100
        for i in range(len(content)):
            if content[i:i + 13] == 'data-original':
                content = content.replace('data-original', 'src')
                i += 100
            # if content[i:i+4]=="href":
            #     content = content[0:i] + 'href="#" ' + content[i:]
            if content[i:i + 4] == '超值低价':
                print('12345789')
                content = content[0:i - 158]
        for i in range(len(content)):
            if content[i:i + 26] == 'class="index_order clrfix"':
                content = content.replace('class="index_order clrfix"',
                                          'class="index_order clrfix" style="visibility:hidden;" ', 1)
                i += 1000

        for i in range(len(content)):
            # content=content.replace('href','alt')
            if content[i:i + 21] == 'class="q_header_main"':
                content = content.replace('class="q_header_main"', 'class="q_header_main" style="display:none;" ')
                # content = content[0:i] + 'style="display:none;" ' + content[i:]
                i += 1000
        with open('templates/dj1.html', 'w', encoding='utf-8')as fp:
            fp.write(content)
        return render(request, 'dj1.html', context={'city': city})
    except Exception as e:
        print('25252525')
        return render(request, 'fanhui.html')

def dj_view_four(request, city):
    try:
        # if city == '七台河':
        #     city = city
        # else:
        city = city + '动物园'
        print('99999999999999')
        get_url = 'http://piao.qunar.com/ticket/list.htm?keyword='
        get_url2 = '&region=&from=mps_search_suggest'
        import urllib.parse
        # import urllib.parse
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
        }
        city = urllib.parse.quote(city)
        # end=urllib.parse.quote(end)
        url = get_url + city + get_url2
        print(url)
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        content = content.replace('action="/ticket/list.htm"', 'action="#"')
        for i in range(len(content)):
            # href = "/ticket/detail_1086665726
            if content[i:i + 15] == '"/ticket/detail':
                # if content[i:i+6]=='ticket':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 100
            elif content[i:i + 14] == '"/ticket/list_':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 10
            elif content[i:i + 17] == 'data-pager-pageno':
                content = content[:i] + ' target="_self" hidefocus="true"' + content[i:]
                i += 100
                print('********')
        for i in range(len(content)):

            if content[i:i + 27] == 'class="mp-search-container"':
                content = content.replace('class="mp-search-container"',
                                          'class="mp-search-container" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
        # elif content[i:i + 15] == '"/ticket/detail':
        # # if content[i:i+6]=='ticket':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i+=200
        #     elif content[i:i+14]=='"/ticket/list_':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i += 10
        for i in range(len(content)):
            if content[i:i + 15] == 'class="section"':
                content = content.replace('class="section"', 'class="section" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
                i += 100

        content = content.replace('48', '5', 1)
        # for i in range(len(content)):
        #     if content[i:i+15]=='class ="piao_menu"':
        #         content = content.replace('class ="piao_menu"', 'class ="piao_menu" style="display:none;"', 1)
        # i += 100
        for i in range(len(content)):
            if content[i:i + 13] == 'data-original':
                content = content.replace('data-original', 'src')
                i += 100
            # if content[i:i+4]=="href":
            #     content = content[0:i] + 'href="#" ' + content[i:]
            if content[i:i + 4] == '超值低价':
                print('12345789')
                content = content[0:i - 158]
        for i in range(len(content)):
            if content[i:i + 26] == 'class="index_order clrfix"':
                content = content.replace('class="index_order clrfix"',
                                          'class="index_order clrfix" style="visibility:hidden;" ', 1)
                i += 1000

        for i in range(len(content)):
            # content=content.replace('href','alt')
            if content[i:i + 21] == 'class="q_header_main"':
                content = content.replace('class="q_header_main"', 'class="q_header_main" style="display:none;" ')
                # content = content[0:i] + 'style="display:none;" ' + content[i:]
                i += 1000
        with open('templates/dj1.html', 'w', encoding='utf-8')as fp:
            fp.write(content)
        return render(request, 'dj1.html', context={'city': city})
    except Exception as e:
        print('25252525')
        return render(request, 'fanhui.html')

def dj_view_five(request, city):
    try:
        # if city == '七台河':
        #     city = city
        # else:
        city = city + '滑雪场'
        print('99999999999999')
        get_url = 'http://piao.qunar.com/ticket/list.htm?keyword='
        get_url2 = '&region=&from=mps_search_suggest'
        import urllib.parse
        # import urllib.parse
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
        }
        city = urllib.parse.quote(city)
        # end=urllib.parse.quote(end)
        url = get_url + city + get_url2
        print(url)
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        content = content.replace('action="/ticket/list.htm"', 'action="#"')
        for i in range(len(content)):
            # href = "/ticket/detail_1086665726
            if content[i:i + 15] == '"/ticket/detail':
                # if content[i:i+6]=='ticket':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 100
            elif content[i:i + 14] == '"/ticket/list_':
                content = content[:i + 1] + 'http://piao.qunar.com' + content[i + 1:]
                i += 10
            elif content[i:i + 17] == 'data-pager-pageno':
                content = content[:i] + ' target="_self" hidefocus="true"' + content[i:]
                i += 100
                print('********')
        for i in range(len(content)):

            if content[i:i + 27] == 'class="mp-search-container"':
                content = content.replace('class="mp-search-container"',
                                          'class="mp-search-container" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
        # elif content[i:i + 15] == '"/ticket/detail':
        # # if content[i:i+6]=='ticket':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i+=200
        #     elif content[i:i+14]=='"/ticket/list_':
        #         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
        #         i += 10
        for i in range(len(content)):
            if content[i:i + 15] == 'class="section"':
                content = content.replace('class="section"', 'class="section" style="display:none;"', 1)
                # content=content[0:i]+ 'style="display:none;" '+content[i:]
                i += 100

        content = content.replace('48', '5', 1)
        # for i in range(len(content)):
        #     if content[i:i+15]=='class ="piao_menu"':
        #         content = content.replace('class ="piao_menu"', 'class ="piao_menu" style="display:none;"', 1)
        # i += 100
        for i in range(len(content)):
            if content[i:i + 13] == 'data-original':
                content = content.replace('data-original', 'src')
                i += 100
            # if content[i:i+4]=="href":
            #     content = content[0:i] + 'href="#" ' + content[i:]
            if content[i:i + 4] == '超值低价':
                print('12345789')
                content = content[0:i - 158]
        for i in range(len(content)):
            if content[i:i + 26] == 'class="index_order clrfix"':
                content = content.replace('class="index_order clrfix"',
                                          'class="index_order clrfix" style="visibility:hidden;" ', 1)
                i += 1000

        for i in range(len(content)):
            # content=content.replace('href','alt')
            if content[i:i + 21] == 'class="q_header_main"':
                content = content.replace('class="q_header_main"', 'class="q_header_main" style="display:none;" ')
                # content = content[0:i] + 'style="display:none;" ' + content[i:]
                i += 1000
        with open('templates/dj1.html', 'w', encoding='utf-8')as fp:
            fp.write(content)
        return render(request, 'dj1.html', context={'city': city})
    except Exception as e:
        print('25252525')
        return render(request, 'fanhui.html')

# def dj_view(request,city):
#     get_url='http://piao.qunar.com/ticket/list.htm?keyword='
#     get_url2='&region=&from=mps_search_suggest'
#     import urllib.parse
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
#     }
#     city=urllib.parse.quote(city)
#     url=get_url+city+get_url2
#     response = urllib.request.urlopen(url)
#     content=response.read().decode('utf-8')
#     content=content.replace('action="/ticket/list.htm"', 'action="#"')
#     # id="search-result-container"  超值低价
#     for i in range(len(content)):
#         # if content[i:i+15]=='"/ticket/detail':
#         #     content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
#         #     i+=200
#         # elif content[i:i+14]=='"/ticket/list_':
#         #     content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
#         #     i += 10
#         if content[i:i+28]=='id="search-result-container"':
#             # print('998998998998')
#             for j in range(0,i):
#                 if is_Chinese(content[j]) or content[j]=='(' or content[j]==')':
#                     # print(content[j])
#                     content=content.replace(content[j],' ',1)
#             # for j in range(i,len(content)):
#             #     if content[j:j+4]=='href':
#             #         print('*******')
#             #         content=content.replace(content[j:j+4],'id')
#         elif content[i:i+19]=='<div class="pager">':
#             content=content[0:i]
#         elif content[i:i+13]=='data-original':
#             content=content.replace('data-original','src')
#         elif content[i:i+4]=='超值低价':
#             content=content[0:i]
#         content=content.replace('<div class="index_order clrfix" id="filter">','<div style="visibility:hidden;" class="index_order clrfix" id="filter">')
#
#         content=content.replace('src="//source.qunarzz.com/common/hf/logo.png"','')
#         # content=content.replace('<div class="piao_menu" id="navigator">','<div style="visibility:hidden;" class="piao_menu" id="navigator">')
#         # content=content.replace('href','id')
#
#
#     with open('templates/dj1.html','w',encoding='utf-8')as fp:
#         fp.write(content)
#     return render(request,'dj1.html',context={'city':city})



import urllib.request
import urllib.parse
def dj_food(request,city):
    get_url='https://'
    get_url2='.nuomi.com/326'
    if city=='哈尔滨':
        str1='hrb'
        url = get_url +str1 + get_url2
    elif city=='齐齐哈尔':
        str1='qqhr'
        url = get_url +str1 + get_url2
    elif city=='绥化':
        str1='suihua'
    elif city=='伊春':
        str1='yich'
    else:
        from xpinyin import Pinyin
        p= Pinyin()
        pinyin=p.get_pinyin(city)
        # print(pinyin)
        str1 = pinyin[0]
        for i in range(len(pinyin)):
            if pinyin[i]=='-':
                str1+=pinyin[i+1]
        # print(str1)
    url = get_url +str1 + get_url2
    print(url)
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    for i in range(len(content)):
        if content[i:i+17]=='static-hook-id-1"':
            content = content.replace('static-hook-id-1"', 'static-hook-id-1" style="display:none;" ')
    for i in range(len(content)):
        if content[i:i+17]=='static-hook-id-2"':
            content = content.replace('static-hook-id-2"', 'static-hook-id-2" style="display:none;" ')
        elif content[i:i+17]=='static-hook-id-3"':
            content = content.replace('static-hook-id-3"', 'static-hook-id-3" style="display:none;" ')
        elif content[i:i+17]=='class="filter-bg"':
            content = content.replace('class="filter-bg"', 'class="filter-bg" style="display:none;" ')
        elif content[i:i+25]=='<div class="pager-info">共':
            content=content[0:i]


    with open('templates/dj2.html', 'w', encoding='utf-8')as fp:
        fp.write(content)
    # urllib.request.urlretrieve(url=url, filename='templates/dj2.html')

    return render(request, 'dj2.html', context={'city': city})
import urllib.parse
import urllib.request
def dj_history(request,city):
    if city=='沈阳':
        url='https://baike.baidu.com/item/%E6%B2%88%E9%98%B3/13034?fr=aladdin'
    else:
        get_url='https://baike.baidu.com/item/'
        city = urllib.parse.quote(city)
        url=get_url+city
    # print(url)
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    # print(content)
    # for i in content:
    #     if i=='县':
    #         print('123456')
    for i in range(len(content)):
        if content[i:i + 9] == '行政区划</h2>':
            content = content[0:i]
        # href = "/ticket/detail_1086665726
        elif content[i:i + 6] == '"/item' or content[i:i + 6] == '"/plan':
            # if content[i:i+6]=='ticket':
            content = content[:i+1] + 'https://baike.baidu.com' + content[i+1:]
            i += 200
            # print('********')
        elif content[i:i + 14] == 'pc-header-new"':
            content = content.replace('pc-header-new"', 'pc-header-new"" style="display:none;" ')
        elif content[i:i + 15] == 'navbar-wrapper"':
            content = content.replace('navbar-wrapper"', 'navbar-wrapper" style="display:none;" ')
        elif content[i:i + 15] == 'before-content"':
            content = content.replace('before-content"', 'before-content" style="display:none;" ')
        elif content[i:i + 15] == '"lemma-catalog"':
            content = content.replace('"lemma-catalog"', '"lemma-catalog" style="display:none;" ')
        elif content[i:i + 6] == 'inline':
            # print('898989999999999')
            content = content.replace('inline', 'none')
        elif content[i:i + 6] == '220px;':
            # print('898989999999999')
            content = content.replace('220px;', '0px; display:none;')
        elif content[i:i + 6] == '222px;':
            # print('898989999999999')
            content = content.replace('222px;', '0px; display:none;')
        elif content[i:i + 33] == 'class="posterFlag excellent-icon"':
            # print('898989999999999')
            content = content.replace('class="posterFlag excellent-icon"', 'class="posterFlag excellent-icon" style="display:none;" ')

    with open('templates/dj3.html', 'w', encoding='utf-8')as fp:
        fp.write(content)
    # urllib.request.urlretrieve(url=url, filename='templates/dj3.html')
    return render(request, 'dj3.html', context={'city': city})


def background(request):

    return render(request,'background.html')

def dj_famous(request,city):
    str1='http://weather.sina.com.cn/'
    str2='/177863#12'
    # city=urllib.parse.quote(city)

    from xpinyin import Pinyin
    p= Pinyin()
    pinyin=p.get_pinyin(city)
    str3=''
    if pinyin=='chu-zhou':
        pinyin+='1'
    for i in pinyin:
        if i!='-':
            str3+=i
    url = str1 + str3
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    # urllib.request.urlretrieve(url=url, filename='templates/dj4.html')
    for i in range(len(content)):
        if content[i:i+4]=='日出日落':
            content=content[0:i-100]
        elif content[i:i + 14] == 'class="header"':
            content = content.replace('class="header"', 'class="header" style="display:none;" ')
        elif content[i:i + 20] == 'slider_dc_container"':
            content = content.replace('slider_dc_container"', 'slider_dc_container" style="display:none;" ')
        elif content[i:i + 19] == 'class="wt_tt0_note"':
            content = content.replace('class="wt_tt0_note"', 'class="wt_tt0_note" style="display:none;" ')
        elif content[i:i + 28] == 'class="slider_ct_time png24"':
            content = content.replace('class="slider_ct_time png24"', 'class="slider_ct_time png24" style="display:none;" ')




    with open('templates/dj4.html', 'w', encoding='utf-8')as fp:
        fp.write(content)
    return render(request, 'dj4.html', context={'city': city,'url':url})

def dj_person(request,city):
    # str1='https://baike.sogou.com/city/'
    # str2 = '.v?category=4&anchor=synthesis'
    # city = urllib.parse.quote(city)
    # url = str1 + city + str2
    str1='http://hotel.elong.com/'
    # str2='?category=4&fr=lmcitynav'
    from xpinyin import Pinyin
    p = Pinyin()
    pinyin = p.get_pinyin(city)
    str3 = ''
    if city=='哈尔滨':
        str3='harbin'
    else:
        for i in pinyin:
            if i != '-':
                str3 += i
    url = str1 + str3
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    # response = urllib.request.urlopen(url)
    # content = response.read().decode('utf-8')
    # for i in range(len(content)):
    #     # href = "/ticket/detail_1086665726
    #     if content[i:i + 7] == 'href="/':
    #         # if content[i:i+6]=='ticket':
    #         content = content[:i + 6] + 'http://hotel.elong.com/' + content[i + 6:]


    for i in range(len(content)):

        if content[i:i + 7] == 'href="/':
            # if content[i:i+6]=='ticket':
            content = content[:i + 6] + 'http://hotel.elong.com/' + content[i + 6:]
        elif content[i:i + 11] == 'id="header"':
            content = content.replace('id="header"','id="header" style="display:none;"', 1)
        elif content[i:i + 17] == 'class="mt10 mb10"':
            content = content.replace('class="mt10 mb10"', 'class="mt10 mb10" style="display:none;"', 1)
        elif content[i:i + 16] == 'id="m_searchBox"':
            content = content.replace('id="m_searchBox"', 'id="m_searchBox" style="display:none;"', 1)
        elif content[i:i + 15] == 'id="filterZone"':
            content = content.replace('id="filterZone"', 'id="filterZone" style="display:none;"', 1)

        elif content[i:i + 18] == 'id="conditionZone"':
            content = content.replace('id="conditionZone"', 'id="conditionZone" style="display:none;"', 1)
        elif content[i:i + 13] == 'id="sortZone"':
            content = content.replace('id="sortZone"', 'id="sortZone" style="display:none;"', 1)
        elif content[i:i + 18] == 'class="list_login"':
            content = content.replace('class="list_login"', 'class="list_login" style="display:none;"', 1)
        # elif content[i:i + 14] == 'class="h_info"':
        #     content = content.replace('class="h_info"', 'class="h_info" style="display:none;"', 1)
        # elif content[i:i + 16] == 'class="icon_nmb"':
        #     content = content.replace('class="icon_nmb"', 'class="icon_nmb" style="visibility:hidden;"')
    for i in range(len(content)):
        if content[i:i + 15] == 'class="paging1"':
            print('123456')
            content = content[0:i]
        elif content[i:i+78]=='http://m.elongstatic.com/static/webapp/pc_static/common/pic/loading180_130.gif':
            content=content.replace('http://m.elongstatic.com/static/webapp/pc_static/common/pic/loading180_130.gif','http://pavo.elongstatic.com/i/Hotel795_325/nw_0009zWp1.jpg')


        # for i in range(len(content)):
        #     if content[i:i + 7] == 'data-ll':
        #         content = content.replace('data-ll', 'src',1)
        #         i+=50

    with open('templates/dj5.html', 'w', encoding='utf-8')as fp:
        fp.write(content)
    # print(url)


    return render(request, 'dj5.html', context={'city': city, 'url': url})

def dj_goods(request,city):
    get_url='http://www.86techan.com/search/?q='
    data=urllib.parse.quote(city)
    url=get_url+data
    # print(url)
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
    }
    request1=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request1)

    content = response.read().decode('utf-8')
    from lxml import etree
    tree = etree.HTML(content)
    list1 = tree.xpath('//div[@class="list center index-f1"]/div/ul/ul/li/div/a/text()')
    print(list1)
    print(type(list1))

    for i in range(len(list1)-1):
        if list1[i]=='带你体验南京秦淮风情游':
            list1.pop(i)
    # with open('templates/dj6.html', 'w', encoding='utf-8')as fp:
    #     fp.write(content)
    return render(request, 'dj6.html', context={'city': city, 'url': url,'list1':list1})

# def dj_goods(request,city):
#     city=city+'特产'
#     get_url='https://search.jd.com/Search?'
#     data={
#         'keyword': city,
#         'enc': 'utf-8',
#         'wq': city,
#     }
#     data=urllib.parse.urlencode(data)
#     url=get_url+data
#     # print(url)
#     headers={
#         'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
#     }
#     request1=urllib.request.Request(url=url,headers=headers)
#     response=urllib.request.urlopen(request1)
#     content = response.read().decode('utf-8')
#     # print(content)
#     # with open('templates/dj_goodsss.html','w',encoding='utf-8')as fp:
#     #     fp.write(content)
#
#     # str1 = 'http://www.ct918.cn/goods_list.html?keyword='
#     # str2='&search=goods'
#     # city = urllib.parse.quote(city)
#     # url = str1 + city + str2
#     return render(request, 'dj6.html', context={'city': city, 'url': url})
#     # return render(request,'dj_goodsss.html')

#下面写第二部分：发布新路径
def dj_add(request):
    cursor=getcursor()
    if request.method=='GET':
        return render(request,'dj_add.html')
    else:
        def is_Chinese(word):
            for ch in word:
                if '\u4e00' <= ch <= '\u9fff':
                    return True
            return False
        try:
            start1=request.POST.get('start')
            end=request.POST.get('end')
            cities=request.POST.get('cities')
            distance=request.POST.get('distance')
            if distance=='':
                distance=='0'
            else:
                distance=float(request.POST.get('distance'))
            if start1=='' or end=='' or cities=='' or distance=='':
                return render(request,'kong.html')
            elif is_Chinese(start1)==True:
                start=''
                for i in start1:
                    if is_Chinese(i):
                        start+=i
                    # print(start)
                if is_Chinese(end)==True:
                    end1=''
                    for i in end:
                        if is_Chinese(i):
                            end1+=i

                        # print(end1)
                    if is_Chinese(cities)==True:
                        for i in cities:
                            if is_Chinese(i) == False:
                                cities = cities.replace(i, ',')
                        str2 = []
                        for i in cities:
                            # if i not in str2:
                            str2.append(i)
                        # print(str2)

                        str3 = []
                        for i in range(1, len(str2)):
                            if str2[i] != str2[i - 1]:
                                str3.append(str2[i - 1])
                            if i == len(str2) - 1 and is_Chinese(str2[i]):
                                str3.append(str2[i])
                        print(str3)
                        cities = ''
                        for i in str3:
                            cities += i

                        print(cities)
                        # print(cities)
                        # print('98888888888888')
                        if '，' in cities or '、' in cities or '.' in cities or '。'in cities or ';' in cities:
                            return render(request, 'chinese.html')
                        else:
                            if type(float(distance)) == float:
                                print(type(distance))
                                cursor.execute('select * from dj where start="%s" and ends="%s"'%(start,end1))
                                find=cursor.fetchall()
                                if not find:
                                    cursor.execute("insert into dj(start,ends,cities,distance) VALUE ('%s','%s','%s','%f')"%(start,end1,cities,distance))
                                    return redirect(reverse('index'))
                                else:
                                    return render(request,'exist.html')
                            else:
                                return render(request,'chinese5.html')
                    else:
                        return render(request, 'chinese4.html')
                else:
                    return render(request, 'chinese3.html')

            else:
                return render(request,'chinese2.html')

        except Exception as e:
            return render(request,'error.html',context={'e':e})

#下面是第三部分，，修改已经存在的路径
def update_dj(request):
    cursor = getcursor()
    cursor.execute("select * from dj order by id limit 10")
    dj_list=cursor.fetchall()
    return render(request,'update_dj.html',context={'dj_list':dj_list})
def dj_detailes(request,dj_id):
    cursor = getcursor()
    cursor.execute("select * from dj where id='%s'" % dj_id)
    dj = cursor.fetchone()
    return render(request, 'dj_detailes.html', context={'dj': dj})
def change_dj(request):
    if request.method=='get':
        return render(request,'update_dj.html')
    else:
        cursor=getcursor()
        try:
            dj_id = request.POST.get('dj_id')
            start1=request.POST.get('start')
            end=request.POST.get('ends')
            # print(end)
            cities=request.POST.get('cities')
            # print('456789')
            distance=request.POST.get('distance')
            if distance=='':
                distance=='0'
            else:
                distance=float(request.POST.get('distance'))
            if start1=='' or end=='' or cities=='' or distance=='':
                return render(request,'kong_update.html',context={'id':dj_id})
            elif is_Chinese(start1)==True:
                start=''
                for i in start1:
                    if is_Chinese(i):
                        start+=i
                #     print(start)
                # print('123456')
                if is_Chinese(end)==True:
                    end1=''
                    for i in end:
                        if is_Chinese(i):
                            end1+=i
                        # print(end1)
                    if is_Chinese(cities)==True:
                        for i in cities:
                            if is_Chinese(i) == False:
                                cities = cities.replace(i, ',')
                        str2 = []
                        for i in cities:
                            # if i not in str2:
                            str2.append(i)
                        # print(str2)

                        str3 = []
                        for i in range(1, len(str2)):
                            if str2[i]=='齐':
                                str3.append(str2[i - 1])
                            elif str2[i] != str2[i - 1]:
                                str3.append(str2[i - 1])
                            if i == len(str2) - 1 and is_Chinese(str2[i]):
                                str3.append(str2[i])
                        print(str3)
                        cities = ''
                        for i in str3:
                            cities += i

                        print(cities)
                        # else:
                            # print('66666666')
                        if type(float(distance)) == float:
                            # print(type(distance))
                            # cursor.execute('select * from dj where start="%s" and ends="%s"' % (start, end1))
                            # find = cursor.fetchall()
                            # if not find:
                            cursor.execute(
                                "update dj set start='%s',ends='%s',cities='%s',distance='%s' where id=%s " % (
                                    start, end1, cities, distance, dj_id))
                            return redirect(reverse('update_dj'))
                            # else:
                            #     return render(request, 'exist_update.html')
                        else:
                            return render(request,'chinese5_dis.html',context={'id':dj_id})
                    else:
                        return render(request, 'chinese4_city.html',context={'id':dj_id})
                else:
                    return render(request, 'chinese3_end.html',context={'id':dj_id})

            else:
                return render(request,'chinese2_start.html',context={'id':dj_id})

        except Exception as e:
            # print(e)
            return render(request,'error_dis.html',context={'e':e,'id':dj_id})


#下面是第四部分，查找路径，也是核心部分

def search_dj(request):
    if request.method=='GET':
        return render(request,'dj_search.html')
    else:
        try:
            def is_Chinese(word):
                for ch in word:
                    if '\u4e00' <= ch <= '\u9fff':
                        return True
                return False

            def is_alphabet(uchar):
                """判断一个unicode是否是英文字母"""
                if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
                    return True
                else:
                    return False
            start=request.POST.get('start')
            middle=request.POST.get('middle')
            ends=request.POST.get('ends')
            if is_alphabet(start)==True:
                if is_alphabet(ends)==True:
                    if is_alphabet(middle)==True:
                        str3=''
                        for i in start:
                            str3+=i
                        str3=str3+'+'
                        for i in ends:
                            str3+=i
                        str3=str3+'+'
                        for i in middle:
                            str3+=i
                        city__ = baidu_translate(str3)
                        print(city__)
                        print(type(city__))
                        city02=city__.split('+')
                        start1=city02[0]
                        ends1=city02[1]
                        middle1=city02[2]
                        print(start1,ends1,middle1)
                    else:
                        str3 = ''
                        for i in start:
                            str3 += i
                        str3 = str3 + '+'
                        for i in ends:
                            str3 += i
                        city__ = baidu_translate(str3)
                        print(city__)
                        print(type(city__))
                        city02 = city__.split('+')
                        start1 = city02[0]
                        ends1 = city02[1]
                        print('99999999')
                        print(start1, ends1)

                else:
                    if is_alphabet(middle)==True:
                        str3=''
                        for i in start:
                            str3+=i
                        str3=str3+'+'
                        for i in middle:
                            str3+=i
                        ends1=''
                        for i in ends:
                            if is_Chinese(i):
                                ends1+=i
                        city__ = baidu_translate(str3)
                        print(city__)
                        print(type(city__))
                        city02=city__.split('+')
                        start1=city02[0]
                        # ends1=city02[1]
                        middle1=city02[1]
                        print(start1,middle1)
                    else:

                        start1=baidu_translate(start)
                        ends1=''
                        for i in ends:
                            if is_Chinese(i):
                                ends1+=i
                        middle1=''
                        for i in middle:
                            if is_Chinese(i):
                                middle1+=i

            else:
                if is_alphabet(ends)==True:
                    if is_alphabet(middle)==True:
                        str3=''
                        for i in ends:
                            str3+=i
                        str3=str3+'+'
                        for i in middle:
                            str3+=i
                        city__ = baidu_translate(str3)
                        print(city__)
                        print(type(city__))
                        city02=city__.split('+')
                        # start1=city02[0]
                        ends1=city02[0]
                        middle1=city02[1]
                        print(middle1,ends1)
                    else:
                        ends1 = baidu_translate(ends)
                        start1 = ''
                        for i in start:
                            if is_Chinese(i):
                                start1 += i
                        middle1 = ''
                        for i in middle:
                            if is_Chinese(i):
                                middle1 += i
                else:
                    if is_alphabet(middle) == True:
                        start1=''
                        ends1=''
                        for i in start:
                            if is_Chinese(i)==True:
                                start1+=i
                        for i in ends:
                            if is_Chinese(i)==True:
                                ends1+=i
                        middle1=baidu_translate(middle)
                    else:
                        middle1=''
                        for i in middle:
                            if is_Chinese(i):
                                middle1+=i
                        start1=''
                        for i in start:
                            if is_Chinese(i):
                                start1+=i
                        ends1=''
                        for i in ends:
                            if is_Chinese(i):
                                ends1+=i
                    # print(start1,ends1)
            print('9*9*9*9*9*')
            print(start1,middle1,ends1)
            if start1=='' or ends1=='':
                return render(request,'kong_search.html')
            if not middle:
                cursor = getcursor()
                cursor.execute("select * from dj where start='%s' and ends='%s'"%(start1,ends1))
                searchs=cursor.fetchall()
            # print(searchs)
            # print('9999999')
                cursor = getcursor()
                cursor.execute("select cities from dj where start='%s' and ends='%s'"%(start1,ends1))
                city_ll=cursor.fetchone()
                # print(city_ll)
                cities=''
                if city_ll:
                    for i in city_ll:
                        cities+=i
                    # cities = str(cursor.fetchone())
                else:
                    cities='没有路径'
                # print(cities)
                # print('888889999')
                if cities != '没有路径':
                    city = cities
                    length = len(city)
                    city_list = city.split(',')
                    ds=0
                    print('66666666666666')
                    print(city_list)
                    print('**********')
                else:
                    for i in range(len(dict1)):
                        if dict1[i] == start1:
                            start2 = i
                        if dict1[i] == ends1:
                            end2 = i
                    # global ds
                    city_list1, ds = Dijkstra(G, start2, end2)
                    city_list = []
                    for i in city_list1:
                        city_list.append(dict1[i])
                    print(city_list)

                from geopy.geocoders import Nominatim

                # 使用geopy查询
                try:
                    def geocodeN(address):
                        gps = Nominatim()
                        location = gps.geocode(address)
                        j = location.longitude
                        w = location.latitude
                        return j, w
                    # j, w = geocodeN('哈尔滨')
                    city_="["
                    for i in range(len(city_list)):
                        if city_list[i]=='白山':
                            j=126.46
                            w=41.90
                        elif city_list[i]=='松原':
                            j = 124.850
                            w = 45.156
                        elif city_list[i]=='吉林':
                            j=126.540
                            w=43.854
                        elif city_list[i]=='葫芦岛':
                            j=120.836
                            w=40.726
                        elif city_list[i]=='锦州':
                            j=121.127
                            w=41.093
                        else:
                            j,w=geocodeN(city_list[i])
                        #"125.320921|43.846056",
                        city_+='"'
                        city_+=str(j)
                        city_+='|'
                        city_+=str(w)
                        city_+='"'
                        if i!=len(city_list)-1:
                            city_+=','
                        else:
                            city_+=']'
                    # print(city_)
                    print('8888888888888888')
                # city_=list(city_)
                except:
                    return render(request, 'time_out.html')

                # print(city_)
                # print('*/*/*/*/*/*/*')
                return render(request,'dj_show.html',context={'searchs':searchs,'middle':middle1,'city_':city_,'start':start1,'ends':ends1,'city_list':city_list,'ds':ds})
            else:
                searchs=''
                for i in range(len(dict1)):
                    if dict1[i] == start1:
                        start2 = i
                    if dict1[i] == ends1:
                        end2 = i
                    if dict1[i]==middle1:
                        middle2 = i
                # global ds
                city_list1, ds01 = Dijkstra(G, start2, middle2)
                city_list2, ds02 = Dijkstra(G, middle2, end2)
                city_list2.pop(0)
                ds=ds01+ds02
                city_list = []
                for i in city_list1:
                    city_list.append(dict1[i])
                for i in city_list2:
                    if dict1[i] not in city_list:
                        city_list.append(dict1[i])
                print(city_list)
                print('963963963')

                from geopy.geocoders import Nominatim

                # 使用geopy查询
                try:
                    def geocodeN(address):
                        gps = Nominatim()
                        location = gps.geocode(address)
                        j = location.longitude
                        w = location.latitude
                        return j, w
                    # j, w = geocodeN('哈尔滨')
                    city_="["
                    for i in range(len(city_list)):
                        if city_list[i]=='白山':
                            j=126.46
                            w=41.90
                        elif city_list[i]=='松原':
                            j = 124.850
                            w = 45.156
                        elif city_list[i]=='吉林':
                            j=126.540
                            w=43.854
                        elif city_list[i]=='葫芦岛':
                            j=120.836
                            w=40.726
                        elif city_list[i]=='锦州':
                            j=121.127
                            w=41.093
                        else:
                            j,w=geocodeN(city_list[i])
                        #"125.320921|43.846056",
                        city_+='"'
                        city_+=str(j)
                        city_+='|'
                        city_+=str(w)
                        city_+='"'
                        if i!=len(city_list)-1:
                            city_+=','
                        else:
                            city_+=']'
                    print(city_)
                    print('8888888888888888')
                # city_=list(city_)
                except:
                    return render(request, 'time_out.html')

                # print(city_)
                # print('*/*/*/*/*/*/*')
                return render(request,'dj_show.html',context={'searchs':searchs,'middle':middle1,'city_':city_,'start':start1,'ends':ends1,'city_list':city_list,'ds':ds})


        except Exception as e:
            return render(request, 'time_out.html')







