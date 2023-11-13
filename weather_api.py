# Import libraries
from datetime import datetime
from requests import get
import sql
import config

def getWeatherData():
    return_value = dict()
    getapi = False

    # Digitraffic.fi allows maximum of 60 apicalls per minute, so we are going to store the results into the database and only get
    # refreshed periodically in order to not get blocked by digitraffic. 
    sql.createTables()
    weather = sql.getLatestWeather()

    # Convert time from sql database to datetime format
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    sql_time = datetime.strptime(weather[0], date_format)

    # If database is empty
    if len(weather) == 0:
        # Get fresh data from api
        getapi = True
    # Otherwise check the time difference, if more than 5 minutes has passed since last api call    
    else: 
        # Get the time difference in minutes
        timediff = (datetime.now() - sql_time).total_seconds() / 60        
        # If more than 5 minutes has passed, get fresh data from api
        if timediff > 5:
            getapi = True
        # Otherwise use data from database
        else:
            getapi = False

    # Do the api call    
    if getapi == True:
        print("api")
        # Url for open source api call, provider digitraffic.fi, which maintains lots of weather stations along Finnish road network
        # This site is located alongside Highway no 4, Oulu (Intiö), Finland (https://tie.digitraffic.fi/api/weather/v1/stations/12019)
        # List of all weather stations: https://tie.digitraffic.fi/api/weather/v1/stations
        apiurl = "https://tie.digitraffic.fi/api/weather/v1/stations/12019/data"

        # Digitraffic.fi requires a user information, so we provide one. You can create your own by creating config.py on root directory
        # and inserting digitraffic_user variable with proper name. Read more: 
        # https://www.digitraffic.fi/tuki/ohjeita/#yleist%C3%A4-huomioitavaa
        headers = {'Digitraffic-User': config.digitraffic_user}
        # Make the api call and get refresh weather data
        response = get(apiurl, headers=headers)
        sensors = response.json()['sensorValues']

        # Create a tuple of parameters to be inserted to database
        parameters = (datetime.now(), sensors[0]['value'], sensors[12]['value'], sensors[14]['value'], sensors[15]['value'], 
                    sensors[16]['value'], sensors[16]['sensorValueDescriptionFi'],  sensors[16]['sensorValueDescriptionEn'])
        
        # Insert values to database
        sql.insertWeather(parameters)

        # Create dictionary
        return_value = {sensors[0]['name']:sensors[0]['value'],
                        sensors[12]['name']:sensors[12]['value'],
                        sensors[14]['name']:sensors[14]['value'],
                        sensors[15]['name']:sensors[15]['value'],
                        sensors[16]['name']:sensors[16]['value'],
                        sensors[16]['name']+"_KUVAUS":sensors[16]['sensorValueDescriptionFi'],
                        sensors[16]['name']+"_DESC":sensors[16]['sensorValueDescriptionEn']}
        
        # DEBUG INFORMATION
        # Print all the sensor data, 85 rows
        # j = 0
        # for i in sensors:
        #     print(j,"\t",i)
        #     j += 1

        # Print the collected sensor data
        # print("\n\n")
        # print(response.json()['dataUpdatedTime'])  #  
        # print("Air temp:",sensors[0]['name'],sensors[0]['value'], 'degrees(C)') 
        # print("Wind speed:",sensors[12]['name'],sensors[12]['value'], 'm/s')
        # print("Wind direction:",sensors[14]['name'],sensors[14]['value'], 'degrees')
        # print("Moisture:",sensors[15]['name'],sensors[15]['value'], "%")
        # print("Rain:",sensors[16]['name'],sensors[16]['value'])
        # print("Rain_kuvaus:", sensors[16]['name']+"_kuvaus", sensors[16]['sensorValueDescriptionFi'])
        # print("Rain_desc:", sensors[16]['name']+"_desc", sensors[16]['sensorValueDescriptionEn'])

    # Return values from sql database
    else:
        print("sql")
        # Create dictionary
        return_value = {"ILMA":weather[1],
                        "KESKITUULI":weather[2],
                        "TUULENSUUNTA":weather[3],
                        "ILMAN_KOSTEUS":weather[4],
                        "SADE":weather[5],
                        "SADE_KUVAUS":weather[6],
                        "SADE_DESC":weather[7]}

    return return_value