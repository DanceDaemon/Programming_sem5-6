import requests
import json
import datetime

key = "0e850ed0-ff74-43a2-896e-e09c26949f26"
dt = 1656600000
city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19

def getweather(api_key=None):
    import json
    import requests
    if api_key:
        url = ('https://api.weather.yandex.ru/v2/forecast/?lat='+str(lat)+'&lon='+str(lon)+'&lang=ru_RU')
        req = requests.get(
            url,
            headers = {
                "X-Yandex-API-Key": str(api_key)
            }
            )
    return(json.loads(req.text)) 

def get_forecast(req_obj):
    days_lst = [obj for obj in req_obj["forecasts"]]
    weather={}
    for day in days_lst:
        for hour in day['hours']:
            weather[str(day["date"]) + " " + str(hour['hour']) + "ч"] = hour["temp"]


    result={}
    result['city'] = city
    result["measures"] = [{
            "dt": str(measure[0]),
            "temp": int(measure[1])
        } for measure in list(weather.items())]
    return(json.dumps(result))

def get_avg_temp(req_obj):
    days_lst = [obj for obj in req_obj["forecasts"]]
    avg={}
    for day in days_lst:
        avg[day["date"]] = day["parts"]["day"]["temp_avg"]
    result={}
    result['city'] = city
    result["temp_avg"] = [{
        "dt": str(t[0]),
        "temp": t[1]
    } for t in list(avg.items())]
    return(json.dumps(result))

def visualise_data(hourly_data='', avg_temp_data=''):
    if hourly_data:
        import matplotlib
        import matplotlib.pyplot as pplt
        import pandas
        
        data = pandas.read_json(hourly_data)
        print(data)
        
        dates = [_d['dt'] for _d in data["measures"]]
        temps = [_t['temp'] for _t in data["measures"]]

        pplt.figure(figsize=(15,7))
        pplt.scatter(
            dates, temps,
        )
        pplt.title(f"Погода в {data['city'][0]} на 4 дня от " + datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d'))
        pplt.xlabel('Дата и время')
        pplt.ylabel('Температура')
        pplt.yticks(temps[::1])
        pplt.xticks(dates[::10])

        pplt.show()

    if avg_temp_data:
        import matplotlib
        import matplotlib.pyplot as pplt
        import pandas

        data = pandas.read_json(avg_temp_data)
        print(data)

        dates = [_d['dt'] for _d in data["temp_avg"]]
        temps = [_t['temp'] for _t in data["temp_avg"]]
        
        pplt.figure(figsize=(15,7))

        pplt.scatter(
            dates,
            temps,
        )
        pplt.title(f"Средняя температура в {data['city'][0]} на 4 дня от " + datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d'))
        pplt.xlabel('Дата')
        pplt.ylabel('Температура')
        pplt.yticks(temps[::1])
        pplt.xticks(dates[::1])

        pplt.show()

data = getweather(key)
forecast = get_forecast(data)
avg_temp = get_avg_temp(data)
visualise_data(forecast, avg_temp)