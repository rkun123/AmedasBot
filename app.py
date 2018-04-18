from twitter import *
from tokensLoader import Loader
from scraper import Scraper
import datetime
from YesterdayUtil import YesterdayUtil
from graph import GraphMaker
import time

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


def main():
    #Start time hour.
    lastHour = datetime.datetime.today().hour
    lastDay = datetime.datetime.today().day
    #Check on loop(by 30 seconds)
    while True:
        print("Start Checking...")
        #New day check
        if lastDay != datetime.datetime.today().day:
            lastHour = 0;
            lastday = datetime.datetime.today().day
        #Load Web
        sc = Scraper()
        data = sc.scrape()
        if lastHour < int(data["time"]):
            #on updated
            lastHour = int(data["time"])
            tweet(data)
        print("Finish Checking.")
        #wait 30 seconds
        time.sleep(30)

#Tweet Function
def tweet(_data):
    nowTime = datetime.datetime.today();
    timeString = nowTime.strftime("%H:%M")
    msg = TEMPLATE.format(_data["time"],_data["temp"],_data["rain"],_data["windAngle"],_data["windSpeed"],_data["sunrisetime"],_data["humidity"],_data["airplessure"],timeString)
    print(msg)
    imageFile = open("./output.png","rb").read()
    params = {"media[]": imageFile, "status":msg}
    #t.statuses.update_with_media(**params)

    t.statuses.update(status=msg)

if __name__ == "__main__":
    main()
