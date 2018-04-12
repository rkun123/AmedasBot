from twitter import *
from tokensLoader import Loader
from notifyScraper import Notify

tokensLoader = Loader()
tokens = tokensLoader.load()
auth=OAuth(tokens["TOKEN"],tokens["TOKEN_SECRET"],tokens["CONSUMER"],tokens["CONSUMER_SECRET"])
t = Twitter(auth=auth)

def notifycheck():
    notifyGetter = Notify()
    latestNotify = notifyGetter.getLatestDetail()
    msgTemplate = """タイトル {0}
日時 {1}
時限等 {2}
対象 {3}
対象学年 {4}
{5}"""
    msg = msgTemplate.format(latestNotify["title"],latestNotify["date"],latestNotify["time"],latestNotify["target"],latestNotify["targetGrade"],latestNotify["url"])
    print(msg)
    t.statuses.update(status=msg)
notifycheck()