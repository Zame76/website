from datetime import date, datetime, timezone, timedelta
from requests import get

import xmltodict
import config

# In this file, we are going to get electricity prices for today and tomorrow (when available)
# To use this feature, you will need to register to the site https://transparency.entsoe.eu/
# and after that, ask permission to use Api by email. You will then generate the needed security token
# and store it to the config.py file as entsoe_securitytoken variable.
# More information here: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html

def getElectricityPrices():
    # Get date as tuple so we can construct period start and end for api call
    datetuple = date.today().timetuple()
    # Code to get electricity prices in Finland
    finland = "10YFI-1--------U"
    # Construct api call
    apiurl = "https://web-api.tp.entsoe.eu/api"
    # Set generated security token to api call
    apiurl += "?securityToken=" + config.entsoe_securitytoken
    apiurl += "&documentType=A44"
    # Set country code to fetch the prices in Finland
    apiurl += "&out_Domain=" + finland
    apiurl += "&in_Domain=" + finland
    # Set the start and end times to get todays prices using datetuple and adding time itself
    apitimes = "&periodStart=" + str(datetuple[0]) + str(datetuple[1]) + str(datetuple[2] - 1) + "2300"
    apitimes += "&periodEnd=" + str(datetuple[0]) + str(datetuple[1]) + str(datetuple[2]) + "2300"
    # Get the data
    response = get(apiurl + apitimes)

    # TODO get tomorrows prices
    
    # Data comes in xml format, which was a real pain to try and read with python. Luckily, there is this 
    # nice little module that turns xml data to structured collection of dictionaries and occasional lists.
    responsedict = xmltodict.parse(response.content)
    print(responsedict)
    print("-" * 80)

    print("UTC:", datetime.now().astimezone(timezone.utc))
    print("CET:",datetime.now(timezone(timedelta(hours=+1), 'CET')))
    #print("CET:", datetime.now().astimezone(timezone.utcoffset('+1')))
    #print("EET:", datetime.now().astimezone(timezone.utcoffset(2)))
    
    print("-" * 80)

    # This block collects today's electricity price data
    # Timezone for the prices the api returns seems to be CET
    i = 0
    print("start:", responsedict['Publication_MarketDocument']['TimeSeries']['Period']['timeInterval']['start'])
    time_cet = responsedict['Publication_MarketDocument']['TimeSeries']['Period']['timeInterval']['start']
    print("end:", responsedict['Publication_MarketDocument']['TimeSeries']['Period']['timeInterval']['end'])
    # Hourly prices are inside many Point dictionaries, so we need to loop them through to get the data
    for item in responsedict['Publication_MarketDocument']['TimeSeries']['Period']['Point']: 
        print(i, "\t", item['position'], "\t", item['price.amount'])    
        i += 1
    # print("start:", respdict['Publication_MarketDocument']['TimeSeries'][0]['Period']['timeInterval']['start'])
    # print("end:", respdict['Publication_MarketDocument']['TimeSeries'][0]['Period']['timeInterval']['end'])
    # # Hourly prices are inside many Point dictionaries, so we need to loop them through to get the data
    # for item in respdict['Publication_MarketDocument']['TimeSeries'][0]['Period']['Point']: 
    #     print(i, "\t", item['position'], "\t", item['price.amount'])    
    #     i += 1
    # print("-" * 80)
    # # This block collects tomorrow's electricity price data, marked by [1] between TimeSeries and Period
    # # Timezone is UTC
    # i = 0
    # print("start:", respdict['Publication_MarketDocument']['TimeSeries'][1]['Period']['timeInterval']['start'])
    # print("end:", respdict['Publication_MarketDocument']['TimeSeries'][1]['Period']['timeInterval']['end'])
    # # Hourly prices are inside many Point dictionaries, so we need to loop them through to get the data
    # for item in respdict['Publication_MarketDocument']['TimeSeries'][1]['Period']['Point']: 
    #     print(i, "\t", item['position'], "\t", item['price.amount'])    
    #     i += 1


    return "not finished yet"

# DEBUG function call
getElectricityPrices()