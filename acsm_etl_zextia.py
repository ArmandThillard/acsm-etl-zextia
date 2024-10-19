import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import gdrive_service
import acsm_service
import live_timings
import transform

cars = gdrive_service.get_cars()

lt = live_timings.LiveTimings(acsm_service.get_live_timings())

connected_drivers = lt.get_connected_drivers()
disconnected_drivers = lt.get_disconnected_drivers()

drivers = []

if connected_drivers is not None:
    drivers = drivers + connected_drivers

if disconnected_drivers is not None:
    drivers = drivers + disconnected_drivers

gdrive_service.set_results(transform.transform(drivers, cars))