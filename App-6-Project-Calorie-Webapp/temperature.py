import requests
from selectorlib import Extractor

BASE_URL = "https://www.timeanddate.com/weather/"
YAML_FILE = "temperature.yaml"


class Temperature:
    def __init__(self, country, city) -> None:
        self.country = country
        self.city = city

    headers = {
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "dnt": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    }

    def __build_url(self):
        return BASE_URL + "/" + self.country + "/" + self.city

    def __preprocessing(self, temp):
        return float(temp["temp"].replace("\xa0°C", ""))

    def scrap_temp(self):
        url = self.__build_url()
        r = requests.get(url, headers=self.headers)
        c = r.text
        extractor = Extractor.from_yaml_file(YAML_FILE)
        raw_result = extractor.extract(c)
        result = self.__preprocessing(raw_result)
        return result
