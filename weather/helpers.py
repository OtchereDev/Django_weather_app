import os 
import requests


apikey=os.getenv('ACCUWEATHER_APIKEY')


def getLocationDet(city):

    respone=requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={apikey}&q={city}')

    # return bool(respone.json())

    return respone.json()[0] if respone.json() else None



def getTemperatureDet(locationKey):

    temp_response=requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{locationKey}?apikey={apikey}')

    return temp_response.json()


print(getLocationDet('accra'))