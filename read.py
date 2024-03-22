import time
import csv

def read_csv_live(live_file):
    lat_coors_list = []
    long_coors_list = []
    highest_percentage = -1
    while True:
        try:
            with open(live_file,'r') as file:
                #creating a csv reader object
                csv_reader = csv.reader(file)
                accuracyIndex = 0
                index = 0
                # read file line by line
                for row in csv_reader:
                    # 'row' variable contains the data of the current line as a list
                    # access latitude at index 8
                    latitude = float(row[8])
                    # access longitude at index 9
                    longitude = float(row[9])
                    # boolean values for if latitude and longitude are already in list
                    lat_yes = False
                    long_yes = False
                    # go through lat_coors_list to see if lat is in there (almost the same, can be 0.0001 off)
                    for i in lat_coors_list:
                        # if lat is in there set boolean to True
                        if(i >= latitude - 0.0001 and i <= latitude + 0.0001):
                            lat_yes = True
                    # go through long_coors_list to see if long is in there (almost the same, can be 0.0001 off)
                    for i in long_coors_list:
                        # if long is in there set boolean to True
                        if(i >= longitude - 0.0001 and i <= longitude + 0.0001):
                            long_yes = True
                    # if lat_yes and long_yes are True, exit out of while loop (stop reading the live_file)
                    if(lat_yes and long_yes):
                        break
                    # save coordinates in list so can compare them later
                    lat_coors_list.append(latitude)
                    long_coors_list.append(longitude)
                    # store highest value in highest_percentage
                    if(float(row[2]) > highest_percentage):
                        highest_percentage = float(row[2])
                        accuracyIndex = index
                    if (highest_percentage >= 98):
                        return lat_coors_list, long_coors_list, accuracyIndex
                    index = index + 1

                return lat_coors_list, long_coors_list, accuracyIndex
        # add exception
        except Exception as e:
             print("Error:", e)