import json
from math import fabs

printTXT = """

the biggest bar: {biggest_bar} .
the smallest bar: {smallest_bar} .
the closest bar : {closest_bar} .

"""

def load_data(filepath):
    file_json = open(filepath, 'r')
    bar_list = file_json.read()
    bar_list_parsed = json.loads(bar_list)
    file_json.close()
    return bar_list_parsed

def get_biggest_bar(bar_info):
    global MAX
    global BIGGEST_BAR
    if bar_info['SeatsCount'] > MAX:
        MAX = bar_info['SeatsCount']
        BIGGEST_BAR = bar_info['Name']

def get_smallest_bar(bar_info):
    global MIN
    global SMALLEST_BAR
    if bar_info['SeatsCount'] < MIN:
        MIN = bar_info['SeatsCount']
        SMALLEST_BAR = bar_info['Name']

def get_closest_bar(data, longitude, latitude):
    global MIN_OFFSET_LATITUDE
    global MIN_OFFSET_LONGITUDE
    global CLOSEST_BAR
    offset_latitude = fabs(latitude - float(data['Latitude_WGS84']))
    offset_longitude = fabs(longitude - float(data['Longitude_WGS84']))
    if offset_latitude < MIN_OFFSET_LATITUDE and offset_longitude < MIN_OFFSET_LONGITUDE:
        MIN_OFFSET_LATITUDE = offset_latitude
        MIN_OFFSET_LONGITUDE = offset_longitude
        CLOSEST_BAR = data['Name']  
    

if __name__ == '__main__':

    MAX = 0; MIN = 100; MIN_OFFSET_LATITUDE = 100; MIN_OFFSET_LONGITUDE = 100
    BIGGEST_BAR = None; SMALLEST_BAR = None; CLOSEST_BAR = None
    bar_list = load_data("data.json")
    longitude,latitude = map(float,input('Input coordinates(Longitude,Latitude):  ').split(","))

    for number in range(0,len(bar_list)):
        if bar_list[number]['TypeObject'] == 'Р±Р°СЂ':
            get_biggest_bar(bar_list[number])
            get_smallest_bar(bar_list[number])
            get_closest_bar(bar_list[number], longitude, latitude)

    result_program = printTXT.format(biggest_bar = BIGGEST_BAR,
                          smallest_bar = SMALLEST_BAR,
                          closest_bar = CLOSEST_BAR)       
    print(result_program)
