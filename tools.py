import requests
import csv
from io import StringIO
import password

class Site(object):
    def __init__(self, name, county, aqi) -> None:
        super().__init__()
        self.site_name = name
        self.county = county
        try:
            self.aqi = int(aqi)
        except:
            self.aqi = 999

    def __repr__(self) -> str:
        return f"站點:{self.site_name},城市:{self.county},aqi:{self.aqi}"


class Taiwan_AQI():

    @classmethod
    def download_aqi(cls) -> list:
        response = requests.get(
            f"https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={password.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV")

        if response.ok:
            # print(response.text)
            # file = open("./lesson17/aqi.csv",mode="w",encoding="utf -8")
            # file.write(response.text)
            # file.close()
            file = StringIO(response.text, newline="")
            csvReader = csv.reader(file)
            next(csvReader)
            dataList = []
            for item in csvReader:
                site = Site(item[0], item[1], item[2])
                dataList.append(site)
            return dataList

            '''
            for item in csvReader:
                print(item[0])
            '''

        else:
            raise Exception("下載失敗")