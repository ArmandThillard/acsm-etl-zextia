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

# Calculate points by driver
def points_by_driver(drivers, classes):
    res = {}

    for driver in drivers:
        if driver['driver'] in res:
            
            if driver['class'] == 'GT3':
                res[driver['driver']]['lapsGt3'] += driver['numLaps']
                res[driver['driver']]['ptsGt3'] += next((sub for sub in classes if sub['Catégorie'] == 'GT3'), 0)['Pts/tour'] * driver['numLaps']
            
            if driver['class'] == 'GT4':
                res[driver['driver']]['lapsGt4'] += driver['numLaps']
                res[driver['driver']]['ptsGt4'] += next((sub for sub in classes if sub['Catégorie'] == 'GT4'), 0)['Pts/tour'] * driver['numLaps']


            res[driver['driver']]['totalLaps'] = res[driver['driver']]['lapsGt3'] + res[driver['driver']]['lapsGt4']
            res[driver['driver']]['totalPts'] = res[driver['driver']]['ptsGt3'] + res[driver['driver']]['ptsGt4']
        else:
            acc = {
                'driver': driver['driver'],
                'lapsGt3': 0,
                'lapsGt4': 0,
                'totalLaps': 0,
                'ptsGt3': 0,
                'ptsGt4': 0,
                'totalPts': 0,
            }

            if driver['class'] == 'GT3':
                acc['lapsGt3'] = driver['numLaps']
                acc['totalLaps'] = driver['numLaps']
                acc['ptsGt3'] = next((sub for sub in classes if sub['Catégorie'] == 'GT3'), 0)['Pts/tour'] * driver['numLaps']
                acc['totalPts'] = acc['ptsGt3']
            
            if driver['class'] == 'GT4':
                acc['lapsGt4'] = driver['numLaps']
                acc['totalLaps'] = driver['numLaps']
                acc['ptsGt4'] = next((sub for sub in classes if sub['Catégorie'] == 'GT4'), 0)['Pts/tour'] * driver['numLaps']
                acc['totalPts'] = acc['ptsGt4']

            res[driver['driver']] = acc
    
    return res
