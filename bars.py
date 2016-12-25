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
    global max_seats
    global biggest_bar
    if bar_info['SeatsCount'] > max_seats:
        max_seats = bar_info['SeatsCount']
        biggest_bar = bar_info['Name']

def get_smallest_bar(bar_info):
    global min_seats
    global smallest_bar
    if bar_info['SeatsCount'] < min_seats:
        min_seats = bar_info['SeatsCount']
        smallest_bar = bar_info['Name']

def get_closest_bar(data, longitude, latitude):
    global min_offset_latitude
    global min_offset_longitude
    global closest_bar
    offset_latitude = fabs(latitude - float(data['Latitude_WGS84']))
    offset_longitude = fabs(longitude - float(data['Longitude_WGS84']))
    if offset_latitude < min_offset_latitude and offset_longitude < min_offset_longitude:
        min_offset_latitude = offset_latitude
        min_offset_longitude = offset_longitude
        closest_bar = data['Name']  
    

if __name__ == '__main__':

    max_seats = 0; min_seats = 100; min_offset_latitude = 100; min_offset_longitude = 100
    biggest_bar = None; smallest_bar = None; closest_bar = None
    bar_list = load_data("data.json")
    longitude,latitude = map(float,input('Input coordinates(Longitude,Latitude):  ').split(","))

    for number in range(0,len(bar_list)):
        if bar_list[number]['TypeObject'] == 'Р±Р°СЂ':
            get_biggest_bar(bar_list[number])
            get_smallest_bar(bar_list[number])
            get_closest_bar(bar_list[number], longitude, latitude)

    result_program = print_txt.format(biggest_bar = biggest_bar,
                          smallest_bar = smallest_bar,
                          closest_bar = closest_bar)       
    print(result_program)
