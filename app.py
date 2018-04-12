from twitter import *
from tokensLoader import Loader
from scraper import Scraper
import datetime

TEMPLATE = """[飯塚アメダスBot]
時刻: {0}時
気温: {1}℃
降水量:{2}mm
風向: {3}
風速: {4}m/s
日照時間:{5}h
湿度: {6}%
気圧: {7}hPa
http://www.jma.go.jp/jp/amedas_h/today-82136.html?areaCode=000&groupCode=58
({8}投稿)"""

tokensLoader = Loader()
tokens = tokensLoader.load()
auth=OAuth(tokens["TOKEN"],tokens["TOKEN_SECRET"],tokens["CONSUMER"],tokens["CONSUMER_SECRET"])
t = Twitter(auth=auth)


def tweet():
    timeString = datetime.datetime.today().strftime("%H:%M")
    sc = Scraper()
    data = sc.scrape()
    msg = TEMPLATE.format(data["time"],data["temp"],data["rain"],data["windAngle"],data["windSpeed"],data["sunrisetime"],data["humidity"],data["airplessure"],timeString)
    print(msg)
    #t.statuses.update(status=msg)
tweet()