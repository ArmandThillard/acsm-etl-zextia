import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import gdrive_service
import acsm_service
import live_timings
import result
import results
import transform


tracks = gdrive_service.get_tracks()
# print(tracks)
results = results.Results(acsm_service.get_results_list())

last_result = results.get_last()

result = acsm_service.get_result(last_result['results_json_url'])

formatted_result = transform.transform(result, last_result, tracks)

gdrive_service.set_results(formatted_result)

# Sum up points
sheet_results = gdrive_service.get_results()

pts = transform.points_by_driver(sheet_results)

gdrive_service.set_pts(pts)



