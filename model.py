from peewee import *

database = MySQLDatabase('fapiao', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'pass@dbmima'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Cities(BaseModel):
    tuangouflag = CharField(column_name='TuanGouFlag', null=True)
    apphotlevel = CharField(column_name='appHotLevel', null=True)
    cityabbrcode = CharField(column_name='cityAbbrCode', null=True)
    cityareacode = CharField(column_name='cityAreaCode', null=True)
    cityenname = CharField(column_name='cityEnName', null=True)
    cityid = CharField(column_name='cityId', null=True)
    citylevel = CharField(column_name='cityLevel', null=True)
    cityname = CharField(column_name='cityName', null=True)
    cityorderid = CharField(column_name='cityOrderId', null=True)
    citypyname = CharField(column_name='cityPyName', null=True)
    directurl = CharField(column_name='directURL', null=True)
    glat = CharField(column_name='gLat', null=True)
    glng = CharField(column_name='gLng', null=True)
    hasreturl = CharField(column_name='hasReturl', null=True)
    isactivecity = CharField(column_name='isActiveCity', null=True)
    isoverseascity = CharField(column_name='isOverseasCity', null=True)
    isscenery = CharField(column_name='isScenery', null=True)
    parentcityid = CharField(column_name='parentCityId', null=True)
    provinceid = CharField(column_name='provinceId', null=True)
    standardenname = CharField(column_name='standardEnName', null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'cities'

class Pics(BaseModel):
    download = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    high_url = CharField(null=True)
    origin = IntegerField(column_name='origin_id', null=True)
    published_at = DateTimeField(null=True)
    result = CharField(null=True)
    source = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'pics'

class Reviews(BaseModel):
    actions = CharField(null=True)
    content = TextField(null=True)
    origin = IntegerField(null=True)
    pics = CharField(null=True)
    published_at = DateTimeField(null=True)
    score = CharField(null=True)
    shop_name = CharField(null=True)
    shop_source = CharField(null=True)
    source = CharField(null=True)
    star = CharField(null=True)
    url = CharField(null=True)
    user_img = CharField(null=True)
    user_level = CharField(null=True)
    user_nickname = CharField(null=True)
    user_source = CharField(null=True)
    user_url = CharField(null=True)
    user_vip = CharField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'reviews'

class Stores(BaseModel):
    avg_price = IntegerField(null=True)
    city = CharField(null=True)
    environmental_srore = DecimalField(null=True)
    latitude = CharField(null=True)
    logo = CharField(null=True)
    longitude = CharField(null=True)
    mobile = CharField(null=True)
    name = CharField(null=True)
    origin = IntegerField(null=True)
    power_title = CharField(null=True)
    reviews = IntegerField(null=True)
    service_score = DecimalField(null=True)
    source = IntegerField(null=True)
    taste_score = DecimalField(null=True)

    class Meta:
        table_name = 'stores'

