# Transform ACSM live timings json to fit gsheet file
def transform(drivers, carList):
    res = []
    
    for driver in drivers:
        name = driver['CarInfo']['DriverName']
        for car, info in driver['Cars'].items():
            c = {
                'driver': name,
                'carName': info['CarName'],
                'carRef': car,
                'class': next((sub for sub in carList if sub['Ref'] == car), None)['Catégorie'],
                'numLaps': info['NumLaps'],
                'bestLap': info['BestLap'],
                'topSpeed': info['TopSpeedBestLap'],
                'totalLapTime': info['TotalLapTime'],
            }
            res.append(c)
    
    return res