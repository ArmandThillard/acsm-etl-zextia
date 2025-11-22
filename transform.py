# Transform ACSM live timings json to fit gsheet file
def transform(result, result_info, tracks):
    res = []

    lookup = {item['Circuit']: item['Longueur (m)'] for item in tracks}

    for driver_result in result['Result']:
        dr = {
            'DriverName': driver_result['DriverName'],
            'track': result_info['track'],
            'session_type': result_info['session_type'],
            'CarModel': driver_result['CarModel'],
            'TotalTime': driver_result['TotalTime'],
            'NumLaps': driver_result['NumLaps'],
            'GridPosition': driver_result['GridPosition'],
            'Distance': lookup['paul_ricard_2021'] * driver_result['NumLaps'] / 1000
        }
        res.append(dr)
    
    return res

# Calculate points by driver
def points_by_driver(results):
    res = {}

    for result in results:
        if result['Pilote'] in res:
            # print(result['Distance parcourue (km)'])
            res[result['Pilote']]['Temps total (min)'] += (result['Temps total (ms)'] / 1000 / 60)
            res[result['Pilote']]['Tours'] += result['Tours']
            res[result['Pilote']]['Distance parcourue (km)'] += result['Distance parcourue (km)']
        else:
            acc = {
                'Pilote': result['Pilote'],
                'Temps total (s)': result['Temps total (ms)'] / 1000 / 60,
                'Tours': result['Tours'],
                'Distance parcourue (km)': result['Distance parcourue (km)'],
                'Points': (result['Temps total (ms)'] / 1000 / 60) * 2,
                'Bonus': 0,
            }
            res[result['Pilote']] = acc

    return res
