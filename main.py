from dianping import Poi, City, Shop
import requests
import time
import html2text

from model import Stores, Reviews, Pics, Cities


# poi = Poi()
# cities = poi.getCities()

# for v in cities:
#     try:
#         city = Cities.get(cityId = v.cityId)
#     except:
#         city = Cities()
#         city.cityid = str(v.cityId)
#         city.tuangouflag = str(v.TuanGouFlag)
#         city.apphotlevel = str(v.appHotLevel)
#         city.cityabbrcode = str(v.cityAbbrCode)
#         city.cityareacode = str(v.cityAreaCode)
#         city.cityenname = str(v.cityEnName)
#         city.cityid = str(v.cityId)
#         city.citylevel = str(v.cityLevel)
#         city.cityname = str(v.cityName)
#         city.cityorderid = str(v.cityOrderId)
#         city.citypyname = str(v.cityPyName)
#         city.directurl = str(v.directURL)
#         city.glat = str(v.gLat)
#         city.glng = str(v.gLng)
#         city.hasreturl = str(v.hasReturl)
#         city.isactivecity = str(v.isActiveCity)
#         city.isoverseascity = str(v.isOverseasCity)
#         city.isscenery = str(v.isScenery)
#         city.parentcityid = str(v.parentCityId)
#         city.provinceid = str(v.provinceId)
#         city.standardenname = str(v.standardEnName)
#         city.url = str(v.url)
#         city.save()


# cities = Cities.select().where(Cities.parentcityid==0).order_by(Cities.cityid)
# for v in cities:
#     print(v.cityid)
#     city = City(int(v.cityid))
#     shops = city.search('海底捞火锅')

#     for v in shops:
#         try:
#             store = Stores.get(source = v.id)
#         except:
#             store = Stores()
#             store.source = v.id
#         store.origin = 2
#         store.name = v.name + v.branchName
#         store.save()



stores = Stores.select().where(Stores.name % '%海底捞%', Stores.id >=  2).order_by(Stores.id)
for store in stores:
    print('store.id:'+str(store.id))
    print(store.source)
    shop = Shop(store.source)
    current = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    page = 1
    while current >= time.strftime('%Y-%m-%d', time.localtime(time.time()-2592000)):
        reviews = shop.get_reviews(page)
        print(reviews)
        if not len(reviews):
            current = time.strftime(
                '%Y-%m-%d', time.localtime(time.time()-2592000))
            break
        page = page+1
        time.sleep(6)
        for v in reviews:
            print(v)
            current = v.published_at
            try:
                Reviews.get(origin=2, source=v.id)
            except:
                review = Reviews()
                review.source = v.id
                review.origin = 2
                review.user_nickname = v.user_nickname
                review.shop_source = store.source
                review.published_at = v.published_at
                review.pics = v.pics
                # review.content = v.content
                review.save()
            if len(v.pics):
                for img in v.pics:
                    try:
                        pic = Pics.get(origin=2, url=img.url)
                    except:
                        pic = Pics()
                        pic.origin = 2
                    pic.source = img.id
                    pic.url = img.url
                    pic.high_url = img.high_url
                    pic.published_at = v.published_at
                    pic.save()
