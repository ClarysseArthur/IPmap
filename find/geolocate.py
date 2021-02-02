from ip2geotools.databases.noncommercial import DbIpCity

def locate(ipList):
    latitude = 0 
    longitude = 0
    location = []
    locationList = []

    for x in ipList:
        try:
            response = DbIpCity.get(x, api_key='free')

            print(f'\n-----------------------------')
            print(f'IP:\t{x}')
            print(f'Stad:\t{response.city}')
            print(f'Regio:\t{response.region}')
            print(f'Land:\t{response.country}')
            print(f'LAT:\t{response.latitude}')
            print(f'LONG:\t{response.longitude}')
            print('-----------------------------\n')

            latitude = float(round(response.latitude, 4))
            longitude = float(round(response.longitude, 4))

            location = [x, latitude, longitude]

            locationList.append(location)
        except:
            print(f'{x} is niet gevonden!')

    return locationList