# import urllib.request
# import urllib.parse
# from django.shortcuts import render,redirect,reverse
#
# str1='http://www.tianqi.com/'
# # city=urllib.parse.quote(city)
#
# from xpinyin import Pinyin
# p= Pinyin()
# pinyin=p.get_pinyin('上海')
# str3=''
# for i in pinyin:
#     if i!='-':
#         str3+=i
# # # print(str1)
# # url=str1+str3+str2
# # print(url)
# # headers={
# #     'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
# # }
# # request=urllib.request.Request(url=url,headers=headers)
# url=str1+str3
# print(url)
# # url=str1+'shanghai'
# response = urllib.request.urlopen(url)
# content = response.read().decode('utf-8')
# # print(content)
# # urllib.request.urlretrieve(url=url, filename='templates/dj4.html')
# with open(r'D:\01python项目\dj\templates\dj5.html', 'w', encoding='utf-8')as fp:
#     fp.write(content)
# # return render(request, 'dj4.html', context={'city': city,'url':url})
#

# def is_alphabet(uchar):
#     """判断一个unicode是否是英文字母"""
#     if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
#         return True
#     else:
#         return False
#
#
# def pinyin_2_hanzi(pinyinList):
#     from Pinyin2Hanzi import DefaultDagParams
#     from Pinyin2Hanzi import dag
#
#     dagParams = DefaultDagParams()
#     # 10个候选值
#     result = dag(dagParams, pinyinList, path_num=10, log=True)
#     for item in result:
#         socre = item.score  # 得分
#         res = item.path  # 转换结果
#         print(socre, res)
#
#
# start = 'jixi'
# print(pinyin_2_hanzi(start))
# ends = 'changchun'
# print(is_alphabet(start))
# if is_alphabet(start) == True:
#     start = pinyin_2_hanzi(start)
# if is_alphabet(ends):
#     ends = pinyin_2_hanzi(ends)
#
# print(start)
import hashlib
import random
import urllib




def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False
#
# print(is_alphabet('长春ll'))

import http.client
import hashlib
import json
import urllib
import random

#
# def baidu_translate(content):
#     appid = '20151113000005349'
#     secretKey = 'osubCEzlGjzvw8qdQc41'
#     httpClient = None
#     myurl = '/api/trans/vip/translate'
#     q = content
#     fromLang = 'en'  # 源语言
#     toLang = 'zh'  # 翻译后的语言
#     salt = random.randint(32768, 65536)
#     sign = appid + q + str(salt) + secretKey
#     sign = hashlib.md5(sign.encode()).hexdigest()
#     myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
#         q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
#         salt) + '&sign=' + sign
#
#     try:
#         httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
#         httpClient.request('GET', myurl)
#         # response是HTTPResponse对象
#         response = httpClient.getresponse()
#         jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
#         js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
#         dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
#         return dst # 打印结果
#     except Exception as e:
#         print(e)
#     finally:
#         if httpClient:
#             httpClient.close()
# start ='jiamusi'
# starts='jixi'
# ll='changchun'
# # if is_alphabet(start) == True:
# #     start = baidu_translate(start)
# # print('************************')
# # print(start)
# # print(ll)
# if is_alphabet(starts) == True:
#     starts = baidu_translate(starts)
# print('************************')
# print(starts)
# def is_alphabet(uchar):
#     """判断一个unicode是否是英文字母"""
#     if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
#         return True
#     else:
#         return False
# #
# # print(is_alphabet('长春ll'))
#
# import http.client
# import hashlib
# import json
# import urllib
# import random

#
# from front.baidufanyi import baidu_translate
# start ='jiamusi'
# starts='jixi'
# ll='changchun'
# if is_alphabet(start) == True:
#     start = baidu_translate('changchun,daqing')
# print(start)
# print('************************')

# def is_Chinese(word):
#     for ch in word:
#         if '\u4e00' <= ch <= '\u9fff':
#             return True
#     return False
#
# print(is_Chinese('常准,李连杰'))

# print(type(float('4')))
#
# s = 'abc123isk'
# print(s.replace('abc', ''))
# get_url='http://piao.qunar.com/ticket/list.htm?keyword='
# get_url2='&region=&from=mps_search_suggest'
# import urllib.parse
# import urllib.request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
# }
# # url=get_url+'shanghai'+get_url2
# # print(url)
# url='http://s.lvmama.com/ticket/P2?keyword=%E4%B8%8A%E6%B5%B7&tabType=ticket#list'
# response = urllib.request.urlopen(url)
# content=response.read().decode('utf-8')
# content=content.replace('action="/ticket/list.htm"', 'action="#"')
# for i in range(len(content)):
#     # href = "/ticket/detail_1086665726
#     if content[i:i+15]=='"/ticket/detail':
#     # if content[i:i+6]=='ticket':
#         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
#         i+=200
#     elif content[i:i+14]=='"/ticket/list_':
#         content=content[:i+1]+'http://piao.qunar.com'+content[i+1:]
#         i += 10
# with open('dj_test.html','w',encoding='utf-8')as fp:
#     fp.write(content)


# def is_Chinese(word):
#     for ch in word:
#         if '\u4e00' <= ch <= '\u9fff':
#             return True
#     return False
# str1='哈尔滨。。长春、、大庆..'
# for i in str1:
#     if is_Chinese(i)==False:
#         str1=str1.replace(i,',')
# print(str1)
# str2=[]
# for i in str1:
#     # if i not in str2:
#     str2.append(i)
# print(str2)
#
# str3=[]
# for i in range(1,len(str2)):
#     if str2[i]!=str2[i-1]:
#         str3.append(str2[i-1])
#     if i==len(str2)-1 and is_Chinese(str2[i]):
#         str3.append(str2[i])
# print(str3)
# str1=''
# for i in str3:
#     str1+=i
#
# print(str1)

tuple=((36, '哈尔滨', '长春', '哈尔滨,长春', 86.69),)
tuple1=((36, '哈尔滨', '长春', '哈尔滨,长春', 86.69),)
li=tuple[0][3]+tuple1[0][3]
print(li)

