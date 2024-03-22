import time
from planefunction import *
from read import *

filename = "kraken_3.csv"

armplane()
mode = "TAKEOFF"
changemode(mode)


latlist, longtlist, index = read_csv_live(filename)

lat, longt = float(latlist[index]), float(longtlist[index])

takeoffplane()
time.sleep(10)

mode = "AUTO"
changemode(mode)

missionStart(lat, longt)