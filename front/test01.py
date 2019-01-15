# from geopy.geocoders import Nominatim
#
# #使用geopy查询
# def geocodeN(address):
#     gps=Nominatim()
#     location=gps.geocode(address)
#     j=location.longitude
#     w=location.latitude
#     return j,w
# j,w=geocodeN('哈尔滨')
# print(j)
# print(w)
# def is_Chinese(word):
#     for ch in word:
#         if '\u4e00' <= ch <= '\u9fff':
#             return True
#     return False
# str1='张三丰12345'
# str2='1'
# print(str2.isdigit())
# print(str1[0:2])
# for i in str1:
#     if is_Chinese(i):
#         print(i)
#         str1=str1.replace(i,"1")
# print(str1)

str1='class="mp-search-container"'


print(len(str1))