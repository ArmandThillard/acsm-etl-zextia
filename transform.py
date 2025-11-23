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
def points_by_driver(results, paliers):
    res = {}

    for result in results:
        if result['Pilote'] in res:
            res[result['Pilote']]['Temps total (min)'] += (result['Temps total (ms)'] / 1000 / 60)
            res[result['Pilote']]['Tours'] += result['Tours']
            res[result['Pilote']]['Distance parcourue (km)'] = res[result['Pilote']]['Distance parcourue (km)'] + (result['Distance parcourue (km)'] / 100)
            res[result['Pilote']]['Points'] = res[result['Pilote']]['Temps total (min)'] * 2
            res[result['Pilote']]['Bonus'] = get_bonus(paliers, res[result['Pilote']]['Distance parcourue (km)'] )
        else:
            acc = {
                'Pilote': result['Pilote'],
                'Temps total (min)': result['Temps total (ms)'] / 1000 / 60,
                'Tours': result['Tours'],
                'Distance parcourue (km)': result['Distance parcourue (km)'] / 100,
                'Points': (result['Temps total (ms)'] / 1000 / 60) * 2,
                'Bonus': 0,
            }
            res[result['Pilote']] = acc

    return res

def get_bonus(paliers, distance):
    bonus = 0

    if(distance >= paliers[0]['Distance parcourue (km)']):
        bonus = paliers[0]['Bonus']

    if(distance >= paliers[1]['Distance parcourue (km)']):
        bonus = paliers[1]['Bonus']

    if(distance >= paliers[2]['Distance parcourue (km)']):
        bonus = paliers[2]['Bonus']

    if(distance >= paliers[3]['Distance parcourue (km)']):
        bonus = paliers[3]['Bonus']

    if(distance >= paliers[4]['Distance parcourue (km)']):
        bonus = paliers[4]['Bonus']
    
    return bonus