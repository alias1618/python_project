


import requests

urlPathApi = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-82BFBBC6-50D9-40EE-9E28-8317814A2503&format=JSON"

def get_weather_of_taiwan():
    try:
        response = requests.get(urlPathApi)
        response.raise_for_status()
    except requests.ConnectionError as e:
        print(e)
        return None
    except requests.HTTPError as e:
        print(e)
        return None
    except requests.Timeout as e:
        print(e)
        return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    allData = response.json()
    locations = allData["records"]['location']
    weatherList = []
    for item in locations:
        itemDic = {}
        itemDic['縣市'] = item['parameter'][0]['parameterValue']
        itemDic['區域'] = item['parameter'][2]['parameterValue']
        itemDic['時間'] = item['time']['obsTime']
        itemDic['溫度'] = float(item['weatherElement'][3]['elementValue'])
        weatherList.append(itemDic)
    return str(weatherList)