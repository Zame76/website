# Import libraries
from requests import get
import config

# Url for open source api call, provider digitraffic.fi, which maintains lots of weather stations along finnish road network
# This site is located alongside Highway no 4, Oulu (Intiö), Finland (https://tie.digitraffic.fi/api/weather/v1/stations/12019)
apiurl = "https://tie.digitraffic.fi/api/weather/v1/stations/12019/data"
# Digitraffic.fi requires 
headers = {'Digitraffic-User': config.digitraffic_user}

r = get(apiurl, headers=headers)

sensors = r.json()['sensorValues']
j = 0
for i in sensors:
    print(j,"\t",i)
    j += 1

print("\n\n")
print(r.json()['dataUpdatedTime'])  #  
print("Air temp:",sensors[0]['name'],sensors[0]['value'], 'degrees(C)') 
print("Wind speed:",sensors[12]['name'],sensors[12]['value'], 'm/s')
print("Wind direction:",sensors[14]['name'],sensors[14]['value'], 'degrees')
print("Moisture:",sensors[15]['name'],sensors[15]['value'], "%")
print("Rain:",sensors[16]['name'],sensors[16]['value'],sensors[16]['sensorValueDescriptionFi'],sensors[16]['sensorValueDescriptionEn'])
