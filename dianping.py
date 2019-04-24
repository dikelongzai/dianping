# -*- coding: utf-8 -*-

import os
import json
import requests
import datetime
from math import ceil
import random
import time

HEADERS = {
    'Referer': 'https://m.dianping.com/shop/4094416/review_all',
    'Origin': 'https://m.dianping.com',
    'User-Agent': 'Mozilla/5.1 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'DNT': '1',
    'Content-Type': 'application/json',
}
cookies = {
    'cityid': '1',
    'msource': 'default',
    'chwlsource': 'default',
    '_lxsdk_cuid': '1696c16406cc8-0d2fcac86e6dbe-36677905-fa000-1696c16406cc8',
    '_lxsdk': '1696c16406cc8-0d2fcac86e6dbe-36677905-fa000-1696c16406cc8',
    'logan_custom_report': '',
    'switchcityflashtoast': '1',
    '_hc.v': '78163bb8-d937-1dae-dad8-e0dab83c2a70.1552296592',
    'dp_pwa_v_': '4918b24041ad5907d9fbe068bd4425432fb2c8c9',
    'dper': '54ab0eef9f32a7bc200c4386d1c1527251f80ce8ab88db4f6fddd7a56975eca4e13fd04d16a8919289778402918ade1fdeb9023b88d57804bb852304e8d1a5dd76e79d1f556b19022584e0953d27cad58d3efc0b313cc50209889f99d827a1ef',
    'll': '7fd06e815b796be3df069dec7836c3df',
    'ua': 'dpuser_0228649147',
    'ctu': '05813833daa55e9ae518c439c336164206edca84febb530c48e8da18ea17728e',
    'default_ab': 'index%3AA%3A1%7Cmyinfo%3AA%3A1',
    'logan_session_token': 'u63twijiwhz2ixydysuj',
    '_lxsdk_s': '1696c1626f4-691-3ac-c78%7C%7C12',
}

class Poi:

    def getCities(self):
        az = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = []
        for v in az:
            url = 'https://m.dianping.com/citylist'
            params = {
                '_api': 'true',
                'msource': 'default',
                'c': v,
            }
            HEADERS['Content-Type']='application/json'
            HEADERS['charset']='UTF-8'
            res = requests.get(url, headers=HEADERS, cookies=cookies, params=params)
            try:
                content = res.json()
            except:
                return result

            for v in content['appState']['list']['data']['charCityData']:
                city = City(v['cityId'])
                city.TuanGouFlag = v['TuanGouFlag']
                city.appHotLevel = v['appHotLevel']
                city.cityAbbrCode = v['cityAbbrCode']
                city.cityAreaCode = v['cityAreaCode']
                city.cityEnName = v['cityEnName']
                city.cityId = v['cityId']
                city.cityLevel = v['cityLevel']
                city.cityName = v['cityName']
                city.cityOrderId = v['cityOrderId']
                city.cityPyName = v['cityPyName']
                city.directURL = v['directURL']
                city.gLat = v['gLat']
                city.gLng = v['gLng']
                city.hasReturl = v['hasReturl']
                city.isActiveCity = v['isActiveCity']
                city.isOverseasCity = v['isOverseasCity']
                city.isScenery = v['isScenery']
                city.parentCityId = v['parentCityId']
                city.provinceId = v['provinceId']
                city.standardEnName = v['standardEnName']
                city.url = v['url']
                result.append(city)
        return result

class City:

    id = None
    cookies = {
        'cityid': '1',
        'msource': 'default',
        'chwlsource': 'default',
        '_lxsdk_cuid': '1696c16406cc8-0d2fcac86e6dbe-36677905-fa000-1696c16406cc8',
        '_lxsdk': '1696c16406cc8-0d2fcac86e6dbe-36677905-fa000-1696c16406cc8',
        'logan_custom_report': '',
        'switchcityflashtoast': '1',
        '_hc.v': '78163bb8-d937-1dae-dad8-e0dab83c2a70.1552296592',
        'dp_pwa_v_': '4918b24041ad5907d9fbe068bd4425432fb2c8c9',
        'dper': '54ab0eef9f32a7bc200c4386d1c1527251f80ce8ab88db4f6fddd7a56975eca4e13fd04d16a8919289778402918ade1fdeb9023b88d57804bb852304e8d1a5dd76e79d1f556b19022584e0953d27cad58d3efc0b313cc50209889f99d827a1ef',
        'll': '7fd06e815b796be3df069dec7836c3df',
        'ua': 'dpuser_0228649147',
        'ctu': '05813833daa55e9ae518c439c336164206edca84febb530c48e8da18ea17728e',
        'default_ab': 'index%3AA%3A1%7Cmyinfo%3AA%3A1',
        'logan_session_token': 'u63twijiwhz2ixydysuj',
        '_lxsdk_s': '1696c1626f4-691-3ac-c78%7C%7C12',
    }
    def __init__(self, city):
        if isinstance(city, int):
            self.id = city
        elif isinstance(city, dict):
            self.id = city['id']
    def search(self, keyword, page = 1):
        url = 'https://m.dianping.com/isoapi/module'
        data = {
            "pageEnName":"shopList",
            "moduleInfoList":[{
                "moduleName":"mapiSearch",
                "query":{"search":
                {
                    "start":0,
                    "categoryId":0,
                    "parentCategoryId":0,
                    "locateCityid":3199,
                    "limit":20,
                    "sortId":0,
                    "cityId": self.id,
                    "keyword": keyword,
                    "regionId":0,
                    "myLat":36.204823999999995,"myLng":138.252924,"maptype":0
                }}}
            ]}
        result = []
        HEADERS['Content-Type']='application/json'
        HEADERS['charset']='UTF-8'
        res = requests.post(url, headers=HEADERS, cookies=self.cookies, json=data)
        # print(res.content)
        shops = []
        try:
            content = res.json()
        except:
            return result
        if 'recordCount' not in content['data']['moduleInfoList'][0]['moduleData']['data']['listData'].keys():
            return result
        
        count = content['data']['moduleInfoList'][0]['moduleData']['data']['listData']['recordCount']
        for v in content['data']['moduleInfoList'][0]['moduleData']['data']['listData']['list']:
            shop = Shop(v['id'])
            shop.adShop = v['adShop']
            shop.altName = v['altName']
            shop.authorityLabelColor = v['authorityLabelColor']
            shop.authorityLabelType = v['authorityLabelType']
            shop.bookable = v['bookable']
            shop.branchName = v['branchName']
            shop.categoryId = v['categoryId']
            shop.categoryName = v['categoryName']
            shop.cityId = v['cityId']
            shop.defaultPic = v['defaultPic']
            if 'dishtags' in v.keys():
                shop.dishtags = v['dishtags']
            else:
                shop.dishtags = ''
            shop.extraJson = v['extraJson']
            shop.hasBeautyBooking = v['hasBeautyBooking']
            shop.hasDeals = v['hasDeals']
            shop.hasMoPay = v['hasMoPay']
            shop.hasPrefer = v['hasPrefer']
            shop.hasPromo = v['hasPromo']
            shop.hasTakeaway = v['hasTakeaway']
            shop.hotelBookable = v['hotelBookable']
            shop.id = v['id']
            shop.matchText = v['matchText']
            shop.name = v['name']
            shop.orderDish = v['orderDish']
            shop.poiType = v['poiType']
            if 'priceText' in v.keys():
                shop.priceText = v['priceText']
            else:
                shop.priceText = ''
            shop.queueable = v['queueable']
            if 'recommendReason' in v.keys():
                shop.recommendReason = v['recommendReason']
            else:
                shop.recommendReason = []

            shop.recommendReasonData = v['recommendReasonData']
            shop.regionName = v['regionName']
            shop.reviewCount = v['reviewCount']
            shop.scoreText = v['scoreText']
            shop.shopPositionInfo = v['shopPositionInfo']
            shop.shopPower = v['shopPower']
            shop.shopStateInformation = v['shopStateInformation']
            shop.shopType = v['shopType']
            shop.shopUuid = v['shopUuid']
            shop.status = v['status']
            if 'tagList' in v.keys():
                shop.tagList = v['tagList']
            else:
                shop.tagList = []
            shop.shopId = v['shopId']
            shops.append(shop)
        print(shops)
        if page * 20 >= count:
            return shops
        else:
            page = page + 1
            return shops + self.search(keyword, page)

        # reviews=[]
        # for v in content['data']['moduleInfoList'][0]['moduleData']['data']['reviewList']:
        #     review = Review(v)
        #     self.reviews.append(review)
        #     reviews.append(review)
        # return reviews
class Shop:

    id = None
    cookie = None
    is_proxy = False
    proxies_bak = []
    proxies = {'http':'','https':''}
    reviews = []

    def __init__(self, shop):
        if isinstance(shop, int):
            self.id = shop
        elif isinstance(shop, dict):
            self.id = shop['id']

    def set_cookie(self, cookie):
        self.cookie = cookie

    def __str__(self):
        return json.dumps({
            'id': self.id,
        }, ensure_ascii=False)

    def get_reviews(self, page=1):
        if not hasattr(self, 'posts'):
            self.posts = []
        url = 'https://m.dianping.com/isoapi/module'
        cookies = {
            'cityid': '1',
            'msource': 'default',
            'chwlsource': 'default',
            '_lxsdk_cuid': '1696c16406cc8-0d2fcac86e6dbe-36677905-fa000-1696c16406cc8',
            '_lxsdk': '1696c16406cc8-0d2fcac86e6dbe-36677905-fa000-1696c16406cc8',
            'logan_custom_report': '',
            'switchcityflashtoast': '1',
            '_hc.v': '78163bb8-d937-1dae-dad8-e0dab83c2a70.1552296592',
            'dp_pwa_v_': '4918b24041ad5907d9fbe068bd4425432fb2c8c9',
            'dper': '54ab0eef9f32a7bc200c4386d1c1527251f80ce8ab88db4f6fddd7a56975eca4e13fd04d16a8919289778402918ade1fdeb9023b88d57804bb852304e8d1a5dd76e79d1f556b19022584e0953d27cad58d3efc0b313cc50209889f99d827a1ef',
            'll': '7fd06e815b796be3df069dec7836c3df',
            'ua': 'dpuser_0228649147',
            'ctu': '05813833daa55e9ae518c439c336164206edca84febb530c48e8da18ea17728e',
            'default_ab': 'index%3AA%3A1%7Cmyinfo%3AA%3A1',
            'logan_session_token': 'u63twijiwhz2ixydysuj',
            '_lxsdk_s': '1696c1626f4-691-3ac-c78%7C%7C12',
        }
        data = {"moduleInfoList":[{"moduleName":"reviewlist","query":{"shopId":(self.id),"offset":10*(page-1),"limit":10,"type":2,"pageDomain":"m.dianping.com"}}],"pageEnName":"shopreviewlist"}

        posts = []
        HEADERS['Content-Type']='application/json'
        HEADERS['charset']='UTF-8'
        res = requests.post(url, headers=HEADERS, cookies=cookies, json=data)
        try:
            content = res.json()
        except:
            return posts
        reviews=[]
        for v in content['data']['moduleInfoList'][0]['moduleData']['data']['reviewList']:
            review = Review(v)
            self.reviews.append(review)
            reviews.append(review)
        return reviews

class Review:

    id = None

    def __init__(self, review):
        if isinstance(review, int):
            self.id = review
        elif isinstance(review, dict):
            self.pics = []
            if 'reviewPics' in review.keys():
                for v in review['reviewPics']:
                    pic = Pic(v)
                    self.pics.append(pic)
            if 'reviewId' in review.keys():
                self.id = review['reviewId']
            if 'reviewBody' in review.keys():
                self.content = review['reviewBody']
            if 'avgPrice' in review.keys():
                self.avg_price = review['avgPrice']
            if 'userNickName' in review.keys():
                self.user_nickname = review['userNickName']
            if 'addTime' in review.keys():
                GMT_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
                self.published_at = datetime.datetime.strptime(review['addTime'], GMT_FORMAT).strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return json.dumps({
            'id': self.id,
            'content': self.content,
            'avg_price': self.avg_price,
            'user_nickname': self.user_nickname,
            'published_at': self.published_at,
        }, ensure_ascii=False)

    def load(self):
        print('load:todo')

class Pic:

    id = None
    url = None
    bigurl = None

    def __init__(self, pic):
        if isinstance(pic, int):
            self.id = pic
        elif isinstance(pic, dict):
            if 'picId' in pic.keys():
                self.id = pic['picId']
            if 'url' in pic.keys():
                self.url = pic['url']
            if 'bigurl' in pic.keys():
                self.high_url = pic['bigurl']

class Search:

    line = []
    is_proxy = False
    proxies_bak = []
    proxies = {'http':'','https':''}

    def use_proxy(self):
        self.is_proxy = True
        self.proxies_bak = load_proxies()

    def get_proxy(self):
        length = len(self.proxies_bak['http'])
        if length > 0:
            r = random.randint(0, length-1)
            self.proxies['http'] = self.proxies_bak['http'][r]['host']+':'+str(self.proxies_bak['http'][r]['port'])
        length = len(self.proxies_bak['https'])
        if length > 0:
            r = random.randint(0, length-1)
            self.proxies['https'] = self.proxies_bak['https'][r]['host']+':'+str(self.proxies_bak['https'][r]['port'])

    def load(self, keyword, page=1):
        url = 'https://m.weibo.cn/api/container/getIndex'
        params = {
            'containerid': '100103type=61&q='+keyword,
            'page': page,
            'page_type': 'searchall',
        }
        headers = HEADERS
        if self.is_proxy:
            self.get_proxy()
            res = requests.get(url, params=params,
                               headers=headers, proxies=self.proxies)
        else:
            res = requests.get(url, params=params, headers=headers)
        try:
            content = res.json()
        except:
            return []
        items = []
        for v in content['data']['cards'][0]['card_group']:
            post = Post(v['mblog'])
            self.line.append(post)
            items.append(post)
        return items


