from bs4 import BeautifulSoup
from urllib import request

class Scraper:
    def __init__(self):
        self.URL = "http://www.jma.go.jp/jp/amedas_h/today-82136.html?areaCode=000&groupCode=58"

    def scrape(self):
        htmlBody = request.urlopen(self.URL)
        soup = BeautifulSoup(htmlBody,"html.parser")
        datalist = soup.find(id="tbl_list").find_all("tr")
        datalist.pop(0)

        for i in (range(23,0,-1)):
            data = datalist[i].find_all("td",class_="block middle")
            if  data[0].get_text() != "\xa0":
                idx = datalist[i].find_all("td",class_="time left")
                res = {}
                res["time"] = idx[0].get_text()
                res["temp"] = data[0].get_text()
                res["rain"] = data[1].get_text()
                res["windAngle"] = data[2].get_text()
                res["windSpeed"] = data[3].get_text()
                res["sunrisetime"] = data[4].get_text()
                res["humidity"] = data[5].get_text()
                res["airplessure"] = data[6].get_text()
                #print(res)
                return res




#for debug
sc = Scraper()
sc.scrape()
