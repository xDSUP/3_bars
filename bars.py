import json
from math import fabs

print_txt = """

the biggest bar: {biggest_bar} .
the smallest bar: {smallest_bar} .
the closest bar : {closest_bar} .

"""

def load_data(filepath): #returns the list of bars 
    with open(filepath, 'r') as bar_list:
        bar_list_parsed = json.loads(bar_list.read())
        return bar_list_parsed

def get_biggest_bar(bar_list):#returns the greatest bar
    max_seats = 0
    for bar in bar_list:
        if bar['SeatsCount'] > max_seats:
            max_seats = bar['SeatsCount']
            biggest_bar = bar['Name']
    return biggest_bar
def get_smallest_bar(bar_list):#returns the smallest bar
    min_seats = 1000
    for bar in bar_list:
        if bar['SeatsCount'] < min_seats:
            min_seats = bar['SeatsCount']
            smallest_bar = bar['Name']
    return smallest_bar
def get_closest_bar(bar_list, longitude, latitude):#returns the closest bar
    min_offset_latitude = 1000 
    min_offset_longitude = 1000 #values express the minimum difference between coordinates
    for bar in bar_list:
        offset_latitude = fabs(latitude - float(bar['Latitude_WGS84']))
        offset_longitude = fabs(longitude - float(bar['Longitude_WGS84']))
        if offset_latitude < min_offset_latitude and offset_longitude < min_offset_longitude:
            min_offset_latitude = offset_latitude
            min_offset_longitude = offset_longitude
            closest_bar = bar['Name']  
    return closest_bar
if __name__ == '__main__':
    bar_list = load_data("data.json")
    longitude,latitude = map(float,input('Input coordinates(Longitude,Latitude):  ').split(","))
    biggest_bar = get_biggest_bar(bar_list)
    smallest_bar = get_smallest_bar(bar_list)
    closest_bar = get_closest_bar(bar_list, longitude, latitude)
    result_program = print_txt.format(biggest_bar = biggest_bar,
                          smallest_bar = smallest_bar,
                          closest_bar = closest_bar)       
    print(result_program)
